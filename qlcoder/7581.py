import hashlib
import time
string = '20151230KIDJourney%d%d'

with open('checksum.txt' , 'w') as ans:
    for vote in range(1,2000):
        for i in range(200000):
            temp_string = string % (vote , i )
            md5 = hashlib.md5(temp_string.encode()).hexdigest()
            if md5[:6] == '000000':
                ans.write(temp_string)
                break
