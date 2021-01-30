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
Gmail : glitcht09.gmail.com
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
    what = input("Choose: ")
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
            os.system("apt update -y")
            os.system("apt upgrade -y")
            os.system("pkg update -y")
            os.system("pkg upgrade -y")
            os.system("termux-setup-storage -y")
            os.system("apt-get update -y")
            os.system("apt-get upgrade -y")
            os.system("apt install php -y")
            os.system("apt install python -y")
            os.system("apt install python2 -y")
            os.system("apt install git -y")
            os.system("apt install golang -y")
            os.system("apt install host -y")
            os.system("apt install nano -y")
            os.system("apt install havij -y")
            os.system("apt install hydra -y")
            os.system("apt install wireshark -y")
            os.system("pkg install figlet -y")
            os.system("pkg install wget -y")
            os.system("pkg install wget -y")
            os.system("apt install wireshark -y")
            os.system("pkg install cowsay -y")
            os.system("pkg install toilet -y")
            os.system("pkg install ruby -y")
            os.system("pkg install help -y")
            os.system("gem install lolcat -y")
            os.system("pkg install curl -y")
            os.system("pkg install wgetrc -y")
            os.system("pkg install unzip -y")
            os.system("pkg install openssh -y")
            os.system("pkg install tor -y")
            os.system("pkg install zip -y")
            os.system("pkg install net-tools -y")
            os.system("pkg install unrar -y")
            os.system("pkg install clang -y")
            os.system("pkg install w3m -y")
            os.system("pkg install proot -y")
            os.system("pip2 install wegt -y")
            os.system("pip2 install requests -y")
            os.system("pkg install sl -y")
            os.system("apt update && apt upgrade && pkg update && pkg upgrade -y")
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
