# Name: Trisha
# Roll No: S086

from multiprocessing import Process, Queue
import time
import random

# Producer function
def producer(queue):
    for i in range(5):
        item = random.randint(1, 100)
        print(f"[Trisha - S086] Producer: Produced item {item} at index {i}")
        queue.put((item, i))
        time.sleep(random.random())

# Consumer function
def consumer(queue):
    for i in range(5):
        item, index = queue.get()
        print(f"[Trisha - S086] Consumer: Consumed item {item} from index {index}")
        time.sleep(random.random())

# Main program
if __name__ == "__main__":

    print("==============================")
    print("Producer-Consumer Problem")
    print("Name     : Trisha")
    print("Roll No. : S086")
    print("==============================")

    print("\nStarting processes...\n")

    q = Queue()

    # Create processes
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    # Start processes
    p1.start()
    p2.start()

    # Wait for completion
    p1.join()
    p2.join()

    print("\n[Trisha - S086] Producer and Consumer processes have finished.")
