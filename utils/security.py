from passlib.context import CryptContext

# Specify bcrypt as the hashing algorithm
pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")

def hash_password(password: str) -> str:
    """Hash the password before storing it."""
    return pwd_context.hash(password)

def check_password(hashed_password: str, plain_password: str) -> bool:
    """Check if the provided password matches the hashed password."""
    return pwd_context.verify(plain_password, hashed_password)

def validate_user_data(data):
    """Validate user data for creation and updates."""
    if not data.get('name') or len(data['name']) < 3:
        return False
    if not data.get('email') or '@' not in data['email']:  # Simple email validation
        return False
    return True
