from random import sample

def get_random_password(n=8) -> str:
    char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'
    return ''.join(i for i in sample(char, n))
    # TODO написать функцию генерации случайных паролей


print(get_random_password())
