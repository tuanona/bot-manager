import tkinter as tk
from ui.app import BotApp

def main():
    """
    Fungsi utama untuk menjalankan aplikasi Bot Manager.
    Inisialisasi root Tkinter dan memulai aplikasi.
    """
    root = tk.Tk()
    app = BotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()