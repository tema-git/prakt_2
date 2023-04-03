import tkinter as tk
import math

# Настройки окна
WIDTH = 800
HEIGHT = 600

# Настройки фрактала
START_X = WIDTH // 2
START_Y = HEIGHT - 50
START_LENGTH = 100
ANGLE = 20
LENGTH_RATIO = 0.7

class FractalTree:
    def __init__(self, canvas, length, angle, length_ratio):
        self.canvas = canvas
        self.length = length
        self.angle = angle
        self.length_ratio = length_ratio

    def draw(self, x, y, length, angle, depth):
        if depth == 0:
            return

        x2 = x + length * math.sin(math.radians(angle))
        y2 = y - length * math.cos(math.radians(angle))

        self.canvas.create_line(x, y, x2, y2)

        self.draw(x2, y2, length * self.length_ratio, angle + self.angle, depth - 1)
        self.draw(x2, y2, length * self.length_ratio, angle - self.angle, depth - 1)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        # Создаем холст для рисования
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        # Создаем слайдер для угла
        self.angle_var = tk.DoubleVar()
        self.angle_var.set(ANGLE)
        self.angle_slider = tk.Scale(self, from_=0, to=90, resolution=1, orient=tk.HORIZONTAL, length=200, label="Angle", variable=self.angle_var, command=self.redraw)
        self.angle_slider.pack()

        # Создаем слайдер для коэффициента убывания длины
        self.length_ratio_var = tk.DoubleVar()
        self.length_ratio_var.set(LENGTH_RATIO)
        self.length_ratio_slider = tk.Scale(self, from_=0, to=1, resolution=0.05, orient=tk.HORIZONTAL, length=200, label="Length Ratio", variable=self.length_ratio_var, command=self.redraw)
        self.length_ratio_slider.pack()

        # Рисуем фрактальное дерево
        self.tree = FractalTree(self.canvas, START_LENGTH, ANGLE, LENGTH_RATIO)
        self.redraw()

    def redraw(self, *args):
        self.canvas.delete("all")
        self.tree.angle = self.angle_var.get()
        self.tree.length_ratio = self.length_ratio_var.get()
        self.tree.draw(START_X, START_Y, START_LENGTH, 0, 10)

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
