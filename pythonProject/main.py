from tkinter import *
from tkinter import ttk

dict = {'red': False, 'green': False, 'blue': False}


def red_checked(dict):
    dict['red'] = not dict['red']


def green_checked(dict):
    dict['green'] = not dict['green']


def blue_checked(dict):
    dict['blue'] = not dict['blue']


def frame_color(dict, frame):
    if dict['red'] and dict['blue'] and dict['green']:
        print('3')
    elif dict['red'] and dict['blue'] and not dict['green']:
        print('2')

def get_num():
    print(1)


window = Tk()

window.title('RGB')
window.geometry('450x320+30+90')
window.resizable(False, False)
#
# checkbuttonR = Checkbutton(window, text='წითელი', command=red_checked(dict))
# checkbuttonR.pack()
#
# checkbuttonG = Checkbutton(window, text='მწვანე', command=green_checked(dict))
# checkbuttonG.pack()
#
# checkbuttonB = Checkbutton(window, text='ლურჯი', command=blue_checked(dict))
# checkbuttonB.pack()
#
frame = Frame(window, width=300, height=300, relief=GROOVE, background='black')
# frame.pack(side='bottom')

submitButton = ttk.Button(window, text='SUBMIT', command=get_num()).grid(row=2, column=2)
# submitButton.place(x=374, y=19)

# frame.configure(fg = "white")


window.mainloop()
