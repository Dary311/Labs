def one(list, elem):
    low = 0
    high = len(list) - 1
    mid = (low + high) // 2
    while elem != list[mid]:
        if elem not in list:
            return print('-1')
        elif elem > list[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    return print(f'ID: {mid}')


def two(list, elem):
    start = -1
    f0 = 0
    f1 = 1
    f2 = 1
    while f2 < len(list):
        f0 = f1
        f1 = f2
        f2 = f1 + f0
    while f2 > 1:
        i = min(start + f0, len(list) - 1)
        if list[i] < elem:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = i
        elif list[i] > elem:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return i and print(f'ID: {i}')
    if f1 and (list[len(list) - 1] == i):
        return len(list) - 1
    return None


def three(list, direction):
    if direction == 'right':
        for i in range(len(list)):
            minimum = i
            for j in range(i + 1, len(list)):
                if list[j] < list[minimum]:
                    minimum = j
            list[minimum], list[i] = list[i], list[minimum]
    elif direction == 'left':
        for i in range(len(list)):
            maximum = i
            for j in range(i + 1, len(list)):
                if list[j] > list[maximum]:
                    maximum = j
            list[maximum], list[i] = list[i], list[maximum]
    return print(list)


def four(list, direction):
    if direction == 'right':
        for i in range(len(list)):
            for j in range(len(list) - 1 - i):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
    elif direction == 'left':
        for i in range(len(list)):
            for j in range(len(list) - 1 - i):
                if list[j] < list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
    return print(list)


def five(list, direction):
    if direction == 'right':
        mid = len(list) // 2
        while mid >= 1:
            for j in range(mid, len(list)):
                i = j
                while i > 0:
                    if list[i] < list[i - mid]:
                        list[i], list[i - 1] = list[i - 1], list[i]
                        i -= mid
                    else:
                        break
            mid //= 2
    elif direction == 'left':
        mid = len(list) // 2
        while mid >= 1:
            for j in range(mid, len(list)):
                i = j
                while i > 0:
                    if list[i] > list[i - mid]:
                        list[i], list[i - 1] = list[i - 1], list[i]
                        i -= mid
                    else:
                        break
            mid //= 2
    return print(list)


def six_default(list):
    min = []
    mid = []
    max = []
    if len(list) > 1:
        item = list[0]
        for x in list:
            if x < item:
                min.append(x)
            elif x == item:
                mid.append(x)
            elif x > item:
                max.append(x)
        return six_default(min) + mid + six_default(max)
    else:
        return list


def six_reverse(list):  # ДОДЕЛАТЬ!
    min = []
    mid = []
    max = []
    if len(list) > 1:
        item = list[-1]
        for x in list:
            if x < item:
                min.append(x)
            elif x == item:
                mid.append(x)
            elif x > item:
                max.append(x)
        return six_reverse(min) + mid + six_reverse(max)
    else:
        return list


six_reverse(list=[8, 4, 9, 52, 15, 24])
