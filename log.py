from time import *

class log:
    def printg(msg:str):
        t:float = time()
        hour = int(t//60//60//12%12);
        minute = int(t//60%60);
        second = int(time()%60);
        print(f"{hour}:{minute}:{second} - \033[92m{msg}\033[0m");
    def printr(msg:str):
        t:float = time()
        hour = int(t//60//60//12%12);
        minute = int(t//60%60);
        second = int(time()%60);
        print(f"{hour}:{minute}:{second} - \033[91m{msg}\033[0m");
    def printb(msg:str):
        t:float = time()
        hour = int(t//60//60//12%12);
        minute = int(t//60%60);
        second = int(time()%60);
        print(f"{hour}:{minute}:{second} - \033[94m{msg}\033[0m");
    def printy(msg:str):
        t:float = time()
        hour = int(t//60//60//12%12);
        minute = int(t//60%60);
        second = int(time()%60);
        print(f"{hour}:{minute}:{second} - \033[93m{msg}\033[0m");
