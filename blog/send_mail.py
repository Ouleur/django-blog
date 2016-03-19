import smtplib
 
def mail_send():

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("ouleur000@gmail.com", "dev=dev#")
	 
	msg = "YOUR MESSAGE!"
	server.sendmail("ouleur000@gmail.com", "jean-marie.adou@smile.ci", msg)
	server.quit()