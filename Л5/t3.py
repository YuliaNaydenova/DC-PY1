from random import randint

def get_unique_list_numbers() -> list[int]:
    list=[]
    c=0
    while c!= 15:
        r = randint(-10,10)
        if r not in list:
            list.append(r)
            c+=1
    return list
    ...  # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
