import argparse
import sys
import os
import re
import platform
class Mac_changer:
    def __init__(self,interface,new_mac):
        self.networkinterface=interface
        self.Custom_mac=new_mac
    def old_mac(self):
        a = os.popen("ifconfig wlx08ea40d296bb").read()
        get_mac = re.compile(r"\b([0-9A-Za-z]{2}:){5}[0-9A-Za-z]{2}\b")
        find_mac = get_mac.search(a).group(0)
        with open("config.txt","a") as config:
            config.write(find_mac)
        config.close()
        return f"Your current mac is : {find_mac}"
    def new_mac(self):
        os.system(f"ifconfig {self.networkinterface} down")
        os.system(f"ifconfig {self.networkinterface} hw ether {self.Custom_mac}")
        os.system(f"ifconfig {self.networkinterface} up")
        return f"your Mac id has been changed to:- {self.Custom_mac}"
    @staticmethod
    def main(infomation):
        user=Mac_changer(infomation.i,infomation.cm)
        print(user.old_mac())
        print(user.new_mac())
if __name__ == '__main__':
    window=argparse.ArgumentParser()
    window.add_argument("-i",type=str,help="Use to declare the network interface")
    window.add_argument("-cm",type=str,help="Type here your custom mac")
    info=window.parse_args()
    sys.stdout.write(str(Mac_changer.main(info)))