#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В магазине комиксов "МАРВЕЛ" на каждый товар стоимостью от 140 рублей скидка 50%,
# а на комиксы по Мстителям скидка 20%.
# Напишите программу, которая подсчитает итоговый чек.
def magaz(**candies):
    summ = 0
    for candies, cost in candies.items():
        summ += cost
        if candies == "Мстители":
            cost = (cost / 100) * 80
        if cost > 140:
            cost /= 2
        print(f"{candies}: {cost}")

    print(f"Итоговая стоимость: {summ}")


if __name__ == "__main__":
    magaz(Мстители=100, Халк=200,
          Человек_паук=150, Железный_человек=130,
          Черная_пантера=150, Капитан_америка=100)
