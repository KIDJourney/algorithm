import hashlib
import time
from multiprocessing import Queue , Process

def cul_it(job , ans , name):
    while not job.empty() :
        print("Worker {0} is working !".format(name))
        vote = job.get()
        number = 0
        while True :
            temp = string % (vote , number)

            md5 = hashlib.md5(temp.encode()).hexdigest()

            if md5[:6] == '000000':
                print("Worker "+str(name) + " Get the answer !")
                print(temp)
                ans.put((vote , number))
                break
            else :
                number += 1
    print("No job to do , worker{0} exit".format(name))

def master_job(job , ans , name):
    print("master is working")
    while not ans.full():
        time.sleep(5)
    with open('ans.txt' , 'w') as f:
        ans_list = []
        while not ans.empty() :
            ans_list.append(ans.get())
        f.write(str(ans_list))    
    print("Master record the ans")


if __name__ == "__main__":

    string = '20160101KIDJourney%d%d'

    max_vote = 1005
    process_num = 4

    ans = Queue(max_vote)
    job = Queue()

    master = Process(target=master_job , args=(job , ans , 'master'))

    for i in range(1 , max_vote+1):job.put(i)

    master.start()

    workers = [Process(target=cul_it , args = (job , ans , i)) for i in range(process_num)]
    
    for worker in workers:
        worker.start()

