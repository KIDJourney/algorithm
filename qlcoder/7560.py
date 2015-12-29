import requests
import bs4
import time

count = 0
url = "http://movie.douban.com/top250?start={0}&filter="
rating_sum = 0

while count != 166 :
    temp_url = url.format(count)
    soup = bs4.BeautifulSoup(requests.get(temp_url).text)
    tag_value = list(map(lambda x : x.text , soup.find_all('span' , {'class':'rating_num'})))
    print(count)
    print(tag_value)
    print(rating_sum)
    if count + len(tag_value) <= 166 :
        rating_sum += sum(map(float , tag_value))
        count = count + len(tag_value)
    else :
        len_need = 166 - count
        rating_sum += sum(map(float , tag_value[0:len_need]))
        count = count + len_need
    time.sleep(0.5)

print (rating_sum)
