from threading import Thread
import time
import requests

class MyThread(Thread):

    def __init__(self, threadID, website):
        Thread.__init__(self)
        self.threadID = threadID
        self.website = website

    def run(self):
        r = requests.get(self.website)




websites = ["http://yahoo.com", "http://google.com", "http://amazon.com", "http://ibm.com", "http://apple.com", "https://www.microsoft.com", "https://www.youtube.com/" , "https://www.polito.it/" , "http://www.wikipedia.org", "https://www.reddit.com/", "https://www.adobe.com/", "https://wordpress.org/", "https://github.com/", "https://www.google.com/maps/"]

if __name__ == "__main__"
    start = time.time()
    for website in websites:
        r = requests.get(website)
    stop = time.time()

    execution_time = stop-start
    print(f'Ciclo for: {execution_time} s')

    start = time.time()
    threads = []
    for threadID, website in enumerate(websites):
        threads.append(MyThread(threadID, website))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    stop = time.time()

    execution_time = stop-start
    print(f'Threading: {execution_time} s')
