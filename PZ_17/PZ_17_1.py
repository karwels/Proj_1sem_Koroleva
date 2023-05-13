# Создайте класс "Здание" с атрибутами "адрес" и "количество этажей". Напишите
# метод, который выводит информацию о здании в формате "Адрес: адрес, Количество этажей: этажи".
class Building:
    def __init__(self, address, floors):
        self.address = address
        self.floors = floors

    def info(self):
        print(f"Адрес: {self.address}, Количество этажей: {self.floors}")

BuildingOne = Building("ул. Максима Горького, 34", 9)
BuildingTwo = Building("ул. Большая Садовая, 46", 4)
BuildingThree = Building("ул. Театральная, 12", 20)
BuildingOne.info()
BuildingTwo.info()
BuildingThree.info()