# Name: Trisha
# Roll No: S086

from multiprocessing import Process, Queue
import time
import random

# Producer function
def producer(queue):
    for i in range(10):
        item = random.randint(1, 100)

        print(f"[Trisha - S086] Producer trying to add: {item}")

        # Blocks if queue is full (maxsize = 3)
        queue.put(item)

        print(f"[Trisha - S086] Producer added: {item}")

        time.sleep(1)


# Consumer function
def consumer(queue):
    for i in range(10):

        # Blocks if queue is empty
        item = queue.get()

        print(f"[Trisha - S086] Consumer removed: {item}")

        time.sleep(2)


# Main program
if __name__ == "__main__":

    print("==============================")
    print("Producer-Consumer Problem")
    print("Queue Size Limit Example")
    print("Name     : Trisha")
    print("Roll No. : S086")
    print("==============================")

    print("\nQueue size = 3")
    print("Starting processes...\n")

    # Queue with maximum size 3
    q = Queue(maxsize=3)

    # Create producer and consumer processes
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    # Start processes
    p1.start()
    p2.start()

    # Wait for completion
    p1.join()
    p2.join()

    print("\n[Trisha - S086] Producer and Consumer processes have finished.")
