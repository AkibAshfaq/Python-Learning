from abc import ABC, abstractmethod 

# ABC for abstract and to have common interface accisable
class animal(ABC):
    
    @abstractmethod
    def sound(self):
        return "Animal Sound"
    
    
    def move(self):
        return "moving"

    @property
    @abstractmethod
    def species(self):
        pass 


# Inherited Class from animal
class dog(animal):
    
    def sound(self):
        return "Bark"

    def move(self):
        return "moving 1"   
    
    @property
    def species(self):
        return "Canine" 

# instance of class
dg = dog()

# Caling functions 
print(dg.sound())
print(dg.move())
print(dg.species)

class public:
    def __init__(self):
        self.name = "Public"


# (_) single underscore means protected 
class protected:
    
    def __init__(self):
        self._name = "protected"

class Subclass(protected):
    def see(self):
        return self._name  # Accessible in subclass

# (__) double underscore means private 
class private:

    def __init__(self):
        self.__name = "Private"

    def see(self):
        return self.__name


pb = public()
po = Subclass()
pv = private()


print(pb.name)
print(po.see()) # print(po.name)  Cant access cause protected
print(pv.see())# print(pv.name) cant be accessed by any other class expect itself


# Iterator
s = "ABCDEF"
ss = iter(s)

while True:
    try:
        print(next(ss))
    except:
        print("End of iternation")
        break


# Try blocks
try:
    m = 'b' / 3
except Exception:
    print("Syntax Error")
else:
    print("In else block")
finally:
    print("Final block")
    
# User made exeptions.
class InvalidAgeError(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120"):
        self.age = age
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.age} -> {self.msg}'

def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print(f"Age set to: {age}")

# User made exeption in use
try:
    set_age(150)  
except InvalidAgeError as e:
    print(e)
