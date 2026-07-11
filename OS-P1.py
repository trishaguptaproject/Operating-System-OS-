from multiprocessing import Process, Semaphore, Lock, Array, Value
import time
import random

# Student Details
NAME = "Trisha"
ROLL_NO = "S086"

BUFFER_SIZE = 5
ITEM_COUNT = 10


# Producer Function
def producer(buffer, in_index, out_index, empty, full, mutex):
    for _ in range(ITEM_COUNT):
        item = random.randint(1, 100)

        empty.acquire()
        mutex.acquire()

        idx = in_index.value
        buffer[idx] = item

        print(f"[{NAME} - {ROLL_NO}] Producer: Produced item {item} at index {idx}", flush=True)

        in_index.value = (idx + 1) % BUFFER_SIZE

        mutex.release()
        full.release()

        time.sleep(random.uniform(0.1, 0.3))


# Consumer Function
def consumer(buffer, in_index, out_index, empty, full, mutex):
    print(f"[{NAME} - {ROLL_NO}] Consumer Process Started", flush=True)

    for _ in range(ITEM_COUNT):
        full.acquire()
        mutex.acquire()

        idx = out_index.value
        item = buffer[idx]

        print(f"[{NAME} - {ROLL_NO}] Consumer: Consumed item {item} from index {idx}", flush=True)

        out_index.value = (idx + 1) % BUFFER_SIZE

        mutex.release()
        empty.release()

        time.sleep(random.uniform(0.1, 0.3))


def main():
    print("=" * 45)
    print(" Producer-Consumer Problem")
    print(f" Name     : {NAME}")
    print(f" Roll No. : {ROLL_NO}")
    print("=" * 45)

    buffer = Array('i', BUFFER_SIZE)
    in_index = Value('i', 0)
    out_index = Value('i', 0)

    empty = Semaphore(BUFFER_SIZE)
    full = Semaphore(0)
    mutex = Lock()

    print("Starting processes...\n")

    p = Process(target=producer,
                args=(buffer, in_index, out_index, empty, full, mutex))

    c = Process(target=consumer,
                args=(buffer, in_index, out_index, empty, full, mutex))

    p.start()
    c.start()

    p.join()
    c.join()

    print(f"\n[{NAME} - {ROLL_NO}] Producer and Consumer processes have finished.")


if __name__ == "__main__":
    main()
