#-------------------------------------------------------
# Serial y Paralelo
#-------------------------------------------------------

import multiprocessing
import time

# cuadrados con retardo
def suma_cuadrados(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
        time.sleep(0.05)
    print(f"Suma de cuadrados hasta {n} completada")

# Ejecución serial
start = time.time()
suma_cuadrados(50)
suma_cuadrados(50)
suma_cuadrados(50)
suma_cuadrados(50)
print("Tiempo de ejecución serial:", time.time() - start)

# Ejecución paralela
start = time.time()
p1 = multiprocessing.Process(target=suma_cuadrados, args=(50,))
p2 = multiprocessing.Process(target=suma_cuadrados, args=(50,))
p3 = multiprocessing.Process(target=suma_cuadrados, args=(50,))
p4 = multiprocessing.Process(target=suma_cuadrados, args=(50,))


p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()

print("Tiempo de ejecución paralela:", time.time() - start)
