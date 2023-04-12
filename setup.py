import platform
import os
if platform.system()=="Linux":
    os.system("sudo su")
    os.system("pip3 install pyfiglet")
else:
    print(f"sorry to say that but this doesn't work on {platform.system()}")
    