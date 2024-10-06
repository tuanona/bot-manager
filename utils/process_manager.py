import subprocess
import os
import time
import psutil

class ProcessManager:
    def __init__(self):
        """
        Inisialisasi ProcessManager.
        """
        self.bot_processes = {}
        self.active_bots = 0

    def run_bot(self, bot_name, bot_url):
        """
        Menjalankan bot sebagai proses terpisah.
        
        :param bot_name: Nama bot
        :param bot_url: URL atau path file bot
        """
        if bot_name not in self.bot_processes:
            try:
                if os.name == 'nt':
                    process = subprocess.Popen(['python', bot_url], creationflags=subprocess.CREATE_NEW_CONSOLE)
                else:
                    process = subprocess.Popen(['python3', bot_url])
                self.bot_processes[bot_name] = process
                self.active_bots += 1
            except Exception as e:
                raise Exception(f"Gagal menjalankan {bot_name}: {str(e)}")

    def stop_bot(self, bot_name):
        """
        Menghentikan bot yang sedang berjalan.
        
        :param bot_name: Nama bot yang akan dihentikan
        """
        if bot_name in self.bot_processes:
            process = self.bot_processes[bot_name]
            try:
                parent = psutil.Process(process.pid)
                for child in parent.children(recursive=True):
                    child.terminate()
                parent.terminate()
                parent.wait(timeout=5)
            except psutil.NoSuchProcess:
                pass  # Proses sudah tidak ada
            except Exception as e:
                raise Exception(f"Gagal menghentikan {bot_name}: {str(e)}")
            finally:
                del self.bot_processes[bot_name]
                self.active_bots -= 1

    def is_bot_running(self, bot_name):
        """
        Memeriksa apakah bot sedang berjalan.
        
        :param bot_name: Nama bot
        :return: Boolean yang menunjukkan status bot
        """
        if bot_name in self.bot_processes:
            process = self.bot_processes[bot_name]
            return process.poll() is None
        return False

    def get_bot_status(self, bot_name):
        """
        Mendapatkan status bot.
        
        :param bot_name: Nama bot
        :return: String yang menunjukkan status bot
        """
        if self.is_bot_running(bot_name):
            last_run = time.strftime("%I:%M %p")
            return f"Active: {last_run}"
        return "Idle"

    def cleanup(self):
        """
        Membersihkan semua proses bot yang masih berjalan.
        """
        for bot_name in list(self.bot_processes.keys()):
            self.stop_bot(bot_name)