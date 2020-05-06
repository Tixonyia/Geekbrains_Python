from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    def __init__(self, name_of_clothes, size):
        self.name_of_clothes = name_of_clothes
        self.size = size

    @abstractmethod
    def print_name(self):
        print(self.name_of_clothes)

    @abstractmethod
    def tissue_consumption(self):
        print("Refer to the method of calculating the type of clothing you need.")


class Coat(MyAbstractClass):
    @property
    def print_name(self):
        print("Calculation of fabric for coat.")

    def tissue_consumption(self):
        result = self.size / 6.5 + 0.5
        print(f"The coat will take {result} meters of fabric")


class Costume(MyAbstractClass):
    @property
    def print_name(self):
        print("Calculation of fabric for costume.")

    def tissue_consumption(self):
        result = self.size * 2 + 0.3
        print(f"The costume will take {round(result, 2)} meters of fabric.")


coat_1 = Coat("coat", 13)
coat_1.tissue_consumption()
coat_1.print_name
costume = Costume("costume", 1.78)
costume.tissue_consumption()
costume.print_name