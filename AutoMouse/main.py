import win32api, win32con, win32gui
def CloseEvent():
    exit(0)

def click(BUTTON=win32con.VK_LBUTTON):
    win32api.mouse_event(win32con.VK_RBUTTON, 0, 0)
    print("Button event")

def is_activate():
    return win32api.GetAsyncKeyState(win32con.VK_NUMLOCK) != 0

def check_windowsHandle(hwnd, extra):
    print(hwnd, win32gui.GetWindowText(hwnd))

def run():
    try:
        while True:
            if is_activate():
                click()
    except Exception as e:
        print("run close: ", e)

if __name__ == "__main__":
    # run()
    win32gui.EnumWindows(check_windowsHandle, None)