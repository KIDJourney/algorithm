# coding: utf-8
import struct
data = open('rf.data','rb').read()
post = 0
post = 0
pos = 0
filename = 0
while data[pos] != 2:
    filesize = struct.unpack('>i',data[pos+1:pos+1+4])
    filedata = data[pos+5:pos+5+filesize]
    pos = pos + 5 + filesize
    with open(str(filename) ,'wb') as f:
        f.write(filedata)
        
while data[pos] != 2:
    filesize = struct.unpack('>i',data[pos+1:pos+1+4])[0]
    filedata = data[pos+5:pos+5+filesize]
    pos = pos + 5 + filesize
    with open(str(filename) ,'wb') as f:
        f.write(filedata)
        
while data[pos] != 2:
    filesize = struct.unpack('>i',data[pos+1:pos+1+4])[0]
    filedata = data[pos+5:pos+5+filesize]
    pos = pos + 5 + filesize
    with open(str(filename) ,'wb') as f:
        f.write(filedata)
    filename += 1
    
pos = 0
while data[pos] != 2:
    filesize = struct.unpack('>i',data[pos+1:pos+1+4])[0]
    filedata = data[pos+5:pos+5+filesize]
    pos = pos + 5 + filesize
    with open(str(filename) ,'wb') as f:
        f.write(filedata)
    filename += 1
    
