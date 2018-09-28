import wx

class A:
    def say(self):
        return 'hi'



class Test(A):
    def __init__(self):
        print(self.say())




t = Test()

