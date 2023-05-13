# Создайте базовый класс "Животное" со свойствами "вид",  "количество лап", "цвет
# шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него свойства
# "кличка" и "порода".
class Animal:
    def __init__(self, species, legs, color):
        self.species = species
        self.legs = legs
        self.color = color

class Dog(Animal):
    def __init__(self, species, legs, color, name, breed):
        Animal.__init__(self, species, legs, color)
        self.name = name
        self.breed = breed

DogOne = Dog("Собака", 4, "Карамельный", "Бим", "Мопс")

print(f"Вид: {DogOne.species}, количество лап: {DogOne.legs}, цвет шерсти: {DogOne.color}, кличка: {DogOne.name}, порода: {DogOne.breed}")
