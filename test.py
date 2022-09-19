class Cat:
    def __init__(self, x):
        self.x = x

class Dog:
    def __init__(self, x):
        self.x = x

cats = [Cat(20), Cat(30)]
dogs = [Dog(10), Dog(15), Dog(25)]

nums = [1, 2, 4, 5]

print(type(a for a in nums))

print(type([a for a in nums]))


a = [dog for dog in dogs if dog.x == max(d.x for d in dogs)]
print(a[0])
