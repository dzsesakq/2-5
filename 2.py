#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def garmonic(*args):
    if args:
        values = [int(arg) for arg in args]

        k = len(values)
        i, summ = 0, 0
        for i in values:
            summ += 1 / i
        garmonica = k / summ
        return garmonica
    else:
        return None


if __name__ == "__main__":
    numbers = input('Аргументы а1, а2, ...аn: ').split()
    print('Среднее гармоническое значение^ ', garmonic(*numbers))
