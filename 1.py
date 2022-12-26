#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def geom(*args):
    if args:
        count = 1
        k = len(args)
        for i in args:
            count *= i
        count = count ** (1 / k)
        return count
    else:
        return None


if __name__ == "__main__":
    numbers = list(map(int, input('Аргументы а1, а2, ...аn: ').split()))
    print('Среднее геометрическое значение: ', geom(*numbers))
