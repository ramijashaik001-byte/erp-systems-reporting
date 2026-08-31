# AuraLedger Exception Hierarchy
class ERPException(Exception):
    """Base exception for all AuraLedger errors."""
    pass

class DatabaseError(ERPException):
    """Database constraints or query failures."""
    pass

class ValidationError(ERPException):
    """Entity field constraint violations."""
    pass

class AuthenticationError(ERPException):
    """Sign-in or identity validation failures."""
    pass

class AuthorizationError(ERPException):
    """RBAC permission access denied."""
    pass

class WorkflowError(ERPException):
    """Invalid ERP business state transition errors."""
    pass
