# sorting a list in ascending and descending order


def sorting():

    n = int(input('Enter the number of items in the list: '))
    numbers = []

    for i in range(0, n):
        print('Enter value for index', i, )
        item = int(input())
        numbers.append(item)

    prompt = input('Enter sorting method: ')

    if prompt is None:
        numbers = []
    if prompt in ('a', 'asc', 'ascend'):
        numbers.sort()
        return numbers
    if prompt in ('d', 'des', 'descend'):
        numbers.sort(reverse=True)
        return numbers
    if prompt in ('n', 'none'):
        return numbers

    return numbers


print(sorting())
