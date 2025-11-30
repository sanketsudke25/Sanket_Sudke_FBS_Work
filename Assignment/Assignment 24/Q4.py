import threading
import queue
import time
import random

buffer = queue.Queue(maxsize=5)
def producer(name):
    for i in range(5):  
        item = f"{name}_item{i}"
        buffer.put(item)  
        print(f" Producer {name} produced: {item}")
        time.sleep(random.uniform(0.2, 0.6))  

def consumer(name):
    for i in range(5):  
        item = buffer.get()  
        print(f"Consumer {name} consumed: {item}")
        buffer.task_done()
        time.sleep(random.uniform(0.3, 0.7)) 
def main():
  
    producers = [threading.Thread(target=producer, args=(f"P{i+1}",)) for i in range(2)]
    consumers = [threading.Thread(target=consumer, args=(f"C{i+1}",)) for i in range(2)]
    for t in producers + consumers:
        t.start()
    for t in producers + consumers:
        t.join()

    print(" All producers and consumers finished.")

if __name__ == "__main__":
    main()