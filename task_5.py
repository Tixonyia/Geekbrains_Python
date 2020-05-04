class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}а.")


class Pen(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print(f"Запуск отрисовки {self.title}а ручкой.")


class Pencil(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print(f"Запуск отрисовки {self.title}а карандашом.")


class Handle(Stationery):
    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print(f"Запуск отрисовки {self.title}а маркером.")


hero_draw = Stationery("Супермен")
print(hero_draw.title)
hero_draw.draw()
hero_draw_pen = Pen("Халк")
hero_draw_pen.draw()
hero_draw_pencil = Pencil("Бугермен")
hero_draw_pencil.draw()
hero_draw_handel = Handle("Спаун")
hero_draw_handel.draw()
