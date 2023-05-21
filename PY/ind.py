#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from multiprocessing import Process, Queue

EPS = 1e-07


def f_sum(x, out):
    n, summa, temp = 1, 1.0, 0
    while abs((summa - temp) > EPS):
        temp = summa
        summa += math.sin(n * x) / n
        n += 1

    out.put(summa)


def check_sum(x, out):
    result = (math.pi - x) / 2
    out.put(result)


if __name__ == '__main__':
    x = x = math.pi / 3
    out1 = Queue()
    out2 = Queue()
    process_1 = Process(target=f_sum, args=(x, out1))
    process_2 = Process(target=check_sum, args=(x, out2))
    process_1.start()
    process_2.start()
    result1 = out1.get()
    result2 = out2.get()
    process_1.join()
    process_2.join()

    print(f"The sum is: {result1}")
    print(f"The check sum is: {result2}")
