class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def show_info(self):
        print(f"Car brend: {self.brand}, color: {self.color}")



car1 = Car("Toyota", "Red")
car2 = Car("bmw", "purple")

car1.show_info()
car2.show_info()