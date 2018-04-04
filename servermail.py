def mail():
    count=int(input('enter how many friends to send mail: \n'))
    subject=input('enter subject: \n')
    message=input('enter message: \n')
    emails=[]#mail ids of friends
    friends=[]#names of friends
    for i in range(0,count):
        mail=input('enter friend mail:  ')
        name=input('enter friend name: ')
        emails.append(mail)
        friends.append(name)
    import smtplib#simple mail transfer protocol
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()#transport layer security
    server.login('madhavakoti45@gmail.com','**********')
    for friend in range(0,len(friends)):
        server.sendmail('madhavakoti45@gmail.com',emails[friend],subject,message)
        print('success')
    server.quit()
mail()
    
