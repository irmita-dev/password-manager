from src.models import PasswordEntry

def test_password_entry_holds_data():
  entry = PasswordEntry(site="github.com", username="irma", password="secret123")

  assert entry.site == "github.com"
  assert entry.username == "irma"
  assert entry.password == "secret123"