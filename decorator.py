def decor(num):
    def inner():
        a = num()
        add = a + 5
        return add
    return inner

@decor
def num():
    return 10

print(num())