import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont  # Tambahkan import ini
from ui.dialogs import AddBotDialog
from core.bot_manager import BotManager
from utils.process_manager import ProcessManager

class BotApp:
    def __init__(self, root):
        """
        Inisialisasi aplikasi Bot Manager.
        
        :param root: Instance Tkinter root
        """
        self.root = root
        self.root.title("Bot Manager v0.1.0 by pidnam")
        self.setup_font()
        
        self.bot_manager = BotManager()
        self.process_manager = ProcessManager()
        
        self.setup_ui()
        
    def setup_font(self):
        """
        Menyiapkan font untuk aplikasi.
        """
        available_fonts = tkfont.families()  # Gunakan tkfont di sini
        if 'Consolas' in available_fonts:
            self.app_font = ('Consolas', 10)
        elif 'Courier' in available_fonts:
            self.app_font = ('Courier', 10)
        else:
            self.app_font = ('TkDefaultFont', 10)
        
        self.root.option_add("*Font", self.app_font)

    def setup_ui(self):
        """
        Menyiapkan elemen-elemen UI utama.
        """
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.active_label = tk.Label(self.frame, text=self.get_active_label(), font=(self.app_font[0], 14))
        self.active_label.grid(row=0, column=0, columnspan=2, pady=5)

        self.add_bot_button = tk.Button(self.frame, text="Add Bot", command=self.show_add_bot_dialog)
        self.add_bot_button.grid(row=0, column=2, pady=5, padx=5)

        self.auto_button = tk.Button(self.frame, text="AUTO", command=self.auto_run_bots, bg="lightblue")
        self.auto_button.grid(row=0, column=3, pady=5, padx=5)

        self.bot_frame = tk.Frame(self.frame)
        self.bot_frame.grid(row=1, column=0, columnspan=4, pady=10)

        self.load_bot_buttons()
    def get_active_label(self):
        """
        Mendapatkan teks label untuk bot aktif.
        
        :return: String berisi informasi bot aktif
        """
        return f"Active: {self.process_manager.active_bots}/{len(self.bot_manager.bots)}"

    def load_bot_buttons(self):
        """
        Memuat tombol-tombol untuk setiap bot yang ada.
        """
        for widget in self.bot_frame.winfo_children():
            widget.destroy()
        
        for idx, bot in enumerate(self.bot_manager.bots):
            btn = tk.Button(self.bot_frame, text=f"{bot['name']}\nIdle", width=15, height=2, 
                            command=lambda b=bot: self.toggle_bot(b))
            btn.grid(row=idx//4, column=idx%4, padx=5, pady=5)

    def show_add_bot_dialog(self):
        """
        Menampilkan dialog untuk menambahkan bot baru.
        """
        dialog = AddBotDialog(self.root)
        if dialog.result:
            self.bot_manager.add_bot(dialog.result['name'], dialog.result['url'])
            self.load_bot_buttons()
            self.update_active_label()

    def toggle_bot(self, bot):
        """
        Mengaktifkan atau menonaktifkan bot.
        
        :param bot: Dictionary berisi informasi bot
        """
        if self.process_manager.is_bot_running(bot['name']):
            self.process_manager.stop_bot(bot['name'])
        else:
            self.process_manager.run_bot(bot['name'], bot['url'])
        self.update_bot_button(bot)
        self.update_active_label()

    def update_bot_button(self, bot):
        """
        Memperbarui tampilan tombol bot.
        
        :param bot: Dictionary berisi informasi bot
        """
        for btn in self.bot_frame.winfo_children():
            if btn['text'].startswith(bot['name']):
                status = self.process_manager.get_bot_status(bot['name'])
                btn.config(text=f"{bot['name']}\n{status}")
                break

    def update_active_label(self):
        """
        Memperbarui label yang menunjukkan jumlah bot aktif.
        """
        self.active_label.config(text=self.get_active_label())

    def auto_run_bots(self):
        """
        Menjalankan semua bot yang tidak aktif atau menghentikan semua bot yang aktif.
        """
        if self.process_manager.active_bots == 0:
            for bot in self.bot_manager.bots:
                if not self.process_manager.is_bot_running(bot['name']):
                    self.process_manager.run_bot(bot['name'], bot['url'])
                    self.update_bot_button(bot)
            self.auto_button.config(text="STOP")
        else:
            for bot in self.bot_manager.bots:
                if self.process_manager.is_bot_running(bot['name']):
                    self.process_manager.stop_bot(bot['name'])
                    self.update_bot_button(bot)
            self.auto_button.config(text="AUTO")
        self.update_active_label()