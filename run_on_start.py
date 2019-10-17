"""
Made by cswil : https://github.com/cswil
A script that adds the program to startup
"""
import os
fp=os.getcwd()+"/main.py"
os.chdir("C:/Users/"+os.path.expandvars("%userprofile%").split("\\")[2]+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
with open("start.bat","w") as f:
    f.write('start '+fp)
    f.close()
