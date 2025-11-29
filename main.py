from pathlib import Path
from getpass import getpass

from src.crypto import derive_key
from src.storage import Storage
from src.manager import PasswordManager
from cryptography.fernet import InvalidToken

DATA_FILE = Path("passwords.json")


def create_manager(master_password: str) -> PasswordManager:
    """Create a PasswordManager configured with derived key and storage."""
    key = derive_key(master_password)
    storage = Storage(str(DATA_FILE), key) # only file_path + key
    return PasswordManager(storage)


def main() -> None:
    print("Password Manager")
    master = getpass("Enter master password: ")

    try:
        manager = create_manager(master)
        run_cli(manager)
    except InvalidToken:
        print("\n[ERROR] Invalid master password or corrupted data file.")
        return


def run_cli(manager: PasswordManager) -> None:
    """Simple CLI loop for interacting with the password manager."""
    while True:
        print("\nOptions:")
        print("1) List entries")
        print("2) Add entry")
        print("3) Delete entry")
        print("4) Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            entries = manager.list_entries()
            if not entries:
                print("No entries stored yet.")
            else:
                for e in entries:
                    print(f"- {e.site}: {e.username} / {e.password}")

        elif choice == "2":
            site = input("Site: ").strip()
            username = input("Username: ").strip()
            password = getpass("Password: ")
            manager.add_entry(site, username, password)
            print("Entry added.")

        elif choice == "3":
            site = input("Site to delete: ").strip()
            manager.delete_entry(site)
            print("Entry deleted (if it existed).")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()