from tkinter import *
from tkinter import filedialog

def getResource():
    path = filedialog.askopenfilename(initialdir="./png", title="Select file", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*")))
    if not path:
        return "No file selected"
    
    # png, jpg 검사
    if path.endswith(".png") or path.endswith(".jpg"):
        setImage(path)
        return path
    else:
        return "Invalid file"

def setImage(path):
    # frame에 이미지 배경 추가.
    root.wm_attributes("-transparentcolor", "")
    img = PhotoImage(file=path)
    lbl = Label(root, image=img)
    lbl.image = img
    lbl.place(x=0, y=0)
    lbl.pack()
    
    return
    

width = 900
height = 600

root = Tk()
root.title("Capture")
root.geometry(f"{width}x{height}")

root.wm_attributes("-transparentcolor", "green")

my_frame = Frame(root, width=width, height=height, bg="green")
my_frame.pack(padx=10, pady=10)

def on_resize(root, frame):
    w = root.winfo_width()
    h = root.winfo_height()
    try:
        frame.config(width=w, height=h)
    except:
        pass
    return 

root.bind("<Configure>", lambda e: on_resize(root, my_frame))

menu = Menu(root)

menu_option = Menu(menu, tearoff=0)
menu_option.add_command(label="Open", command=lambda: getResource())
menu.add_cascade(label="Option", menu=menu_option)

root.configure(menu=menu)

root = mainloop()

