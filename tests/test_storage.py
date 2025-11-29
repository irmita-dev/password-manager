import os
from src.storage import Storage
from src.crypto import derive_key
from src.models import PasswordEntry

def test_storage_saves_and_loads_encrypted_data(tmp_path):
  # Arrange
  file_path = tmp_path / "passwords.json"
  key = derive_key("master123")

  storage = Storage(str(file_path), key)

  entry = PasswordEntry("gmail.com", "user123", "mypassword")

  # Act
  storage.save_entry(entry)
  loaded = storage.load_entries()

  # Assert
  assert len(loaded) == 1
  assert loaded[0].site == "gmail.com"
  assert loaded[0].username == "user123"
  assert loaded[0].password == "mypassword"

  # Check file content is NOT plain text (encrypted)
  content = file_path.read_text()
  assert "mypassword" not in content # must never store raw passwords