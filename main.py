from tkinter import *


def b1(event):
    x = event.x
    y = event.y
    print(x,y)


window_width = 400
window_height = 400
window_xpos = 100
window_ypos = 100
height_indent = 30

root = Tk()
root.title("Крестики нолики")
win_geo = str(window_width) + "x" + str(window_height + height_indent) + "+" + str(window_xpos) + "+" + str(window_ypos)
root.geometry(win_geo)
root.resizable(width=False, height=False)
canv = Canvas(bg="white", width=1000, height=1000)
canv.grid()

# Draw vertical lines
canv.create_line(window_width / 3, height_indent, window_width / 3, window_height + height_indent)
canv.create_line(window_width / 3 * 2, + height_indent, window_width / 3 * 2, window_height + height_indent)

#Draw header underline
canv.create_line(0, height_indent, window_width, height_indent)

# Draw horizontal lines
canv.create_line(0, window_height / 3 + height_indent, window_width, window_height / 3 + height_indent)
canv.create_line(0, window_height / 3 * 2 + height_indent, window_width, window_height / 3 * 2 + height_indent)

root.bind('<Button-1>', b1)

root.mainloop()

