# class Bird:
#     def fly(self):
#         return "Flying"
#
#
# class Sparrow(Bird):
#     def fly(self):
#         return "Sparrow flying"
#
#
# class Ostrich(Bird):
#     def fly(self):
#         raise Exception("Ostrich cannot fly")

class Bird:
    def legs(self):
        return 2

class FlyingBird(Bird):
    def fly(self):
        return "flying flying"

class Ostrich(Bird):
    pass

class Sparrow(FlyingBird):
    def fly(self):
        return "sparrow flying"