import os

def menu():
    
    os.system('printf "\033[3;36m"') 
    os.system('figlet GBasics')

    print("""                               
=======================================
BY: Glitch
=======================================
Telegram : @B4H09
=======================================
Gmail : b4h09.Hack.gmail.com
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
            os.system("gem install golang -y")
            os.system("gem install host -y")
            os.system("apt install nano -y")
            os.system("gem install havij -y")
            os.system("gem install hydra -y")
            os.system("gem install wireshark -y")
            os.system("pkg install figlet -y")
            os.system("gem install wget -y")
            os.system("pkg install cowsay -y")
            os.system("pkg install toilet -y")
            os.system("pkg install ruby -y")
            os.system("gem install help -y")
            os.system("gem install lolcat -y")
            os.system("pkg install curl -y")
            os.system("gem install wgetrc -y")
            os.system("pkg install unzip -y")
            os.system("gem install openssh -y")
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
            os.system("pkg install unstable-repo")
            os.system("pkg install x11-repo")
            os.system("pkg install root-repo")
            os.system("pkg install proot")
            os.system("gem install bundle")
            os.system("gem install bundler")
            os.system("pip install --upgrade pip")
            os.system("pip install pip")
            os.system("pip install --upgrade pip")
            os.system("pip2 install pip")
            os.system("pip3 install pip")
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
