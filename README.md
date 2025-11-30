<!-- Banner -->
<p align="center">
<img src="https://raw.githubusercontent.com/irmita-dev/password-manager/refs/heads/main/password_manager_irmita_dev.png" width="65%" alt="Irma's GitHub banner password manager">
</p>

<h1 align="center">🔐 Password Manager (Python)</h1>

<p align="center">
  <img src="https://img.shields.io/badge/tests-pytest-brightgreen" alt="Tests">
  <img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python">
</p>

<p align="center">
A secure and fully tested **Password Manager** written in Python.  
Includes **AES-level encryption**, **encrypted JSON storage**, **Clean Architecture**, **TDD**, CLI and GUI (Tkinter).  
Portfolio project demonstrating real-world Python skills.
</p>

<hr/>

<h2 align="center">🚀 Features</h2>

<p align="left">
• Strong AES-based Fernet encryption<br>
• Encrypted JSON vault<br>
• Clean Architecture (crypto → storage → manager → interfaces)<br>
• Full pytest test suite<br>
• CLI interface<br>
• GUI (Tkinter)<br>
• Beginner-friendly, secure, and modular
</p>

<hr/>

<h2 align="center">📁 Project Structure</h2>

<pre><code>password_manager/
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
</code></pre>

<hr/>

<h2 align="center">🧭 Installation</h2>

<pre><code>pip install -r requirements.txt
</code></pre>

<hr/>

<h2 align="center">▶️ Usage</h2>

<p align="center">
<strong>CLI</strong><br><br>
<code>python3 main.py</code>
</p>

<p align="left">
Available actions:<br>
• unlock vault (enter master password)<br>
• add entry<br>
• list entries<br>
• delete entry
</p>

<hr/>

<p align="center">
<strong>GUI</strong><br><br>
<code>python3 gui.py</code>
</p>

<p align="left">
Features:<br>
• Master password unlock<br>
• Entry table (site, username)<br>
• Add entry dialog<br>
• Delete entry dialog<br>
• Auto-refresh
</p>

<hr/>

<h2 align="center">🔐 Security Notes</h2>

<p align="left">
• Uses cryptography.Fernet (AES-based symmetric encryption)<br>
• Vault file is always encrypted<br>
• Master password is never stored<br>
• Never commit plain-text vaults<br>
• Avoid storing passwords in environment variables
</p>

<hr/>

<h2 align="center">🧪 Testing</h2>

<pre><code>python3 -m pytest -q
</code></pre>

<p align="center">
Expected:<br>
✓ All tests pass
</p>

<hr/>

<h2 align="center">✨ Roadmap</h2>

<p align="left">
• Search bar in GUI<br>
• Copy-to-clipboard<br>
• Sorting & filtering<br>
• Export / import (CSV / encrypted)<br>
• Flask/FastAPI web version<br>
• Password generator<br>
• GUI dark mode
</p>

<hr/>

<h2 align="center">👩‍💻 Author</h2>

<p align="left">
Irmita Dev<br>
Python Developer • TDD • Clean Architecture<br>
Always learning & building.
</p>

<hr/>

<h2 align="center">✉️ Contact</h2>

<p align="center">
GitHub: https://github.com/irmita-dev<br>
Email: ljubijankicirma3@gmail.com
</p>
