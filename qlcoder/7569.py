import requests
import bs4
import time
import itertools
urls = ['http://www.qlcoder.com/train/spider3/5',
 'http://www.qlcoder.com/train/spider3/3',
 'http://www.qlcoder.com/train/spider3/4',
 'http://www.qlcoder.com/train/spider3/8',
 'http://www.qlcoder.com/train/spider3/7']


avg_time = {}

# for index , url in enumerate(urls):
    
#     print('processing %d url' % index)
#     print("Url:" + url + '\n')

#     content = [requests.get(url).text , time.time()]
    
#     avg = 0
#     tried_time = 0
#     request_time = 0

#     while tried_time < 3:
#         temp = [requests.get(url).text , time.time()]
    
#         if temp[0] != content[0]:
#             time_after = temp[1] - content[1]
#             print("Content changed , time spend : %lf" % time_after)
#             avg = (avg * tried_time + time_after)/(tried_time+1)
#             content = temp
#             tried_time += 1
#             requests_time = 0
#         else :
#             print("Requests success , content not change")

#         request_time += 1
#         time.sleep(5)
#         if request_time >= 60:
#             request_time = 0
#             avg = "Very Long"
#             break 
    
#     print('url :{0}  time:{1} \n'.format(url , avg))
#     avg_time[url] = avg

# with open("avg.txt" , 'w+') as f:
#     f.write(str(avg_time))

def get_ans():
    right = list(map(int ,('1 2 10 9 6 5'.split())))
    left = list(map(int , ("3 4 7 8".split())))
    for i in itertools.permutations(left , len(left)):
        temp_list = right[:]
        temp_list.extend(i) 
        ans = '-'.join(map(str , temp_list))
        yield ans

def get_token(content):
    soup = bs4.BeautifulSoup(content)
    soup = soup.find('input',{'type':'hidden'})
    return soup.get('value')

def submit_ans(session , token , ans):
    post_url = "http://www.qlcoder.com/task/26/solve"
    data = {'_token':token , 
            'answer' : ans}
    response = session.post(post_url , data=data)
    return response.text

if __name__ == "__main__":
    url = "http://www.qlcoder.com/task/7569"
    
    session = requests.Session()
    cookie = {'laravel_session':"eyJpdiI6InVVc3BCRGU1akpwaG1FbGMyQ1cxOHc9PSIsInZhbHVlIjoiXC9cL2h6UmxmQUVCRmRCUDBsb09yQXlobzJCMXNyVkY2Z3dDRk5NeWdiRzRSWE1cLzRaMUNCanBEam11Q2Q1eEJIa3BjSVhmMVc4THpIRDBUK0Q5YVJ0UGc9PSIsIm1hYyI6ImMyZGRkMmJhNzExODA4ZDBmM2RjMmE0NzA0MDQ5MjNhZmRiNjQ1OWZiNjFjYTY4YmQ5Y2E0ZmJmOTMwNjZkYjUifQ%3D%3D"}

    for ans in get_ans():
        response = session.get(url , cookies = cookie).text
        token = get_token(response)        
        print(submit_ans(session , token , ans))
        time.sleep(1)