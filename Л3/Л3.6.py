list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
ind = 0
maxx = 0
for pos, i in enumerate(list_numbers):
    if i > maxx:
        maxx = i
        ind = pos
# TODO Оформить решение
change = list_numbers[-1]
list_numbers[-1]= maxx
list_numbers[ind] = change
print(list_numbers)