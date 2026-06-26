import logging

logger = logging.getLogger(__name__)

def validate_file(filepath):
    """Validate if file exists"""
    import os
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    return filepath

def read_file(filepath):
    """Read file content"""
    with open(filepath, 'r') as f:
        return f.read()

def write_file(filepath, content):
    """Write content to file"""
    with open(filepath, 'w') as f:
        f.write(content)
    logger.info(f"Written to {filepath}")