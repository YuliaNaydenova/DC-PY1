money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
flag = True
month = 0  # количество месяцев, которое можно прожить
while flag:
    money_capital -= spend
    if money_capital <= 0:
        flag = False
    else:
        money_capital += salary
        spend = increase * spend + spend
        month += 1
# TODO Оформить решение

print(month)
