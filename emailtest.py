import csv,email, smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart  import MIMEMultipart

port = 465
smtp_server = 'smtp.gmail.com' 
#add senders email
sender_email = "" 
#ass password // for privacy issues you can input through command line
password = ""

#for encryption
context = ssl.create_default_context()

#creates a secure connection with Gmail’s SMTP server
with smtplib.SMTP_SSL(smtp_server,port, context=context) as server :
	server.login(sender_email,password)
	with open("contact.csv") as file:
		reader = csv.reader(file)
		next(reader)
		for email,name,age in reader:
			print(email)
			message = MIMEMultipart("alternative")
			message["Subject"] = "Multipart test and csv  "
			message["From"] = "<MK>"
			message["To"] = email
			text = """\

Email automation testing
Name : {name}
Age : {age}

This  mail has been sent for testing purpose(text content) (unofficial)
"""
			html = """\
<html> 
	<body>
		<h5>Email  automation testing</h5>
		<h4>Name:{name}</h4>
		<h3>age:{age}</h3>
		<p> body </p>	
		<footer>This  mail has been sent for testing purpose(html content) (unofficial)</footer>
	</body>
</html>
"""
			text = text.format(name=name,age=age)
			html = html.format(name=name,age=age)
                      
			part1 = MIMEText(text, "plain") 
			part2 = MIMEText(html, "html")
                      
			message.attach(part1)
			message.attach(part2)
			try:	
				server.sendmail(sender_email,email,message.as_string())
			except :
				print("failed",email)


