import ctypes
import random
import time
import sys

user32= ctypes.windll.user32
kernel32=ctypes.windll.kernel32

keystrokes = 0
clicks     = 0
doubleClicks=0

class LASTINPUTINFO(ctypes.Structure):
    _fields_=[("cbSize", ctypes.c_uint),
              ("cbSize", ctypes.c_ulong)
             ]

def getLastInput():
    
    struct_lastinputinfo=LASTINPUTINFO()
    struct_lastinputinfo.cbSize=ctypes.sizeof(LASTINPUTINFO)

    user32.GetLastInputInfo(ctypes.byref(struct_lastinputinfo))

    run_time=kernel32.GetTickCount()
    elapsed=run_time-struct_lastinputinfo.dwTime
    return elapsed

def getKeyPress():
    global mouse_clicks
    global keystrokes
    
    for i in range(0, 0xff):
        if user32.GetAsyincKeyState(i)== -32767:
        #0x1=mouse click
            if i == 0x1:
                mouse_clicks+=1 
                return time.time()
            elif i > 32 and i < 127:
                keystrokes+=1

    return None 

def detectSandbox():
    global mouse_clicks
    global keystrokes
    max_keystrokes=random.randint(10,25)
    max_mouse_clicks=random.randint(5,25)
    doubles=0
    max_doubles=10
    double_threshhold=0.250 #seconds
    first_double=None
    avg_mousetime=0
    max_input=3000 #milisecs
    previous_timestamp=None
    detection_complete=False
    last_input=getLastInput()

    if last_input>=max_input
        sys.exit(0)
    
    while not detection_complete:
        keypress_time=getKeyPress()
        if keypress_time is not None and previous_timestamp is not None:
            elapsed=keypress_time-previous_timestamp #time between doubles
            if elapsed<=double_threshold:
                doubles+=1#if usr doubles
                if first_double is None:
                    first_double=time.time()#time stamp it
                else:
                    if doubles==max_doubles:
                        if keypress_time - first_double<=(max_doubles * double_threshhold):
                            sys.exit(0)
            if keystrokes>=max_keystrokes: and doubles>=max_doubles and mouse_clicks>=max_mouse_clicks:
                
                return
            previous_timestamp=keypress_time
        elif keypress_time is not None:
            previous_timestamp=keypress_time

detectSandbox()                
            
    
