import win32gui
import win32ui
import win32con
import win32api 
#grab handle to desktop window
hdesktop=win32gui.GetDesktopWindow()
#dimensions
width=win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height=win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
left=win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
right=win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
#create a device context
desktop_dc=win32gui.GetWindowDC(hdesktop)
img_dc=win32ui.CreateDCFromHandle(desktop_dc)
#memory based device context 
mem_dc=img_dc.CreateCompatibleDC()
#create bmp
screenshot=win32ui.CreateBitmap()
screenshot.CreateCompatibleBitmap(img_dc, width, height)
mem_dc.SelectObject(screenshot)
#copy to memory
mem_dc.Bitblt((0,0), (width, height), img_dc, (left, top), win32con.SRCCOPY)
#save that bitmap
screenshot.SaveBitmapFile(mem_dc, 'c:\\WINDOWS\\Temp\\screenshot.bmp')
#freedom
mem_dc.DeleteDC()
win32gui.DeleteObject(screenshot.GetHandle())
