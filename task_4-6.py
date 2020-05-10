from abc import ABC, abstractmethod


class OwnErr(Exception):
    def __init__(self, text):
        self.text = text


class Warehouse(ABC):
    while True:
        try:
            stock_balance = list(map(int, input("Enter the balance of all equipment in "
                                                "stock separated by space(printers scanners photocopiers): ").split()))
            if len(stock_balance) != 3:
                raise OwnErr("Three Integer Conception Required.")
            printers_balance_in_departments, scanners_balance_in_departments, photocopiers_balance_in_departments \
                = 1, 1, 1
            break
        except ValueError:
            print("Enter correct data.")
        except OwnErr as own:
            print(own)

    @abstractmethod
    def residue_calculation(self):
        pass


class OfficeEquipmentWarehouse(Warehouse):
    def __init__(self, name, person_in_charge, id_name):
        self.name = name
        self.person_in_charge = person_in_charge
        self.id_name = id_name

    @staticmethod
    def calculation(units_stock, units_departments):
        while True:
            try:
                replenishment = int(input("How many vehicles need to be moved?('+' -> departments, '-' -> stock: "))

                if units_stock < replenishment:
                    print("No stock quantity required.")
                    return units_stock, units_departments
                elif units_departments == replenishment:
                    print("And what should the guys do?")
                    return units_stock, units_departments
                else:
                    return units_stock - replenishment, units_departments + replenishment
            except ValueError:
                print("Enter correct data.")

    def residue_calculation(self):
        return f'In stock of units: {sum(Warehouse.stock_balance)}'


class Printers(OfficeEquipmentWarehouse):

    def __init__(self, name, person_in_charge, id_name, cartridge):
        super().__init__(name, person_in_charge, id_name)
        self.cartridge = cartridge

    @property
    def residue_calculation(self):
        Warehouse.stock_balance[0], Warehouse.printers_balance_in_departments = \
            OfficeEquipmentWarehouse.calculation(Warehouse.stock_balance[0], Warehouse.printers_balance_in_departments)
        return f"In departments of printers: {Warehouse.printers_balance_in_departments}"

    def expendable_materials(self):
        return f"For printer needed cartridge - {self.cartridge}."


class Scanners(OfficeEquipmentWarehouse):

    def __init__(self, name, person_in_charge, id_name, interchangeable_casters):
        super().__init__(name, person_in_charge, id_name)
        self.interchangeable_casters = interchangeable_casters

    @property
    def residue_calculation(self):
        Warehouse.stock_balance[1], Warehouse.scanners_balance_in_departments = \
            OfficeEquipmentWarehouse.calculation(Warehouse.stock_balance[1], Warehouse.scanners_balance_in_departments)
        return f"In departments of scanners: {Warehouse.scanners_balance_in_departments}"

    def expendable_materials(self):
        return f"For scanner needed interchangeable casters - {self.interchangeable_casters}."


class Photocopiers(OfficeEquipmentWarehouse):

    def __init__(self, name, person_in_charge, id_name, toner):
        super().__init__(name, person_in_charge, id_name)
        self.toner = toner

    @property
    def residue_calculation(self):
        Warehouse.stock_balance[2], Warehouse.photocopiers_balance_in_departments = \
            OfficeEquipmentWarehouse.calculation(Warehouse.stock_balance[2],
                                                 Warehouse.photocopiers_balance_in_departments)
        return f"In departments of photocopiers: {Warehouse.photocopiers_balance_in_departments}"

    def expendable_materials(self):
        return f"For photocopier needed toner - {self.toner}."


printer_1 = Printers('Brother DCP-J100', 'Petrov', 5344, 'vendor code: 0896865')
scanner_1 = Scanners('Panasonic KV-SS009', 'Ivanov', 1234, 'vendor code: 2345')
photocopier_1 = Photocopiers('Xerox Color C60', 'Sidorov', 4326, 'vendor code: 2345')
print(printer_1.residue_calculation)
print(OfficeEquipmentWarehouse.residue_calculation(1))
print(scanner_1.person_in_charge)
print(photocopier_1.name)
print(printer_1.id_name)
print(photocopier_1.expendable_materials())
