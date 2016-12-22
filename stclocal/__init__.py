import os


class STCLocal:
    HOME = os.environ['STCLOCAL']
    IMPORT_DIR = os.path.join(HOME, 'import')
    DOWNLOAD_DIR = os.path.join(HOME, 'download')
    EXPORT_DIR = os.path.join(HOME, 'export')
    INVENTORY_FILE_NAME = 'linnworks_inventory.csv'
    LINKING_FILE_NAME = 'linnworks_linking.csv'
    SHOPIFY_PRODUCT_FILE_NAME = "products_export.zip"
    SHOPIFY_THEME_FILE_NAME = "www-stcstores-co-uk-stcstores.zip"
    directories = [IMPORT_DIR, DOWNLOAD_DIR, EXPORT_DIR]
