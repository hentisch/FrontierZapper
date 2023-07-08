import sys
from math import log2

def main():
    zap_archive_path = sys.argv[1]

    with open(zap_archive_path, 'rb') as f:
        header = f.read(4)

        assert header == bytearray([90, 65, 80, 0]), "File does not contain proper ZAP header"    

        block_size = int.from_bytes(f.read(4), byteorder='little')

        assert log2(block_size) == int(log2(block_size)), "Block size should be a power of 2"

        num_entries = int.from_bytes(f.read(4), byteorder='little')

        f.read(4) #Skip currently unknown bytes
        
        working_archive_dir = "/"
        files = []
        count = 0
        while count < num_entries:
            count += 1
            #Loop to read through files and folders
            seperator_bytes = f.read(2) # These are very likely not seperator bytes, though currently they are understood to function as such
            assert seperator_bytes == bytearray([13, 10]), "File sequence doesen't begin with proper seperator sequence 0D 0A"

            num_bytes = int.from_bytes(f.read(2), byteorder="little")

            type_id = int.from_bytes(f.read(2), byteorder='little')

            name_length = int.from_bytes(f.read(2), byteorder='little')
            name_bytes = f.read(name_length-1) # It's possible that the archive uses utf-8 encoding, though I haven't observed any non-ascii characters so far
            f.read(1) # null terminator

            if name_bytes == bytearray([46, 46]):
                working_archive_dir = working_archive_dir[:working_archive_dir[:-1].rfind('/')+1]
                continue

            name = name_bytes.decode('ascii')

            if name[-1] == '/':
                working_archive_dir += name
            else:
                files.append((working_archive_dir + name, num_bytes))

        print("hello world")
if __name__ == "__main__":
    main()