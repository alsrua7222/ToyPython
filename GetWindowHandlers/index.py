import win32gui
def check_windowsHandle(hwnd, extra):
    print(hwnd, win32gui.GetWindowText(hwnd))
    
if __name__ == '__main__':
    win32gui.EnumWindows(check_windowsHandle, None)