# def add(*args):
#     total_sum = 0
#     for num in args:
#         total_sum += num
#     return total_sum
#
#
# print(add(5, 8, 6, 1, 5, 9, 3))

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5, minus=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.model)
