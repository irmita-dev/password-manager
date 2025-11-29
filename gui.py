# Tkinter GUI for the encrypted Password Manager.

import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

from src.crypto import derive_key
from src.manager import PasswordManager

APP_TITLE = "Password Manager (GUI)"
DATA_FILE = os.path.join(os.path.dirname(__file__), "passwords.json")


def apply_premium_style():
    """Apply premium dark theme with accent colors."""
    style = ttk.Style()
    # Use a base theme that is easy to customize
    style.theme_use("clam")

    bg_dark = "#1e1e1e"
    bg_panel = "#252526"
    fg_text = "#dddddd"
    accent = "#f0c674" # warm gold/beige accent

    # Global defaults
    style.configure(
        ".",
        background=bg_dark,
        foreground=fg_text,
        font=("Segoe UI", 11),
    )

    style.configure("TFrame", background=bg_dark)
    style.configure("TLabel", background=bg_dark, foreground=fg_text)

    # Buttons
    style.configure(
        "TButton",
        padding=6,
        background=accent,
        foreground="#1e1e1e",
        borderwidth=0,
        focusthickness=0,
        font=("Segoe UI", 10, "bold"),
    )
    style.map(
        "TButton",
        background=[("active", "#ddb55c")],
    )

    # Treeview (table)
    style.configure(
        "Treeview",
        background=bg_panel,
        fieldbackground=bg_panel,
        foreground=fg_text,
        rowheight=28,
        borderwidth=0,
    )
    style.configure(
        "Treeview.Heading",
        background=bg_panel,
        foreground=accent,
        font=("Segoe UI", 10, "bold"),
        padding=6,
    )


