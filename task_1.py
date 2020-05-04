import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        index = 0
        while True:
            current_color = self.__color[index]
            comparison = ["Зелёный", "Жёлтый", "Красный", "Жёлтый"]
            if current_color[0] == comparison[index]:
                if index == 0:
                    print(f"\033[92m{current_color[0]}\033[0m")
                    time.sleep(7)
                    index += 1
                elif index == 1:
                    print(f"\033[93m{current_color[0]}\033[0m")
                    time.sleep(2)
                    index += 1
                elif index == 2:
                    print(f"\033[91m{current_color[0]}\033[0m")
                    time.sleep(7)
                    index += 1
                elif index == 3:
                    print(f"\033[93m{current_color[0]}\033[0m")
                    time.sleep(2)
                    index = 0
            else:
                print("Несоответствие сигналов светофоров! Ща шо будет!!!")
                break


a = TrafficLight([["Зелёный"], ["Жёлтый"], ["Красный"], ["Жёлтый"]])
a.running()
