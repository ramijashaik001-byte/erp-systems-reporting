# AuraLedger Core Database Simulator
from typing import Dict, Any, List, Callable, Optional
import uuid
from datetime import datetime
from erp.core.errors import DatabaseError

class BaseModel:
    """Base class for all ERP database models."""
    def __init__(self, **kwargs):
        self.id = kwargs.get('id') or str(uuid.uuid4())
        self.created_at = kwargs.get('created_at') or datetime.now()
        self.updated_at = kwargs.get('updated_at') or datetime.now()
        self.status = kwargs.get('status') or 'active'
        self.tenant_id = kwargs.get('tenant_id') or 'tenant_default'
        self.metadata = kwargs.get('metadata') or {}
        
    def to_dict(self) -> Dict[str, Any]:
        result = {}
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                result[k] = v.isoformat()
            else:
                result[k] = v
        return result
        
    def update_timestamp(self):
        self.updated_at = datetime.now()

class Database:
    """In-memory database with transaction logging and rollback capability."""
    def __init__(self):
        self._tables: Dict[str, Dict[str, Any]] = {}
        self._transaction_log: List[tuple] = []
        self._in_transaction: bool = False
        
    def create_table(self, table_name: str):
        if table_name not in self._tables:
            self._tables[table_name] = {}
            
    def insert(self, table_name: str, record_id: str, record: Dict[str, Any]):
        self.create_table(table_name)
        if record_id in self._tables[table_name]:
            raise DatabaseError(f"Record with ID {record_id} already exists in table {table_name}.")
        
        self._tables[table_name][record_id] = record.copy()
        if self._in_transaction:
            self._transaction_log.append(('insert', table_name, record_id, None, record.copy()))
            
    def get(self, table_name: str, record_id: str) -> Optional[Dict[str, Any]]:
        return self._tables.get(table_name, {}).get(record_id)
        
    def update(self, table_name: str, record_id: str, new_record: Dict[str, Any]):
        if table_name not in self._tables or record_id not in self._tables[table_name]:
            raise DatabaseError(f"Record with ID {record_id} not found in table {table_name}.")
            
        old_record = self._tables[table_name][record_id].copy()
        self._tables[table_name][record_id] = new_record.copy()
        
        if self._in_transaction:
            self._transaction_log.append(('update', table_name, record_id, old_record, new_record.copy()))
            
    def delete(self, table_name: str, record_id: str):
        if table_name not in self._tables or record_id not in self._tables[table_name]:
            raise DatabaseError(f"Record with ID {record_id} not found in table {table_name}.")
            
        old_record = self._tables[table_name][record_id].copy()
        del self._tables[table_name][record_id]
        
        if self._in_transaction:
            self._transaction_log.append(('delete', table_name, record_id, old_record, None))
            
    def query(self, table_name: str, filter_func: Optional[Callable[[Dict[str, Any]], bool]] = None) -> List[Dict[str, Any]]:
        self.create_table(table_name)
        records = list(self._tables[table_name].values())
        if filter_func:
            return [r for r in records if filter_func(r)]
        return records
        
    def begin(self):
        self._in_transaction = True
        self._transaction_log = []
        
    def commit(self):
        self._in_transaction = False
        self._transaction_log = []
        
    def rollback(self):
        if not self._in_transaction:
            return
        
        self._in_transaction = False
        for action, table, rid, old, new in reversed(self._transaction_log):
            if action == 'insert':
                if rid in self._tables.get(table, {}):
                    del self._tables[table][rid]
            elif action == 'update':
                self._tables[table][rid] = old
            elif action == 'delete':
                self._tables[table][rid] = old
        self._transaction_log = []
        
db_instance = Database()
