# AuraLedger Structured System Logger
import os
from datetime import datetime

def audit_log(subsystem: str, message: str, level: str = "INFO"):
    log_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_path = os.path.join(log_dir, 'auraledger_audit.log')
    
    timestamp = datetime.now().isoformat()
    formatted_message = f"[{timestamp}] [{level}] [{subsystem}] {message}\n"
    
    try:
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(formatted_message)
    except IOError:
        pass
