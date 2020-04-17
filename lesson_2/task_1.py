my_list = [
            1, 1.3, "abrakatabra", [1, 23], complex(5, 6), ("xc", 23),
            {"as": 54}, {400, True, None, 'text'}, True, b"sadfsad",
            bytearray(b"text"), None, ZeroDivisionError, range(10)
            ]

for i in my_list:
    print(type(i))