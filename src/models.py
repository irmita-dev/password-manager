from dataclasses import dataclass

@dataclass
class PasswordEntry:
  """ Represents a single password entry stored in the password manager. """

  site: str
  username: str
  password: str
  