import os
import json
import pylinnworks


from . ftpbackup import FTPBackup
from . channel_lookup import source_lookup, sub_source_lookup
from . exceptions import ChannelNotFound


HOME = os.environ['STCLOCAL']
IMPORT_DIR = os.path.join(HOME, 'import')
DOWNLOAD_DIR = os.path.join(HOME, 'download')
BACKUP_DIR = os.path.join(HOME, 'backup')
EXPORT_DIR = os.path.join(HOME, 'export')
INVENTORY_FILE_NAME = 'linnworks_inventory.csv'
LINKING_FILE_NAME = 'linnworks_linking.csv'
SHOPIFY_PRODUCT_FILE_NAME = "products_export.zip"
SHOPIFY_THEME_FILE_NAME = "www-stcstores-co-uk-stcstores.zip"
LOG_DIR = os.path.join(HOME, 'logs')
directories = [IMPORT_DIR, DOWNLOAD_DIR, EXPORT_DIR, LOG_DIR]

config_path = os.path.join(HOME, 'config.json')
with open(config_path, 'r') as config_file:
    config = json.load(config_file)
BACKUP_DIRS = [BACKUP_DIR] + config['BACKUP_DIRECTORIES']
FTP_BACKUPS = [
    FTPBackup(login['HOST'], login['USER'], login['PASSWD'], login['PATH'])
    for login in config['FTP_BACKUPS']]
pylinnworks.PyLinnworks.connect(config=config['LINNWORKS_LOGIN'])
