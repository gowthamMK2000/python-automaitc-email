import csv,email, smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart  import MIMEMultipart

port = 465
smtp_server = 'smtp.gmail.com'
sender_email = ""

password = ""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server,port, context=context) as server :
	server.login(sender_email,password)
	with open("contact.csv") as file:
		reader = csv.reader(file)
		next(reader)
		for email,name in reader:
			print(email)
			message = MIMEMultipart("alternative")
			message["Subject"] = "Multipart test and csv  "
			message["From"] = "<MK>"
			message["To"] = email
			text = """\
Greetings from  team,

We , the  ,
Coimbatore Institute of Technology conducting a National Level Technical
Symposium on September 19 and September 20 2018.Workshops, Paper
Presentations and various Technical events and Non Technical events will be
conducted.

For paper presentation any technical topics are welcomed and
open for all the departments.Kindly send the abstracts before September 15.
"Ethical hacking" workshop will be conducted on September 19

and "Artificial Intelligence and Deep learning" on September 20.
We are glad to welcome your "Government College of
Technology" students to participate in this event to gain knowledge and
experience
For Further Details visit:

website:http://
Facebook:
Instagram:

Kindly Forward this to all the departments in your college
This  mail has been sent for testing purpose(text content) (unofficial)

"""
			ahtml = """\
<html> 
	<body>
		<h5>Email  automation testing</h5>
		<h4>Id:{aname}</h4>
		<h3>age:{age}</h3>
	<p>									
			We , the Department of  ,
			Coimbatore Institute of Technology conducting a National Level Technical
			Symposium on September 19 and September 20 2018.Workshops, Paper
			Presentations and various Technical events and Non Technical events will be
			conducted.
		</p>
		<p>
			For paper presentation any technical topics are welcomed and
			open for all the departments.Kindly send the abstracts before September 15.
			"" workshop will be conducted on September 19
		</p>
		<p>
			and "" on September 20.
			We are glad to welcome your "Government College of
			Technology" students to participate in this event to gain knowledge and
			experience
			For Further Details visit:
		</p>
		<p>
			website:http://
			Facebook
			Instagram
		</p>
		<p>
			Kindly Forward this to all the departments in 
 college
		</p>
		<footer>This  mail has been sent for testing purpose(html content) (unofficial)</footer>
	</body>
</html>
"""
			html = ahtml.format(aname=name,age=age)
                      
			part1 = MIMEText(text, "plain") 
			part2 = MIMEText(html, "html")
                      
			message.attach(part1)
			message.attach(part2)
			try:	
				server.sendmail(sender_email,email,message.as_string())
			except :
				print("failed",email)


