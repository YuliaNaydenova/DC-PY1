def delete(list_, index=None):
    if index != 0 and not index:
        return list_[:-1]
    # TODO реализовать функцию удаления элемента из списка по индексу]
    return list_[:index] + list_[index+1:]
print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
