import psutil
import time
import numpy as np
count = 0
mass = []
while count<100:
        p = psutil.swap_memory()._asdict()
        mass.append(p["used"]//1048576)
        count += 1
        time.sleep(0.1)
print("Данная программа показывает количество используемого подкачки памяти в Мбайтах ")
print("Всего данных:", count)
print("Перцентиль 90%:", np.percentile(mass, 90))