import os

def menu():
    
    os.system('printf "\033[3;36m"') 
    os.system('figlet GBasics')

    print("""                               
=======================================
BY: Glitch
=======================================
Telegram : @GlitchT
=======================================
Youtube : Glitch - جلتش
=======================================
Choose A Number..
_______________________________________________
[1] The Basics Termux
_______________________________________________
[00] Exit
_______________________________________________""")

loop = True

while loop:
    menu()
    what = input("Choose:")
    if what == "1":
        print("===================================")
        print("======>>")
        g = input("Do You Want To Continue? (y/n): ")
        print("================================")
        if g == "y":
            print("========================================================")
            print("[+] Leave The Phone And Set It To Continue Downloading")
            print("[+] Because This Will Take A Long Time")            
            print("========================================================")
            os.system("apt update")
            os.system("apt upgrade")
            os.system("pkg install update")
            os.system("pkg install upgrade")
            os.system("pkg update")
            os.system("termux-setup-storage")
            os.system("apt-get update")
            os.system("apt-get upgrade")
            os.system("apt install php")
            os.system("apt install python")
            os.system("apt install python2")
            os.system("apt install git")
            os.system("apt install golang")
            os.system("apt install host")
            os.system("apt install nano")
            os.system("apt install havij")
            os.system("apt install hydra")
            os.system("apt install wireshark")
            os.system("pkg install figlet")
            os.system("pkg install wget")
            os.system("pkg install wget -y")
            os.system("pkg install python2 -y")
            os.system("pkg install python2-dev -y")
            os.system("apt install wireshark")
            os.system("pkg install cowsay")
            os.system("pkg install toilet")
            os.system("pkg install ruby")
            os.system("pkg install help ")
            os.system("gem install lolcat")
            os.system("pkg install curl")
            os.system("pkg install wgetrc")
            os.system("pkg install unzip")
            os.system("pkg install openssh")
            os.system("pkg install tor")
            os.system("pkg install uzip")
            os.system("pkg install net-tools")
            os.system("pkg install unrar")
            os.system("pkg install clang")
            os.system("pkg install w3m")
            os.system("pkg install proot")
            os.system("pip2 install wegt")
            os.system("pip2 install requests")
            os.system("pkg install sl")
            os.system("apt update && apt upgrade && pkg update && pkg upgrade")
            os.system("clear")            
            print("====================================")
            print("[+] Basics Downloaded Successfully")
            print("[+] Don't Forget To Follow us")
            print("====================================")
            gmenu = input("Back To Menu? (y/n): ")
            if gmenu == "y":
                menu()
            else:
                break
    elif what == "00":
        print("Thank You To Use {GBasics}")
        break