import smtplib

email, password= "xyz123@gmail.com", "password"
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(email,password)
massage="model is trained with accuracy more than 85%"
s.sendmail("xyz123@gmail.com","xyz123@gmail.com",massage)
print(massage)
s.quit()
