import imaplib, email, json, smtplib, sys, mimetypes, os, datetime
import update_pelican
from email.mime.text import MIMEText
from PyEmailWatcher.pyemailwatcher.pyemailwatcher import Watcher

def read_config():
	dir = os.path.dirname(os.path.realpath(__file__))
	with open(os.path.join(dir, 'config.json')) as fp:
		config = json.loads(fp.read())
	login = config['login']
	
	mail = Watcher(login['username'], login['password'], login['imap_server'], 
		login['smtp_server'], confirm_from="PelicanReceiver")
	
	return mail

def new_location(email):
	return update_pelican.location(email['subject'].replace("Location: ", ''))

def new_post(email):

	title = email['subject'].replace("Post: ", '')
	body = None
	if email.get_content_maintype() == 'multipart':
		for part in email.walk():
			if part.get_content_maintype() == 'multipart':
				pass
			elif part.get_content_maintype() == 'text':
				if body: continue
				body = part.get_payload(None, True)
			elif part.get_content_maintype() == 'image':
				filename = part.get_filename()
				with open(os.path.join('../content/images', filename), 'wb') as img:
					img.write(part.get_payload(decode=True))
				mdfilename = '![ ](images/%s)' % filename

	return update_pelican.post(title, body, mdfilename)


def main():	
	mail = read_config()
	mail.connect()
	all_messages = mail.check_inbox()
	for q, func in {"Location: ":new_location, "Post: ":new_post}.items():
		results = mail.search(q)
		for e in results:
			uid, email = e
			confirm = func(email)
			if confirm:
				mail.confirm(uid, email)
	mail.logout()

if __name__ == '__main__':
	
	main()