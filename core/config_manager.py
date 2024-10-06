import toml
import os

BOTS_CONFIG_PATH = 'bots.toml'

class ConfigManager:
    def load_bots(self):
        """
        Memuat konfigurasi bot dari file TOML.
        
        :return: List berisi dictionary informasi bot
        """
        try:
            with open(BOTS_CONFIG_PATH, 'r') as f:
                data = toml.load(f)
            return data.get('bot', [])
        except FileNotFoundError:
            return []

    def save_bots(self, bots):
        """
        Menyimpan konfigurasi bot ke file TOML.
        
        :param bots: List berisi dictionary informasi bot
        """
        with open(BOTS_CONFIG_PATH, 'w') as f:
            toml.dump({'bot': bots}, f)