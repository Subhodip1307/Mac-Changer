import argparse
import sys
import os
import re

class Mac_changer:
    def __init__(self,interface,new_mac):
        self.networkinterface=interface
        self.Custom_mac=new_mac
    # def restore_oldmac(self):
    #    #return your old mac from config.txt
    #    with open("config.txt", "r") as k:
    #        a = k.readlines()
    #    k.close()
    #    mac=a[0].split('=')[1]
    #    return mac
    # def restore_old_interface(self):
    #     #return your old mac's interface
    #     with open("config.txt", "r") as k:
    #         a = k.readlines()
    #     k.close()
    #     inter = a[0].split('=')[0]
    #     return inter
    def retrivemac(self):
        with open("config.txt", "r") as k:
            a = k.readlines()
        objlen = (len(a))
        k.close()
        interfaces=a[objlen - 1].split('=')[0]
        os.system(f"ifconfig {interfaces} down")
        os.system(f"ifconfig {interfaces} hw ether {a[objlen - 1].split('=')[1]}")
        os.system(f"ifconfig {interfaces} up")
        return f"your Mac id has been changed to:- {a[objlen - 1].split('=')[1]}"

    def old_mac(self):
        a = os.popen("ifconfig wlx08ea40d296bb").read()
        get_mac = re.compile(r"\b([0-9A-Za-z]{2}:){5}[0-9A-Za-z]{2}\b")
        find_mac = get_mac.search(a).group(0)
        with open("config.txt","a") as config:
            config.write(f"{self.networkinterface}= {find_mac}\n")
        config.close()
        return find_mac
    def change_mac(self):
        os.system(f"ifconfig {self.networkinterface} down")
        os.system(f"ifconfig {self.networkinterface} hw ether {self.Custom_mac}")
        os.system(f"ifconfig {self.networkinterface} up")
        return f"your Mac id has been changed to:- {self.Custom_mac}"
    @staticmethod
    def main(infomation):
        user = Mac_changer(infomation.i, infomation.cm)
        if infomation.i=="retrive" or infomation.i=="re":
            print(user.retrivemac())
            return " "
        else:
            print(f"your old mac id is: {user.old_mac()}")
            print(user.change_mac())
            return " "
if __name__ == '__main__':
    window=argparse.ArgumentParser()
    window.add_argument("-i",type=str,help="Use to declare the network interface")
    window.add_argument("-cm",type=str,help="Type here your custom mac")
    info=window.parse_args()
    sys.stdout.write(str(Mac_changer.main(info)))