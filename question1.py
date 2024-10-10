def sumab(a):
    def sumb(b):
        return a + b # a has local scope
    return sumb

f = sumab(20)
# print(f)
print(f(10))

