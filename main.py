def same_type(func):
    def amount_pos_args(*args):
        var_args = set(type(value) for value in args)
        if len(var_args) == 1:
            return func(*args)
        else:
            print('Обнаружены различные типы данных')
    return amount_pos_args


@same_type
def combine_text(*words):
    return ' '.join(words)


print(combine_text('Hello,', 'world!') or 'Fail')
print(combine_text(2, '+', 2, '=', 4) or 'Fail')
print(combine_text('Список из 30', 0, 'можно получить так', [0] * 30) or 'Fail')