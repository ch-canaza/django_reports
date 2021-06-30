""" store helper functions
"""
import uuid

def generate_code():
    """ generates an unique code to be set in transaction_id
    """
    code = str(uuid.uuid4()).replace('-', '').upper()[:12]
    return code
