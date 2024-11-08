from time import *

class log:
    def print(msg:str):
        hour = int(time()//60//60//12%12);
        minute = int(time()//60%60);
        second = int(time()%60);
        print(f"{hour}:{minute}:{second} - {msg}");
