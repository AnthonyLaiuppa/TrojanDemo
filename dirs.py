import os

def run(**args):
    print "[*] In dirs module."
    files=os.listdir(".")
    return str(files)
