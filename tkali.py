#!/usr/bin/python

import sys
import os, time

def banner():
    print("""
    -------------------------------------------
 \033[0;32mCreator:\033[0;m \033[1;37msatanic\033[0;m                   \033[1;31m\033[0;m 
\033[1;31m\033[0;m \033[0;32mGithub:\033[0;m \033[1;37mhttps://github.com/satanic-ofc\033[0;m
    -------------------------------------------
    """)
banner()


def menu():
	print("""
\033[1;37m(1)\033[0;m \033[0;32mNmap\033[0;m               \033[1;37m(11)\033[0;m \033[0;32mWireshark\033[0;m     \033[1;37m(21)\033[0;m \033[0;32mAutopsy\033[0;m
\033[1;37m(2)\033[0;m \033[0;32mNikto\033[0;m              \033[1;37m(12)\033[0;m \033[0;32mCrunch\033[0;m        \033[1;37m(22)\033[0;m \033[0;32mPipal\033[0;m
\033[1;37m(3)\033[0;m \033[0;32mJohn the Ripper\033[0;m    \033[1;37m(13)\033[0;m \033[0;32mCewl\033[0;m          \033[1;37m(23)\033[0;m \033[0;32mMasscan\033[0;m
\033[1;37m(4)\033[0;m \033[0;32mWifite\033[0;m             \033[1;37m(14)\033[0;m \033[0;32mMedusa\033[0;m        \033[1;37m(24)\033[0;m \033[0;32mWhatWeb\033[0;m
\033[1;37m(5)\033[0;m \033[0;32mMetasploit\033[0;m         \033[1;37m(15)\033[0;m \033[0;32mReaver\033[0;m        \033[1;37m(25)\033[0;m \033[0;32mMaltego\033[0;m
\033[1;37m(6)\033[0;m \033[0;32mSqlmap\033[0;m             \033[1;37m(16)\033[0;m \033[0;32mNcrack\033[0;m        \033[1;37m(26)\033[0;m \033[0;32mArmitage\033[0;m
\033[1;37m(7)\033[0;m \033[0;32mAircrack-ng\033[0;m        \033[1;37m(17)\033[0;m \033[0;32mHydra\033[0;m         \033[1;37m(27)\033[0;m \033[0;32mArping\033[0;m
\033[1;37m(8)\033[0;m \033[0;32mHashCat\033[0;m            \033[1;37m(18)\033[0;m \033[0;32mEtterCap\033[0;m      \033[1;37m(28)\033[0;m \033[0;32mProxyChains\033[0;m
\033[1;37m(9)\033[0;m \033[0;32mLegion\033[0;m             \033[1;37m(19)\033[0;m \033[0;32mMACchanger\033[0;m    \033[1;37m(29)\033[0;m \033[0;32mTor-Browser\033[0;m
\033[1;37m(10)\033[0;m \033[0;32mWPScan\033[0;m            \033[1;37m(20)\033[0;m \033[0;32mDNSchef\033[0;m       \033[1;37m(0)\033[0;m \033[0;31mSalir\033[0;m\033[0;37m/\033[0;m\033[0;31mLeave\033[0;m
""")
menu()

X = input("\033[1;44;37mElige una herramienta:\033[0;m \033[1;36m\n\n>\033[0;m ")

if X == "1":
    tool = os.system("apt-get install nmap")
elif X == "2":
    tool = os.system("apt-get install nikto -y")
elif X == "3":
    tool = os.system("apt-get install john")
elif X == "4":
    tool = os.system("apt-get install wifite")
elif X == "5":
    tool = os.system("apt-get install metasploit-framework")
elif X == "6":
    tool = os.system("apt-get install sqlmap")
elif X == "7":
    tool = os.system("apt-get install aircrack-ng")
elif X == "8":
    tool = os.system("apt-get install hashcat")
elif X == "9":
    tool = os.system("apt-get install legion -y")
elif X == "10":
    tool = os.system("apt-get install wpscan")
elif X == "11":
    tool = os.system("apt-get install wireshark")
elif X == "12":
    tool = os.system("apt-get install crunch -y")
elif X == "13":
    tool = os.system("apt-get install cewl")
elif X == "14":
    tool = os.system("apt-get install medusa")
elif X == "15":
    tool = os.system("apt-get install reaver")
elif X == "16":
    tool = os.system("apt-get install ncrack")
elif X == "17":
    tool = os.system("apt-get install hydra-gtk")
elif X == "18":
    tool = os.system("apt-get install ettercap")
    tool = os.system("apt-get install ettercap-graphical")
elif X == "19":
    tool = os.system("apt-get install macchanger -y")
elif X == "20":
    tool = os.system("apt-get install dnschef")
elif X == "21":
    tool = os.system("apt-get install autopsy")
elif X == "22":
    tool = os.system("apt-get install pipal")
elif X == "23":
    tool = os.system("apt-get --assume-yes install git make gcc")
    tool = os.system("git clone https://github.com/robertdavidgraham/masscan")
    tool = os.system("cd masscan")
    tool = os.system("make install")
elif X == "24":
    tool = os.system("apt-get install whatweb -y")
elif X == "25":
    tool = os.system("apt-get install maltego-teeth")
elif X == "26":
    tool = os.system("apt-get install armitage")
elif X == "27":
    tool = os.system("apt-get install arping")
elif X == "28":
    tool = os.system("apt-get install proxychains -y")
elif X == "29":
    tool = os.system("apt-get install tor torbrowser-launcher")
elif X == "0":
    tool = os.system("exit")
    time.sleep(1)
    print("\n\033[1;32mGracias por usar este script, vuelve nuevamente\033[0;m\033[1;37m!\033[0;m")
else:
    print("\033[1;31m\nError:\033[0;m Carácter incorrecto, intentelo nuevamente")                                                                     
