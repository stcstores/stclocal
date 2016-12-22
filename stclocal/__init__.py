import os
import json


class FTPLogin:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password


HOME = os.environ['STCLOCAL']
IMPORT_DIR = os.path.join(HOME, 'import')
DOWNLOAD_DIR = os.path.join(HOME, 'download')
EXPORT_DIR = os.path.join(HOME, 'export')
INVENTORY_FILE_NAME = 'linnworks_inventory.csv'
LINKING_FILE_NAME = 'linnworks_linking.csv'
SHOPIFY_PRODUCT_FILE_NAME = "products_export.zip"
SHOPIFY_THEME_FILE_NAME = "www-stcstores-co-uk-stcstores.zip"
directories = [IMPORT_DIR, DOWNLOAD_DIR, EXPORT_DIR]

config_path = os.path.join(HOME, 'config.json')
with open(config_path, 'r') as config_file:
    config = json.load(config_file)
BACKUP_DIRS = config['BACKUP_DIRECTORIES']
FTP_BACKUPS = [
    FTPLogin(login['HOST'], login['USER'], login['PASSWD'])
    for login in config['FTP_BACKUPS']]
