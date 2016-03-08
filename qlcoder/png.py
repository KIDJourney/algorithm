import binascii
def pngCheck(date):
    pos = 8
    chunks = 1
    while pos < len(data):
        print("\nReading chunks {0} at Pos {1}".format(chunks , pos))

        length = int.from_bytes(data[pos:pos+4] , byteorder='big')
        print("Length " +str(length))
        pos += 4

        chunk_type = data[pos:pos+4]
        print(chunk_type)
        pos += 4

        chunks_data = data[pos:pos+length]
        pos += length

        crc =  int.from_bytes(data[pos:pos+4] , byteorder='big')
        pos += 4

        crc_check = binascii.crc32(chunk_type + chunks_data)

        if crc_check != crc :
            print("Error crc at chunk {0}".format(chunks , pos))

        chunks += 1

if __name__ == "__main__":
    data = open('145682845224096.png' , 'rb').read()
    pngCheck(data)