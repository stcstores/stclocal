class ChannelNotFound(Exception):
    def __init__(self, search_string):
        self.message = 'No channel matches {}'.format(search_string)
        super().__init__(self.message)
