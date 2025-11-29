import json
from typing import List
from src.models import PasswordEntry
from src.crypto import encrypt_value, decrypt_value

class Storage:
  """Handles encrypted JSON storage of password entries."""

  def __init__(self, file_path: str, key: bytes):
    self.file_path = file_path
    self.key = key

  def load_raw(self) -> list:
    """Returns raw list of encrypted dicts from JSON."""
    try:
      with open(self.file_path, "r") as f:
        return json.load(f)
    except FileNotFoundError:
      return []
  
  def save_raw(self, data: list):
    with open(self.file_path, "w") as f:
      json.dump(data, f, indent=4)

  def save_entry(self, entry: PasswordEntry):
    """Encrypts and stores a new entry."""
    encrypted_entry = {
      "site": encrypt_value(entry.site, self.key),
      "username": encrypt_value(entry.username, self.key),
      "password": encrypt_value(entry.password, self.key),
    }
    data = self.load_raw()
    data.append(encrypted_entry)
    self.save_raw(data)

  def load_entries(self) -> List[PasswordEntry]:
    """Loads and decrypts entries into PasswordEntry objects."""
    data = self.load_raw()
    result = []

    for item in data:
      site = decrypt_value(item["site"], self.key)
      username = decrypt_value(item["username"], self.key)
      password = decrypt_value(item["password"], self.key)

      result.append(PasswordEntry(site, username, password))

    return result

  def save_entries(self, entries: list[PasswordEntry]) -> None:
    """Encrypts a full list of entries and writes them to disk."""
    data = [
      {
      "site": encrypt_value(entry.site, self.key),
      "username": encrypt_value(entry.username, self.key),
      "password": encrypt_value(entry.password, self.key)
      }
      for entry in entries
    ]
    self.save_raw(data)