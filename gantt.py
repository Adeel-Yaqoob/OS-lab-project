import tkinter as tk
import random


class GanttChart:

    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 10
        self.colors = {}

    def random_color(self):
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))

    def draw(self, pid, time):

        if pid not in self.colors:
            self.colors[pid] = self.random_color()

        color = self.colors[pid]

        self.canvas.create_rectangle(
            self.x,
            20,
            self.x + 40,
            60,
            fill=color
        )

        self.canvas.create_text(
            self.x + 20,
            40,
            text=pid,
            fill="black"
        )

        self.canvas.create_text(
            self.x,
            70,
            text=str(time)
        )

        self.x += 40