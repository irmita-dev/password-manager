from cryptography.fernet import Fernet
import base64
import hashlib

def derive_key(master_password: str) -> bytes:
  """Derives a 32-byte key from the master password."""
  digest = hashlib.sha256(master_password.encode("utf-8")).digest()
  return base64.urlsafe_b64encode(digest)

def encrypt_value(value: str, key: bytes) -> str:
  """Encrypts a string and returns a base64-encoded token as a string."""
  f = Fernet(key)
  token = bytes = f.encrypt(value.encode("utf-8"))
  return token.decode("utf-8")  # Convert bytes to str for storage

def decrypt_value(token_str: str, key: bytes) -> str:
  """Decrypts a token string and returns the original string."""
  f = Fernet(key)
  token: bytes = token_str.encode("utf-8") 
  plain: bytes = f.decrypt(token)
  return plain.decode("utf-8") 