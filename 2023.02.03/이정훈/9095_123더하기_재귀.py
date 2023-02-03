def _123_plus(N) :
    if N == 1 :
        return 1
    elif N == 2 :
        return 2
    elif N == 3 :
        return 4
    else :
        return _123_plus(N-3) + _123_plus(N-2) + _123_plus(N-1)


T = int(input())

for tc in range(1, 1+T) :
    N = int(input())
    print(_123_plus(N))

