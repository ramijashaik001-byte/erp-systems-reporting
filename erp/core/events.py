# AuraLedger Core Event Broker
from typing import Dict, Any, List, Callable
from erp.core.logger import audit_log

class EventBroker:
    """Handles decoupled messaging between ERP modules."""
    def __init__(self):
        self._subscribers: Dict[str, List[Callable[[Dict[str, Any]], None]]] = {}
        
    def subscribe(self, event_type: str, callback: Callable[[Dict[str, Any]], None]):
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(callback)
        
    def publish(self, event_type: str, data: Dict[str, Any]):
        audit_log("event_broker", f"Publishing event {event_type} with keys: {list(data.keys())}")
        if event_type in self._subscribers:
            for callback in self._subscribers[event_type]:
                try:
                    callback(data)
                except Exception as e:
                    audit_log("event_broker_error", f"Error firing subscriber for {event_type}: {e}")

event_broker = EventBroker()
