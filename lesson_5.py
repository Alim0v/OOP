class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def display_info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}")


car1 = Car("Toyota", "Camry", 2020)
car1.display_info()  

car2 = Car("BMW", "X5", 2022)
car2.display_info()  