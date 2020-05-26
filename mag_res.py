#!/usr/bin/env python3

default_resistance_rating_max = 400
default_enemy_caster_lvl = 80

def calc_resistanse(resistance_rating, caster_lvl):
    return 100 * (( resistance_rating - 5) / (resistance_rating + (caster_lvl * 5 )))

res = []
dmg = []
print("{:<4} | {}".format("Rate","Resistance"))
for i in range(0,411,1):
    res.append(i)
    dmg.append(calc_resistanse(i,default_enemy_caster_lvl))
    print("{:<4} | {:.2f} %".format(i, calc_resistanse(i,default_enemy_caster_lvl)))


