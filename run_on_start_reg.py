"""
Desc : writes a key to registry that links to the file, no admin required
"""
import winreg as reg
import os
def wtr():
    pth=os.path.dirname(os.path.realpath(__file__))
    s_name="main.py"
    address=os.path.join(pth,s_name) # create the file path
    key = reg.HKEY_CURRENT_USER # fetch the current users reg key
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run" # fetch curr key value
    open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS) # open this reg kety
    reg.SetValueEx(open,"any_name",0,reg.REG_SZ,address) # create my reg key and write it to the registry
    reg.CloseKey(open) # close it 
if __name__=="__main__":
    wtr() # run
