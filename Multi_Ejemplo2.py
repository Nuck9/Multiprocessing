#------------------------------------------------
# Colas en Multiprocessing
#------------------------------------------------
from multiprocessing import Queue, Process

# Al cubo
def cube(numbers, queue):
    for i in numbers:
        queue.put(i ** 3)

# Multiplicar por dos
def multiply_by_two(numbers, queue):
    for i in numbers:
        queue.put(i * 2)

# Cola
q = Queue()

numbers = range(1, 5)


p1 = Process(target=cube, args=(numbers, q))
p2 = Process(target=multiply_by_two, args=(numbers, q))


p1.start()
p2.start()


p1.join()
p2.join()


while not q.empty():
    print(q.get())
