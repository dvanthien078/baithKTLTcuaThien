print('đinh văn thiện msv 235752021610032')
import tkinter
import random

colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
color_translations = {
    'Red': 'Đỏ',
    'Blue': 'Xanh dương',
    'Green': 'Xanh lá',
    'Pink': 'Hồng',
    'Black': 'Đen',
    'Yellow': 'Vàng',
    'Orange': 'Cam',
    'White': 'Trắng',
    'Purple': 'Tím',
    'Brown': 'Nâu'
}
score = 0
timeleft = 120

def startGame(event):
    if timeleft == 120:
        countdown()
    nextColour()

def nextColour():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        user_input = e.get().lower()
        if user_input == color_translations[colors[0]].lower():
            score += 2
        e.delete(0, tkinter.END)
        random.shuffle(colors)
        label.config(fg=str(colors[1]), text=str(colors[0]))
        scoreLabel.config(text="Điểm: " + str(score))

def countdown():
    global timeleft
