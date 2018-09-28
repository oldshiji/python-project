class Dog:
    tricks = []
    def __init__(self,name):
        self.name = name
    def add_Tricks(self,trick):
        self.tricks.append(trick)





d = Dog('tom')
e = Dog('tony');

d.add_Tricks('Lucy')
e.add_Tricks('Georgo')

print(d.tricks)
print(e.tricks)