from . exceptions import ChannelNotFound

class LookUp:

    def __init__(self, name, matches):
        self.name = name
        self.matches = [string.lower() for string in matches]
        self.matches.append(self.name.lower())

    def check_match(self, string):
        if string.lower() in self.matches:
            return True
        return False


def source_lookup(string):
    sources = [
        LookUp('EBAY', ['ebay']),
        LookUp('AMAZON', ['amazon']),
        LookUp('SHOPIFY', ['shopify'])
    ]
    for source in sources:
        if source.check_match(string):
            return source.name
    raise ChannelNotFound(string)


def sub_source_lookup(string):
    sub_sources = [
        LookUp('EBAY0', (
            'ebay', 'ebay uk', 'ebayuk', 'ebay.co.uk', 'ebay.com')),
        LookUp('Stc Stores', (
            'amazon uk', 'amazonuk', 'amazon', 'amazon.co.uk')),
        LookUp('STC Stores France', (
            'amazon france', 'amazon.fr', 'amazon fr')),
        LookUp('STC Stores Germany', (
            'amazon.de', 'amazon germany', 'amazon de')),
        LookUp('STC Stores Italy', (
            'amazon.it', 'amazon italy', 'amazon it')),
        LookUp('STC Stores Spain', (
            'amazon.es', 'amazon spain', 'amazon es')),
        LookUp('STC Stores USA', (
            'amazon.com', 'amazon usa', 'amazon america', 'amazon.com',
            'amazon us')),
        LookUp('STC Stores Canada', (
            'amazon.ca', 'amazon canada', 'amazon ca')),
        LookUp('STC Stores Mexico', (
            'amazon.com.mx', 'amazon mexico', 'amazon mx')),
        LookUp('STC Stores Japan', (
            'amazon.co.jp', 'amazon japan', 'amazon jp')),
    ]
    for sub_source in sub_sources:
        if sub_source.check_match(string):
            return sub_source.name
    raise ChannelNotFound(string)
