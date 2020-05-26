#!/usr/bin/env python3

import matplotlib.pyplot as plt
class Income:
    income = []
    def __init__(self):  
        sum = 0
        for i in range(1,21,1):
            d_sum = (0.1 * pow(1.11, i - 1))
            sum+=d_sum
            self.income.append({ "level" : i, "gold" : sum, "delta" : d_sum})
        sum -= 6
        for i in range(1,21,1):
            d_sum = (0.72 * pow(1.14, i - 1))
            sum+=d_sum
            self.income.append({ "level" : i+20, "gold" : sum, "delta" : d_sum})
        sum -= 60
        for i in range(1,21,1):
            d_sum = (8.82 * pow(1.071, i - 1))
            sum+=d_sum
            self.income.append({ "level" : i+40, "gold" : sum, "delta" : d_sum})
        sum -= 300
        for i in range(1,18,1):
            d_sum = (32.46 * pow(1.065, i - 1))
            sum+=d_sum
            self.income.append({ "level" : i+60, "gold" : sum, "delta" : d_sum})
        sum -= 1000
        for i in range(1,4,1):
            d_sum = (88.90 * pow(2.7, i - 1))
            sum+=d_sum
            self.income.append({ "level" : i+77, "gold" : sum, "delta" : d_sum})

    def print(self):
        print("{:<2}| {:^7} | {}".format("Lvl","Sum","Delta"))
        for i in self.income:
            print("{:<2} | {:^7.2f} | {:.2f}".format(i.get('level'),i.get('gold'),i.get('delta')))

