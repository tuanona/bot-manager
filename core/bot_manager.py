from core.config_manager import ConfigManager

class BotManager:
    def __init__(self):
        """
        Inisialisasi BotManager.
        """
        self.config_manager = ConfigManager()
        self.bots = self.config_manager.load_bots()

    def add_bot(self, name, url):
        """
        Menambahkan bot baru ke daftar dan menyimpannya.
        
        :param name: Nama bot
        :param url: URL atau path file bot
        """
        new_bot = {"name": name, "url": url}
        self.bots.append(new_bot)
        self.config_manager.save_bots(self.bots)

    def remove_bot(self, name):
        """
        Menghapus bot dari daftar.
        
        :param name: Nama bot yang akan dihapus
        """
        self.bots = [bot for bot in self.bots if bot['name'] != name]
        self.config_manager.save_bots(self.bots)

    def get_bot(self, name):
        """
        Mendapatkan informasi bot berdasarkan nama.
        
        :param name: Nama bot
        :return: Dictionary berisi informasi bot atau None jika tidak ditemukan
        """
        for bot in self.bots:
            if bot['name'] == name:
                return bot
        return None