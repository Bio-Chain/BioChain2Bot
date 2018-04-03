class FileString:
    def __init__(self, filename):
        self.filename = filename
        self.data = ''

    def update(self):
        try:
            with open(self.filename) as f:
                self.data = f.read()
        except:
            pass

    def set(self, data):
        self.data = str(data)
        with open(self.filename, 'w') as f:
            f.write(data)

    def append(self, data):
        self.data = str(data)
        with open(self.filename, 'a') as f:
            f.write(data)

    def get(self):
        self.update()
        return self.data

    def __str__(self):
        self.update()
        return self.data
