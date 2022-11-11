import pprint

# TODO решить с помощью list comprehension и распечатать его
dict = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(0, 16)]
pprint.pprint(dict)