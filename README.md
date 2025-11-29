<h1 align="center">🔐 Password Manager (Python)</h1>

<p align="center">
  <img src="https://img.shields.io/badge/tests-pytest-brightgreen" alt="Tests">
  <img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python">
</p>

A secure and fully tested **Password Manager** written in Python.  
Includes **AES-level encryption**, **encrypted JSON storage**, **Clean Architecture**, **TDD**, CLI and GUI (Tkinter).  
Portfolio project demonstrating real-world Python skills.

---

## 🚀 Features

• Strong AES-based Fernet encryption
• Encrypted JSON vault
• Clean Architecture (crypto → storage → manager → interfaces)
• Full pytest test suite
• CLI interface
• GUI (Tkinter)
• Beginner-friendly, secure, and modular


---

📁 Project Structure

password_manager/
│
├── src/
│ ├── crypto.py # Encryption / decryption
│ ├── models.py # PasswordEntry dataclass
│ ├── storage.py # Encrypted JSON read/write
│ ├── manager.py # Business logic
│
├── tests/
│ ├── test_crypto.py
│ ├── test_storage.py
│ ├── test_manager.py
│ ├── test_model.py
│
├── main.py # CLI
├── gui.py # Tkinter GUI
├── passwords.json # Encrypted vault (auto-created)
├── requirements.txt
└── README.md


---

🧭 Installation

pip install -r requirements.txt


---

▶️ Usage

CLI

python3 main.py

Available actions:
• unlock vault (enter master password)
• add entry
• list entries
• delete entry


---

GUI

python3 gui.py

Features:
• Master password unlock
• Entry table (site, username)
• Add entry dialog
• Delete entry dialog
• Auto-refresh


---

🔐 Security Notes

• Uses cryptography.Fernet (AES-based symmetric encryption)
• Vault file is always encrypted
• Master password is never stored
• Never commit plain-text vaults
• Avoid storing passwords in environment variables


---

🧪 Testing

python3 -m pytest -q

Expected:
✓ All tests pass


---

✨ Roadmap

• Search bar in GUI
• Copy-to-clipboard
• Sorting & filtering
• Export / import (CSV / encrypted)
• Flask/FastAPI web version
• Password generator
• GUI dark mode


---

👩‍💻 Author

Irmita Dev
Python Developer • TDD • Clean Architecture
Always learning & building.


---

✉️ Contact

GitHub: https://github.com/irmita-dev
Email: ljubijankicirma3@gmail.com
