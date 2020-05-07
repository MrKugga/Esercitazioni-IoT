import threading
import random
import requests
import time

class Customer:
    def __init__(self, ID):
        self.ID = ID
        self.timer = random.randrange(1, 10)

class Desk(threading.Thread):
    availableDesks = [1, 2, 3, 4, 5]
    counter = {
        "Desk 1": 0,
        "Desk 2": 0,
        "Desk 3": 0,
        "Desk 4": 0,
        "Desk 5": 0,
    }

    def __init__(self, customer, semaphore):
        threading.Thread.__init__(self)
        self.customer = customer
        self.threadSemaphore = semaphore

    def run(self):
        self.threadSemaphore.acquire()

        desk = Desk.availableDesks.pop()
        Desk.counter[f"Desk {desk}"] += 1
        print(f"Customer {self.customer.ID} at desk {desk}")
        time.sleep(self.customer.timer)
        Desk.availableDesks.append(desk)

        self.threadSemaphore.release()

if __name__ == "__main__":
    n_customers = 30
    customers = []
    for x in range(1, n_customers):
        customers.append(Customer(x))

    threadSemaphore = threading.Semaphore(len(Desk.availableDesks))

    threads = []
    for customer in customers:
        threads.append(Desk(customer, threadSemaphore))

    start = time.time()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    stop = time.time()

    total_time = stop-start
    average_time = total_time/n_customers

    print(f"Total time: {total_time}\nAverage time: {average_time}\nCustomers per desk: {Desk.counter}")
