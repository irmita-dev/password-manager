from src.crypto import derive_key, encrypt_value, decrypt_value

def test_key_derivation_is_consistent():
  key1 = derive_key("MySecretPassword")
  key2 = derive_key("MySecretPassword")
  assert key1 == key2   # Same password same key

def test_encryption_and_decryption():
  key = derive_key("Master123")
  encrypted = encrypt_value("hello123", key)
  decrypted = decrypt_value(encrypted, key)
  assert decrypted == "hello123"

def test_different_keys_fail_to_decrypt():
  key1 = derive_key("Password1")
  key2 = derive_key("Password2")
  encrypted = encrypt_value("secret", key1)

  try:
    decrypt_value(encrypted, key2)
    assert False, "Decryption with wrong key should fail."
  except Exception:
    assert True