import password_gen as pg
import smtplib



def message():
    global mess
    mess = pg.func()
    return mess

mssgf = message()   


def send_mail(mail):
    import smtplib, ssl

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "druncha.fum@gmail.com"
    receiver_email = mail
    with open('pass.txt', 'r') as file:
        password = file.read()
    

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, mssgf)





