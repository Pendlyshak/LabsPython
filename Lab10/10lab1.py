import random
class Array:
    def __init__(self, lenght):
        self.lenght = lenght


    def create_array(self):
        a = [random.randint(self.lenght)]
        print(a)

#знаходження суми цифр
    def suma(self):
        suma = 0
        for el in a:
            suma += el
            return suma

#----------------------------------------------------
f = Array(6)
f.create_array()
print(f)
array = Array
res = array.suma()
print(res)





