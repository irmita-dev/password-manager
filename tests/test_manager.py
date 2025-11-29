import pytest
from src.models import PasswordEntry
from src.storage import Storage
from src.crypto import derive_key
from src.manager import PasswordManager

@pytest.fixture
def setup_pm(tmp_path):
  file_path = tmp_path / "pw.json"
  key = derive_key("master123")
  storage = Storage(str(file_path), key)
  pm = PasswordManager(storage)
  return pm

def test_add_entry_creates_encrypted_record(setup_pm):
  pm = setup_pm

  pm.add_entry("gmail.com", "user@gmail.com", "mypw123")

  entries = pm.list_entries()

  assert len(entries) == 1
  assert entries[0].site == "gmail.com"
  assert entries[0].username == "user@gmail.com"
  assert entries[0].password == "mypw123"

def test_search_by_site(setup_pm):
  pm = setup_pm

  pm.add_entry("gmail.com", "a", "1")
  pm.add_entry("facebook.com", "b", "2")
  pm.add_entry("gmx.com", "c", "3")

  result = pm.search("gm")

  assert len(result) == 2
  assert all("gm" in e.site for e in result)

def test_delete_entry(setup_pm):
  pm = setup_pm

  pm.add_entry("gmail.com", "a", "1")
  pm.add_entry("facebook.com", "b", "2")

  pm.delete("gmail.com")

  remaining = pm.list_entries()
  assert len(remaining) == 1
  assert remaining[0].site == "facebook.com"