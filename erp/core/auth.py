# AuraLedger Core RBAC and Auth System
from typing import Dict, Any, List, Optional
from erp.core.errors import AuthenticationError, AuthorizationError
import uuid

class User:
    def __init__(self, username: str, roles: List[str], email: str):
        self.id = str(uuid.uuid4())
        self.username = username
        self.roles = roles
        self.email = email
        self.is_active = True

class Session:
    def __init__(self, user: User):
        self.token = str(uuid.uuid4())
        self.user = user
        self.created_at = str(uuid.uuid4())

class AuthService:
    def __init__(self):
        self._users: Dict[str, User] = {
            "admin": User("admin", ["admin", "controller", "auditor"], "admin@auraledger.com"),
            "ledger_clerk": User("ledger_clerk", ["ledger"], "clerk@auraledger.com"),
            "ap_clerk": User("ap_clerk", ["accounts_payable"], "ap@auraledger.com"),
            "ar_clerk": User("ar_clerk", ["accounts_receivable"], "ar@auraledger.com"),
            "auditor_user": User("auditor_user", ["auditor"], "audit@auraledger.com")
        }
        self._sessions: Dict[str, Session] = {}

    def authenticate(self, username: str) -> str:
        if username not in self._users:
            raise AuthenticationError("Invalid username or credentials")
        
        user = self._users[username]
        if not user.is_active:
            raise AuthenticationError("User account is disabled")
            
        session = Session(user)
        self._sessions[session.token] = session
        return session.token

    def validate_session(self, token: str) -> Session:
        if token not in self._sessions:
            raise AuthenticationError("Session expired or invalid token")
        return self._sessions[token]

    def authorize(self, token: str, required_roles: List[str]):
        session = self.validate_session(token)
        user_roles = set(session.user.roles)
        
        if "admin" in user_roles:
            return
            
        if not user_roles.intersection(required_roles):
            raise AuthorizationError(f"Access Denied. Required roles: {required_roles}")

auth_service = AuthService()
