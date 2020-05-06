class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        string = ''
        for i in self.matrix:
            for j in i:
                string += f"{j}   "
            string += "\n"
        return string

    def __add__(self, other):
        def func(el_1, el_2):
            result = []
            for i in range(len(el_1)):
                result.append(int(el_1[i]) + int(el_2[i]))
            return result

        return Matrix(list(map(func, self.matrix, other.matrix)))


obj_1 = Matrix([[11, 22, 3], [3, -13, 5], [22, 33, 43]])
obj_2 = Matrix([[4, 5, 6], [7, 8, 9], [12, 32, 54]])
obj_3 = Matrix([[34, 53, 23], [13, 123, 43], [32, 32, 45]])
print(obj_1 + obj_2 + obj_3)
print(obj_1)
print(obj_2)

