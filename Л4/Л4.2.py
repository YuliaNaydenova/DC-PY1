def get_count_char(str_):
    dict_ = {}
    str_ = str_.lower()
    a = str_.split()
    for word in a:
        for i in word:
            if i.isalpha():
                if i in dict_:
                    dict_[i] += 1
                else:
                    dict_[i] = 1
    return dict_
    # TODO посчитать количество каждой буквы в строке в аргументе str_

def get_percent_char(dict_):
    count_ = 0
    dict_p = {}
    for value in dict_.values():
        count_ += value
    for key in dict_.keys():
        dict_p[key] = str(round((dict_[key]/count_) * 100, 2)) + '%'
    return dict_p

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
