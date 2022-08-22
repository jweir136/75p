import math

"""
A File reader and writer util that allows you to easily read individual bits and bytes of a file and write individual bits and bytes.
"""
class FILE(object):
    def __init__(self, filepath, create_mode=False):
        self.filepath = filepath
        self.create_mode = create_mode
        self.read_bits_buffer = ""
        self.write_bits_buffer = ""

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
                yield ord(byte)

            byte = self.file.read(1)

    def write_bit(self, bit):
        if not self.create_mode:
            raise Exception("Error: Can't write to file not in CREATE_MODE")
        
        if len(self.write_bits_buffer) < 8:
            self.write_bits_buffer += bit
        if len(self.write_bits_buffer) == 8:
            self.file.write(bytes([int(self.write_bits_buffer, base=2)]))
            self.write_bits_buffer = ""

    def close(self):
        if self.create_mode and len(self.write_bits_buffer):
            raise Exception("Error: {} bits still left in buffer".format(len(self.write_bits_buffer)))

        self.file.close()

    def __str__(self):
        return "<FILE {}>".format(self.filepath)

if __name__ == "__main__":
    f = FILE("examples/king_james_bible2.txt", True)
    for _ in range(8):
        f.write_bit('1')
    f.close()
    