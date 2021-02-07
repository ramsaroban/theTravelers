from django.core.mail import EmailMessage
class Utils:
	@staticmethod
	def send_mail(data):
		try:
			email = EmailMessage(subject=data['email_subject'],
			body=data['email_body'],to=[data['to_email']])
			email.send()
			print('a try')
		except Exception as e:
			print(e,'---------------')



class UserDoesNotExistsException(Exception):
    '''
    Raise this if User doesnt exist!
    '''
    pass