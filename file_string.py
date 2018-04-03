class FileString:
    def __init__(self, filename):
        self.filename = filename

    def set(self, data):
        with open(self.filename, 'w') as f:
            f.write(data)

    def append(self, data):
        with open(self.filename, 'a') as f:
            f.write(data)

    def get(self):
        with open(self.filename) as f:
                return f.read()
    
    def getLines(self):
        with open(self.filename) as f:
            lines = []
            for line in f:
                lines.append(line)
            return lines

    def __str__(self):
        self.update()
        return self.data
