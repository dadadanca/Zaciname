a=[1,2,3,4,5,6]
b=[1,2,3,4,5,6]
c=[1, 2, 3, 9]

def jsouStejne (x,y):
    if len(x)== len(y):
        i = 0
        while i < len(x):
            if x[i] != y[i]:
                return False
            i = i+1
        return True
    else:
        return False


assert jsouStejne(a, b)
assert not jsouStejne(a, c)


def jsouStejneR (x,y):
    if len(x)==len(y):
        if len(x) == 0:
            return True
        if x[0] == y [0]:
            return jsouStejneR (x[1::], y [1::])
        else:
            return False
    else:
        return False



assert jsouStejneR(a, b)
assert not jsouStejneR(a, c)

