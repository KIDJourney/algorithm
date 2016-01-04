import requests
from bs4 import BeautifulSoup
from datetime import date
import hashlib

def cul_md5(vote):
    today = date.today()
    orc_code = "%d%.2d%.2dKIDJourney%d" % (today.year , today.month , today.day , vote)
    number = 0
    while True :
        temp = orc_code + str(number)
        if hashlib.md5(temp.encode()).hexdigest()[:6] == '000000' :
            return str(number)
        else :
            number += 1

def post_vote(hash_string):
    url = "http://www.qlcoder.com/train/handsomerank"
    soup = BeautifulSoup(requests.get(url).text)
    token = soup.find('input' , {'type':'hidden'}).get('value')
    post_data = {"_token":token , 
                 'name':'KIDJourney',
                 'checkcode' : hash_string}
    response = requests.get(url , data=post_data)
    print(response.text)

if __name__ == "__main__" :
    for i in range(4,1006):
        post_vote(cul_md5(i))