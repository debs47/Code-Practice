import tkinter as tk
import random
from random import randint

grid_width=600
grid_height=600

def pick_random_position():
    return [randint(0, grid_width), randint(0, grid_height)]

class SpellItem:
    def __init__(self, spell):
        self.spell = spell
        x, y = random.randint(20, 600), random.randint(20, 600)
        self.obj = self.spell.create_oval(x, y, x + 10, y + 10, fill="yellow")


class EvilWizard:
    def __init__(self, canvas, x, y, size=20):
        self.evilwizard = EvilWizard
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.color = "red"

    def move_to_random_position(self):
        new_x, new_y = pick_random_position()
        self.canvas.move(self.evilwizard, new_x - self.x, new_y - self.y)
        self.x, self.y = new_x, new_y
        self.canvas.after(1000, self.move_to_random_position)

    def draw(self):
        self.canvas.create_rectangle(
            self.x - self.size // 2,
            self.y - self.size // 2,
            self.x + self.size // 2,
            self.y + self.size // 2,
            fill=self.color,
            outline="black",
            width=2
        )


class Wizard:
    def __init__(self, person):
        self.person = person
        self.wizard = self.person.create_rectangle(200, 200, 250, 250, fill="#e377c2")
        self.spells_collected = 0

    def quit_game(self):
        self.person.destroy()

    def move_left(self, event):
        self.person.move(self.wizard, -10, 0)
        self.collect_objects()

    def move_right(self, event):
        self.person.move(self.wizard, 10, 0)
        self.collect_objects()

    def move_up(self, event):
        self.person.move(self.wizard, 0, -10)
        self.collect_objects()

    def move_down(self, event):
        self.person.move(self.wizard, 0, 10)
        self.collect_objects()




    def collect_objects(self):
        for spell_item in self.spell_items:
            if self.person.find_overlapping(*spell_item.obj.coords()):
                self.spells_collected + 1
                print(f"Spell item collected! Total score: {self.spells_collected}")
                spell_item.obj.destroy()

        if self.spells_collected == 25:
            print("Congratulations! You've collected all magical objects!")


class WizardGame:
    def __init__(self, start):
        self.start = start
        self.start.title("Wizard Spell Game")
        self.canvas = tk.Canvas(start, width=600, height=600, bg="#17becf")
        self.canvas.pack()

        self.canvas.create_text(200, 100, text="Welcome to Magical Land! Help the wizard collect all the spell items!",
                                fill="red")

        self.wizard = Wizard(self.canvas)
        evil_wizard = EvilWizard(self.canvas, x=150, y=150, size=30)
        evil_wizard.draw()
        evil_wizard.move_to_random_position()
        self.spell_items = [SpellItem(self.canvas) for _ in range(25)]


        quit_button = tk.Button(self.start, text="Quit", command=self.wizard.quit_game)
        quit_button.pack()

        self.start.bind("<Left>", self.wizard.move_left)
        self.start.bind("<Right>", self.wizard.move_right)
        self.start.bind("<Up>", self.wizard.move_up)
        self.start.bind("<Down>", self.wizard.move_down)


if __name__ == "__main__":
    start = tk.Tk()
    game = WizardGame(start)
    start.mainloop()