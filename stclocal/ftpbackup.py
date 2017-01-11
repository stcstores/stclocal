class FTPBackup:
    def __init__(self, host, user, password, path):
        self.host = host
        self.user = user
        self.password = password
        self.path = path

    def __repr__(self):
        return ''.join([self.user, '@', self.host, '/', self.path])
