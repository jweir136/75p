"""
A File reader and writer util that allows you to easily read individual bits and bytes of a file and write individual bits and bytes.
"""
class FILE(object):
    def __init__(self, filepath, create_mode=False):
        self.filepath = filepath

        if create_mode:
            self.file = open(filepath, "wb+")
        else:
            self.file = open(filepath, "rb")

    def bytes(self):
        byte = self.file.read(1)

        while True:
            if not byte:
                break
            else:
                yield byte

            byte = self.file.read(1)

    def close(self):
        self.file.close()

    def __str__(self):
        return "<FILE {}>".format(self.filepath)

if __name__ == "__main__":
    f = FILE("examples/king_james_bible.txt")
    for byte in f.bytes():
        print(byte)