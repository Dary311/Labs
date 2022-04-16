def one(*args):
    return print(args)


def two(*args):
    numbers = []
    for x in args:
        numbers.append(x)
    numbers.sort()
    numbers.reverse()
    return print(numbers)


def five(*args):
    numbers = []
    for x in args:
        if int(x) / float(x) == 1.0:
            numbers.append(x)
        else:
            return print(args)
    numbers.sort()
    return print(numbers)


def six(dict, elem):
    if elem in dict:
        dict = dict.replace(elem, '', 1)
        return print(dict)
    else:
        return print(dict)


def three(First_name, Second_name, Weight, Hight, Age):
    data = {'Age': Age, 'Weight': Weight, 'Hight': Hight, 'First_name': First_name}
    Sex = input('Укажите пол: ')
    data['Sex'] = Sex
    return print(data)


def four_max():
    dict_one = {'a': 1, 'b': 5, 'c': 9}
    dict_two = {'a': 4, 'b': 2}
    dict_max = {}
    dicts = [dict_one, dict_two]
    for key_1, value_1 in dict_one.items():
        for key_2, value_2 in dict_two.items():
            if key_1 == key_2:
                dict_max[key_1] = max(value_1, value_2)
    print(dict_max)


def four_sum():
    dict_one = {'a': 1, 'b': 5, 'c': 9}
    dict_two = {'a': 4, 'b': 2}
    dict_sum = {}
    dicts = [dict_one, dict_two]
    for key_1, value_1 in dict_one.items():
        for key_2, value_2 in dict_two.items():
            if key_1 == key_2:
                dict_sum[key_1] = value_1+value_2
    print(dict_sum)