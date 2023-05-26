from tkinter import Tk, Canvas
import random

# Размеры
WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20
# Переменная отвечающая за состояние игры
IN_GAME = True


# Вспомогательные функции
def create_block():
    """ Создание поинта"""
    global BLOCK
    posx = SEG_SIZE * random.randint(1, (WIDTH-SEG_SIZE) / SEG_SIZE)
    posy = SEG_SIZE * random.randint(1, (HEIGHT-SEG_SIZE) / SEG_SIZE)
    BLOCK = c.create_oval(posx, posy,
                          posx+SEG_SIZE, posy+SEG_SIZE,
                          fill="yellow")


def main():
    """ Управление игровым процессом """
    global IN_GAME
    if IN_GAME:
        s.move()
        head_coords = c.coords(s.segments[-1].instance)
        x1, y1, x2, y2 = head_coords
        # Проверка, нет ли столкновения с краями игрового поля
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            IN_GAME = False
        # Поедание поинтов
        elif head_coords == c.coords(BLOCK):
            s.add_segment()
            c.delete(BLOCK)
            create_block()
        # Самоедство
        else:
            for index in range(len(s.segments)-1):
                if head_coords == c.coords(s.segments[index].instance):
                    IN_GAME = False
        root.after(100, main)
    # Если не в игре выводим сообщение о проигрыше
    else:
        set_state(restart_text, 'normal')
        set_state(game_over_text, 'normal')


class Segment(object):
    """ Класс сегмента змейки """
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                                           x+SEG_SIZE, y+SEG_SIZE,
                                           fill="white")


class Snake(object):
    """ Класс змейки """
    def __init__(self, segments):
        self.segments = segments
        #список доступных направлений движения змейки
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}
        #изначально змейка двигается вправо
        self.vector = self.mapping["Right"]

    def move(self):
        """Двигает змейку в заданном направлении"""
        # перебираем все сегменты кроме первого
        for index in range(len(self.segments)-1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index+1].instance)
            # задаем каждому сегменту позицию сегмента стоящего после него
            c.coords(segment, x1, y1, x2, y2)

        # получаем координаты сегмента перед "головой"
        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        # помещаем "голову" в направлении указанном в векторе движения
        c.coords(self.segments[-1].instance,
                 x1+self.vector[0]*SEG_SIZE, y1+self.vector[1]*SEG_SIZE,
                 x2+self.vector[0]*SEG_SIZE, y2+self.vector[1]*SEG_SIZE)

    def add_segment(self):
        """ Создает сегмент змейки """
        # определяем последний сегмент
        last_seg = c.coords(self.segments[0].instance)
        # определяем координаты куда поставить следующий сегмент
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
        # добавляем змейке еще один сегмент в заданных координатах
        self.segments.insert(0, Segment(x, y))

    def change_direction(self, event):
        """ Меняет направление движения змейки """
        # event передаст нам символ нажатой клавиши
        # и если эта клавиша в доступных направлениях
        # изменяем направление
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]

    def reset_snake(self):
        for segment in self.segments:
            c.delete(segment.instance)


def set_state(item, state):
    #устанавливаем состояние змейки
    c.itemconfigure(item, state=state)


def clicked(event):
    global IN_GAME
    s.reset_snake()
    IN_GAME = True
    c.delete(BLOCK)
    c.itemconfigure(restart_text, state='hidden')
    c.itemconfigure(game_over_text, state='hidden')
    start_game()


def start_game():
    global s
    create_block()
    s = create_snake()
    # Реакция на нажатие клавиши
    c.bind("<KeyPress>", s.change_direction)
    main()


def create_snake():
    # создание сегментов и змейки
    segments = [Segment(SEG_SIZE, SEG_SIZE),
                Segment(SEG_SIZE*2, SEG_SIZE),
                Segment(SEG_SIZE*3, SEG_SIZE)]
    return Snake(segments)


#Создаем окно
root = Tk()
# Устанавливаем название окна
root.title("Snake IS-24")

# создаем экземпляр класса Canvas и заливаем все розовым цветом

c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#e0abcb")
c.grid()
# Наводим фокус на Canvas, чтобы мы могли ловить нажатия клавиш
c.focus_set()
game_over_text = c.create_text(WIDTH/2, HEIGHT/2, text="ИГРА ОКОНЧЕНА!",
                               font='IMPACT 20', fill='red',
                               state='hidden')
restart_text = c.create_text(WIDTH/2, HEIGHT-HEIGHT/3,
                             font='IMPACT 30',
                             fill='white',
                             text="Нажмите здесь, чтобы перезапустить",
                             state='hidden')
c.tag_bind(restart_text, "<Button-1>", clicked)
start_game()
root.mainloop()