from tkinter import *

def main():
    root = Tk()
    root.title("Крестики нолики")
    #geo = "400x" + str(len(ips * 19) + 50)
    root.geometry("400x400+100+100")
    root.resizable(width=False, height=False)
    canv = Canvas(bg="white", width=1000, height=1000)
    canv.grid()
    canv.create_oval((10, 20, 30, 40), width=0, fill='black')
    #canv.bind("<Button-1>")
    root.mainloop()

if __name__ == "__main__":
    main()
