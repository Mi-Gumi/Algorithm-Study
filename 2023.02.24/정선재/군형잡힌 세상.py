while True:
    a = input()
    _list = []
    if a == '.':
        break

    for i in a:
        if i == '(':
            _list.append(i)
        elif i == '[':
            _list.append(i)
        elif i == ')':
            if len(_list) != 0 and _list[-1] == '(':
                _list.pop(-1)
            else:
                _list.append(i)
                break

        elif i == ']':
            if len(_list) != 0 and _list[-1] == '[':
                _list.pop(-1)

            else:
                _list.append(i)
                break

    if len(_list) == 0:
        print('yes')

    else:
        print('no')
