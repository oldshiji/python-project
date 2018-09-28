
def f1():
    return 'hi'


class C:
    f = f1

    def g(self):
        return 'g'

    h = g


c = C()

#print(c.f())
#print(c.h())

print(f1())
#print(c.f())