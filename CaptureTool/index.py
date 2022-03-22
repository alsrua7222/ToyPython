from tkinter import *
from tkinter import filedialog
from PIL import ImageGrab
from Func import *
from recordVideo import *


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

def makeScreenshot():
    # 스크린샷 저장
    x1 = my_frame.winfo_rootx()
    y1 = my_frame.winfo_rooty()
    x2 = x1 + my_frame.winfo_width()
    y2 = y1 + my_frame.winfo_height()
    
    print(my_frame.winfo_width(), my_frame.winfo_height())
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    # 현재 날짜의 시간으로 저장.
    img.save(getDateTimeCurrent() + ".png")
    return

def Record():
    if rV.isRecording:
        print("레코딩 강제 종료.")
        rV.isRecording = False
        return
    print("레코딩 시작")
    x1 = my_frame.winfo_rootx()
    y1 = my_frame.winfo_rooty()
    x2 = x1 + my_frame.winfo_width()
    y2 = y1 + my_frame.winfo_height()

    
    rV.StartRecord(root, point=[x1, y1, x2, y2])
    rV.isRecording = True
    return

width = 900
height = 600
rV = recordVideo('F3')
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
root.bind("<F2>", lambda e: makeScreenshot())
root.bind("<F3>", lambda e: Record())
menu = Menu(root)

menu_option = Menu(menu, tearoff=0)
menu_option.add_command(label="Open", command=lambda: getResource())
menu.add_cascade(label="Option", menu=menu_option)

root.configure(menu=menu)

root = mainloop()

