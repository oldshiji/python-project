class Dog:
    kind = 'candy'
    def __init__(self,name):
        self.name = name




d = Dog('buddy')
e = Dog('insult')

print(d.kind)
print(e.kind)

print(d.name)
print(e.name)