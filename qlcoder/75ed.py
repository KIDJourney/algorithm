def f(keys, text):
    bytes = [ord(c) for c in text]
    result_str = ""
    for i in range(0, len(bytes), 3):
        temp = 0
        for j in range(3):
            temp <<= 8
            temp += bytes[i + j]
        for j in range(3):
            print('ori:\t %+34s' % bin(temp))
            temp ^= (keys[temp & 3] << 8)
            print('xor:\t %+34s' % bin(temp))
            temp = (temp << 7) | (temp >> 17)
            print('or:\t\t %+34s' % bin(temp))
            temp &= ((1 << 24) - 1)
            print('res:\t %+34s' % bin(temp))
        result_str += hex(temp)[2:]
    return result_str

def decode(keys , text):
    result = ''
    for i in range(0 , len(text) , 6):
        code = text[i:i+6]
        print(code)
        code = (int(code , 16))

        print(bin(code))

        for t in range(3):
            # code = code[-7:] + code[:-7]

            code = (code >> 7) | (code << 17)

            code &= ((1<<24)-1)

            key = keys[code&3]

            # code = bin(int(code ,2) ^ (key << 8))

            code = code ^ (key<<8)
            print('tans:\t'+bin(code))

        code = bin(code)[2:]

        code = '0'*(24-len(code))+code

        ans = [chr(int(code[x*8:x*8+8] , 2))for x in range(3)]

        result += ''.join(ans)

    return result

if __name__ == "__main__":
    keys = [123,232,1,23]
    words = 'aon'
    code = f(keys , words)
    print(code)
    print(decode(keys , code))

    # code = """bb2af286e3ec8ead77cf81d0e7299fef8fd0a3837a4621fef3827dd0887c51aa168b4f0953aa3f070dfffc2cb0df8afdbdacbddce28165efe57ceac945cde63c28d23ce6e927a9f2624b4f8683fa51e8683da6fdaba13a2b055d0b2f7e0583f299081139027275089311cc6b112a124f85d3070dff6b237d53aa1f51805ed3aa3efd66e4dce2eb50ea29870dfffe26f4e66988116041b12073dda2f71d2292e381305ce28baf8dd3c643e1f92c90b1a45f1c86d6190e700ba932838d7794205669c54591205329eb468683fac9095e85c3cc51e868d1a05e6a4b4b8683fabb2af286e3ece9e546d02e504f85d36b0b5f6aa532bdacbde38530dce2e1130a12254fc8e9213751e868eb2137b1406ca72dff4601ff4aaf32a3837ad38a1f71827d7024139d22da5f64c56769c962215e0bab721340447c88fe5da29dd8805e6a412b6b237f590e33d16c464aaf327904132f89f0fc8adea589d2e8a550f50ed2250fdedcca814d095f990a334643a8ddaafdd0887ceb21175ca2bfd1a05ea9eb46d0887cc723d7bd28b2caaf30bf86ffdce2eb7faadfff46e45ce28b1f42a54603ff750eb305079658c2ab2ba313072dff6b237d53aa1f7f66e5d1c04fbfaeded1a05ab4267a152a12ea4361caaf324601ff6b2b5d8683fa1ca4dea6a9f2a60fdd690b5fd1aa3e5de280af89d28be925c643a1c5c5c6e729dcd90c50c723d73c2ad2ea21371d22923508923d2ad0d34e46620b5d8683fa71a05d8b2f3d3c2a92190830536c659ca4dc91281370827d7e26f3eb4b4bd0887ceb211705e3e61f84deeb6121d36c4490005245ede406a3f33d86fe074deb502e50620b5d71a05d53aa1f3508d2d3887ed0805fc643c167299ff0a0775ca2bf5da2d64f85d3d1805ffd8a9f50c82951805e7cea892a255e050dff6b237d53aa1fff66e6e9233ef50ed023813045c5c4b1ac5edfa2fd4aaf324f85d3870dfdbcee887daad63c4ae55f04d3e7618fbfaeded1a05ab4267a152a12ea4361aaa13abd2a92a6a9d227c9c4790413a3837a7ccae8ebc5467904122381536ba77250ea08936044c643c1716405d3887eea41216a237d53aa1f750e937ccac92a47608f85d33da6ff27a9f2b50ab2a9eb4586a3b3f08077930a12102a32870dffc4adf0fdaa9e7daabfa9c12c256fe80e0dffea610149095f438f5385e1ccc585d0df8ad7918e5d916a0507c3e48f81d33da6ff27a9f2a589d292205245ede4dfa2971d22926385533deec94aaf3258c04ca7a991af89d306e3e48f81d3bda6ffe5cfc67f06f2a9c366e68fd2936044c643c18b4f09e92137dce2814621fef3827dd0887c0727b649095f4f85d33f6aa4934045ff66e331426650ea4929c366702413604bce"""
    # for x in range(256):
    #     for y in range(256):
    #         for z in range(256):
    #             for zz in range(256):
    #                 keys = [x,y,z,zz]
    #                 ans = decode(keys , code)
    #                 if "answer" in ans.lower() :
    #                     print(ans)
    #                     break

    