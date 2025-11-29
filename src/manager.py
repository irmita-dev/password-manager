from typing import List
from src.models import PasswordEntry
from src.storage import Storage


class PasswordManager:
  """
  High-level facade used by CLI and GUI.
  """

  def __init__(self, file_path: str, key: bytes):
    #create storage instance
    self.storage = Storage(file_path, key)

  def add_entry(self, site: str, username: str, password: str) -> None:
    entry = PasswordEntry(site, username, password)
    self.storage.save_entry(entry)

  def list_entries(self) -> List[PasswordEntry]:
    return self.storage.load_entries()

  def delete_entry(self, site: str) -> None:
    self.storage.delete_entry(site)