import tkinter as tk
from tkinter import filedialog

class AddBotDialog(tk.Toplevel):
    def __init__(self, parent):
        """
        Inisialisasi dialog untuk menambahkan bot baru.
        
        :param parent: Widget induk Tkinter
        """
        super().__init__(parent)
        self.title("Add New Bot")
        self.result = None
        self.setup_ui()

    def setup_ui(self):
        """
        Menyiapkan elemen-elemen UI untuk dialog.
        """
        self.name_label = tk.Label(self, text="Bot Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.url_label = tk.Label(self, text="Bot URL:")
        self.url_label.grid(row=1, column=0, padx=5, pady=5)
        self.url_entry = tk.Entry(self, width=30)
        self.url_entry.grid(row=1, column=1, padx=5, pady=5)
        self.browse_button = tk.Button(self, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=1, column=2, padx=5, pady=5)

        self.ok_button = tk.Button(self, text="OK", command=self.on_ok)
        self.ok_button.grid(row=2, column=0, columnspan=3, pady=10)

        self.protocol("WM_DELETE_WINDOW", self.on_cancel)
        self.transient(self.master)
        self.grab_set()
        self.master.wait_window(self)

    def browse_file(self):
        """
        Membuka dialog untuk memilih file bot.
        """
        filename = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if filename:
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, filename)

    def on_ok(self):
        """
        Menangani aksi ketika tombol OK ditekan.
        """
        name = self.name_entry.get().strip()
        url = self.url_entry.get().strip()
        if name and url:
            self.result = {"name": name, "url": url}
            self.destroy()
        else:
            tk.messagebox.showerror("Error", "Nama bot dan URL harus diisi!")

    def on_cancel(self):
        """
        Menangani aksi ketika dialog ditutup.
        """
        self.result = None
        self.destroy()