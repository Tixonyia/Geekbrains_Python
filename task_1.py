import datetime


class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def conversion(cls, data):
        try:
            conv = [int(d) for d in data.split("-")]
            return conv
        except ValueError:
            print("Something is wrong with numbers.")

    @staticmethod
    def validity(result):
        if len(result) != 3:
            print("Something is wrong with numbers. Wrong quantity")
        else:
            try:
                datetime.date(result[2], result[1], result[0])
                print("Things are good.")
            except ValueError:
                print("Сheck the number of days per month or months in a year.")

    def communication(self):
        result_conversion = Data.conversion(self.data)
        Data.validity(result_conversion)


string = Data("12-02-2345")
string.communication()
