class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def result(self, ):
        print(f"{self._length * self._width * 25 * 5 / 1000} T.")


a = Road(float(input("Enter length (m): ")), float(input("Enter width (m): ")))
a.result()
