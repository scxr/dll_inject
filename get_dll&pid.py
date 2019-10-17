#Made by cswil : https://github.com/cswil
import psutil,os
got=False
for proc in psutil.process_iter():
    try:
        p=psutil.Process(os.getpid())
        for dll in p.memory_maps():
            if got == False: # stop an infinite loop, we only need 1 dll
                print(os.getpid(),dll.path)
            else:
                break
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