class App(tk.Tk):
    """Main GUI application."""

    def __init__(self):
        super().__init__()
        apply_premium_style()

        self.title(APP_TITLE)
        self.geometry("760x480")
        self.minsize(640, 400)

        # Domain manager (set after master password)
        self.pm: PasswordManager | None = None

        # Status text
        self.status = tk.StringVar(value="Waiting for master password…")

        # Main containers
        self._build_shell()

        # Ask for master password after window appears
        self.after(100, self._ask_master_password)

    # ──────────────────────────────────────────────────────────────────────────────
    # Shell layout (toolbar + center + status bar)

    def _build_shell(self) -> None:
        # Toolbar (top)
        self.toolbar = ttk.Frame(self, padding=(8, 8))
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        # Center area (will hold either welcome text or vault table)
        self.center = ttk.Frame(self, padding=12)
        self.center.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Status bar (bottom)
        self.status_bar = ttk.Label(
            self,
            textvariable=self.status,
            anchor="w",
            background="#252526",
            foreground="#f0c674",
            padding=8,
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Initial welcome content
        info = ttk.Label(
            self.center,
            text="Welcome! Enter your master password to unlock the vault.",
            justify="center",
            font=("Segoe UI", 12),
        )
        info.pack(expand=True)

    # ──────────────────────────────────────────────────────────────────────────────
    # Master password flow

    def _ask_master_password(self) -> None:
        """Prompt for master password and initialize PasswordManager."""

        password = simpledialog.askstring(
            "Unlock",
            "Enter master password:",
            show="*",
            parent=self,
        )

        if password is None or password.strip() == "":
            # User cancelled or empty → close app
            self.destroy()
            return

        try:
            key = derive_key(password.strip())
            self.pm = PasswordManager(DATA_FILE, key)

            # Smoke test: ensure key is compatible with existing data (if any)
            _ = self.pm.list_entries()

            self.status.set("Vault unlocked.")
            self._on_unlocked()
        except Exception as exc:
            messagebox.showerror("Unlock failed", f"Could not unlock vault:\n{exc}")
            # Try again
            self.after(50, self._ask_master_password)

    # ──────────────────────────────────────────────────────────────────────────────
    # After unlock: build vault UI (table + actions)

    def _on_unlocked(self) -> None:
        """Called once manager is ready. Builds the vault UI."""

        assert self.pm is not None

        # Clear center content
        for child in self.center.winfo_children():
            child.destroy()

        # Rebuild toolbar for unlocked state
        for child in self.toolbar.winfo_children():
            child.destroy()

        ttk.Button(self.toolbar, text="Add entry", command=self._open_add_dialog).pack(
            side=tk.LEFT, padx=(0, 8)
        )
        ttk.Button(
            self.toolbar, text="Delete entry", command=self._open_delete_dialog
        ).pack(side=tk.LEFT, padx=(0, 8))
        ttk.Button(self.toolbar, text="Refresh", command=self._refresh_vault).pack(
            side=tk.LEFT
        )

        # Table
        columns = ("site", "username", "password")
        self.table = ttk.Treeview(
            self.center,
            columns=columns,
            show="headings",
            selectmode="browse",
        )

        self.table.heading("site", text="Site")
        self.table.heading("username", text="Username")
        self.table.heading("password", text="Password")

        self.table.column("site", width=220, anchor="w")
        self.table.column("username", width=180, anchor="w")
        self.table.column("password", width=200, anchor="w")

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            self.center, orient=tk.VERTICAL, command=self.table.yview
        )
        self.table.configure(yscrollcommand=scrollbar.set)

        self.table.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True,
            padx=12,
            pady=12,
        )
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=12)

        self._refresh_vault()

    def _refresh_vault(self) -> None:
        """Reload data from manager into the table."""

        assert self.pm is not None

        for row in self.table.get_children():
            self.table.delete(row)

        entries = self.pm.list_entries()

        for entry in entries:
            # For portfolio screenshots you can leave real password,
            # otherwise mask it like "********".
            self.table.insert(
                "",
                tk.END,
                values=(entry.site, entry.username, entry.password),
            )

        self.status.set(f"Loaded {len(entries)} entr{'y' if len(entries) == 1 else 'ies'}.")

    # ──────────────────────────────────────────────────────────────────────────────
    # Dialogs

    def _open_add_dialog(self) -> None:
        """Dialog for adding a new entry."""
        assert self.pm is not None

        win = tk.Toplevel(self)
        win.title("Add entry")
        win.geometry("320x220")
        win.resizable(False, False)
        win.transient(self)
        win.grab_set()

        ttk.Label(win, text="Site:").pack(pady=(12, 0))
        site_entry = ttk.Entry(win, width=30)
        site_entry.pack()

        ttk.Label(win, text="Username:").pack(pady=(8, 0))
        user_entry = ttk.Entry(win, width=30)
        user_entry.pack()

        ttk.Label(win, text="Password:").pack(pady=(8, 0))
        pwd_entry = ttk.Entry(win, width=30, show="*")
        pwd_entry.pack()

        def on_save() -> None:
            site = site_entry.get().strip()
            user = user_entry.get().strip()
            pwd = pwd_entry.get().strip()

            if not site or not user or not pwd:
                messagebox.showerror("Error", "All fields are required.", parent=win)
                return

            self.pm.add_entry(site, user, pwd)
            self._refresh_vault()
            win.destroy()

        ttk.Button(win, text="Save", command=on_save).pack(pady=12)

    def _open_delete_dialog(self) -> None:
        """Dialog for deleting an entry by site name."""
        assert self.pm is not None

        win = tk.Toplevel(self)
        win.title("Delete entry")
        win.geometry("280x150")
        win.resizable(False, False)
        win.transient(self)
        win.grab_set()

        ttk.Label(win, text="Site to delete:").pack(pady=(10, 0))
        site_entry = ttk.Entry(win, width=30)
        site_entry.pack()

        def on_delete() -> None:
            site = site_entry.get().strip()
            if not site:
                messagebox.showerror("Error", "Please enter a site.", parent=win)
                return

            self.pm.delete_entry(site)
            self._refresh_vault()
            win.destroy()

        ttk.Button(win, text="Delete", command=on_delete).pack(pady=12)


def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()