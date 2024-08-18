import re

NAME_REGEX = re.compile(r'^[a-zA-Z0-9_\u00C0-\u00FF]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$')

def validName(name: str) -> bool:
    return NAME_REGEX.match(name) is not None

def validEmail(email: str) -> bool:
    return EMAIL_REGEX.match(email) is not None

def validPassword(password: str) -> bool:
    return PASSWORD_REGEX.match(password) is not None