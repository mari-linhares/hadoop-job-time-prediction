#Thank you : Nael Shiab
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from sys import argv

def sendMail(result, fromaddr, toaddr, fromaddr_mail_password, nodes, output_file_path):

	msg = MIMEMultipart()

	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = 'RESULT: Script result for ' + str(nodes)

	body = 'Experiment results for ' + str(nodes) +  '\n' + result

	msg.attach(MIMEText(body, 'plain'))

	filename = output_file_path
	attachment = open(output_file_path, 'rb')

	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

	msg.attach(part)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, fromaddr_mail_password)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
