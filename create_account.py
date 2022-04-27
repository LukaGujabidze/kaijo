from logging import root
from os import access
from tkinter import Tk, Canvas, simpledialog, messagebox, Button
import forgot_password as fp
import hashlib

account = {}

def forgot_password(mail, username):
    pass_valid = False
    while pass_valid == False:
        fp.send_mail(mail)
        sent_pass = simpledialog.askstring('forgot password', 'the password will send on your account , please type password here:')
        if sent_pass == fp.mssgf:
            pass_valid = True
            new_pass = simpledialog.askstring('new password','Type your new password here: ').encode('UTF-8')
            with open('Accounts.txt','a') as file:
                file.write('\n' + mail + '/' + username + '/' + hashlib.sha512(new_pass).hexdigest())
                file.close()
                return
        else:
            pass_valid = False
                
            messagebox.showerror('incorrect password', 'you had typed incorrect password')
            sent_pass = simpledialog.askstring('forgot password', 'resend?')
            if sent_pass == 'yes':
                fp.send_mail(mail)
                sent_pass = simpledialog.askstring('forgot password', 'the password will send on your account , please type password here:')
            else:
                return    


def create_account():
    mail = simpledialog.askstring('Create Account', 'Type your Email: ')
    username = simpledialog.askstring('Create Account', 'Type your username: ')
    password = simpledialog.askstring('Create Account', 'Type your password: ').encode('UTF-8')

    with open('Accounts.txt','a') as file:
        file.write('\n' + mail + '/' + username + '/' + hashlib.sha512(password).hexdigest())
        file.close()

    account[username] = password
def sign():
    mail = simpledialog.askstring('sign in Account', 'Type your Email: ')
    username = simpledialog.askstring('sign in Account', 'Type your username: ')
    password = simpledialog.askstring('sign in Account', 'Type your password: if you forgot your password please type "forgot password"')
    if password == 'forgot password':
        forgot_password(mail, username)
        return
    
    
    
    

    if username in account and mail:
        messagebox.showinfo(username, 'you are in your account ')
    else:
        messagebox.showerror('incorrect account', 'whe haven\'t found your account! ')        




root = Tk()
root.withdraw()



while True:
    user_input = simpledialog.askstring('What to do? ', 'sign in or create account or finish program? ')
    if user_input.lower() == 'create account':
        create_account()
    elif user_input.lower() == 'sign in':
        sign()
    else:
        break        

root.mainloop()