class Dog:
    def __init__(self,name):
        self.name = name
        self.tricks = []
    def add_Tricks(self,tricks):
        self.tricks.append(tricks)




d = Dog('tom');
e = Dog('tony');

d.add_Tricks('Lucy')
e.add_Tricks('Gergo')

print(d.tricks)
print(e.tricks)