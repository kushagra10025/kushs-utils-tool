import src.globals as glbs
import requests
from bs4 import BeautifulSoup
import smtplib

class PriceTracker:
	def __init__(self,URL = glbs.default_url_link, expected_price=glbs.default_expected_fallen_price, sender_email = glbs.default_sender_email, sender_password = glbs.deafult_sender_password, receiver_email = glbs.default_receiver_email):
		self.headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
		self.URL = URL
		self.expected_price = expected_price
		self.sender_email = sender_email
		self.sender_password = sender_password
		self.receiver_email = receiver_email

	def send_mail(self):
		try:
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.ehlo()
			server.starttls()
			server.ehlo()
			server.login(self.sender_email,self.sender_password)

			subject = 'Low price alert !!'
			body = f'hey there user!\nwe have tracked your product and the prices have fallen down!!\ncheck the amazon link ->\n' + self.URL
			msg = f"Subject : {subject}\n\n{body}"

			server.sendmail(self.sender_email,self.receiver_email,msg)
			print('message has been sent')

			server.quit()
		except smtplib.SMTPException as e:
			print("SMTP Exception")
			print("Try turning on less secure apps for your google account!")

	def check_price(self):
		page = requests.get(self.URL, headers=self.headers)
		soup = BeautifulSoup(page.content, 'html.parser')

		try:
			title = soup.find(id="productTitle").get_text()
			price = soup.find(id=glbs.default_priceblock_tag_id).get_text()
			a = price.replace("₹", '')
			a = a.replace(",", '')
			converted_price = float(a)
			exp_price = float(self.expected_price)
			if(converted_price < exp_price):
				self.send_mail()

			print(title.strip())
			print(a)

			if(converted_price < exp_price):
				self.send_mail()
		except AttributeError as a:
			print("Attribute not found")


# check_price()