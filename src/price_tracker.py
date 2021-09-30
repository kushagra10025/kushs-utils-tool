import requests
from bs4 import BeautifulSoup
import smtplib

URL = input("enter the product link to be tracked : ")
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

e_price = float(input("enter the expected fallen price : "))

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_dealprice").get_text()
    a = price.replace("₹", '')
    b = a.replace(",", '')
    converted_price = float(b)

    if(converted_price < e_price):
        send_mail()

    print(title.strip())
    print(b)

    if(converted_price < e_price):
        send_mail()

s_email = input("enter the sender's email : ")
s_password = input("enter the password : ")
r_email = input("enter reciever's email : ")

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(s_email, s_password)

    subject = 'Low price alert !!'
    body = f'hey there user!\nwe have tracked your product and the prices have fallen down!!\ncheck the amazon link ->\n' + URL
    
    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail('kartik.dhasmana001@gmail.com',r_email,msg)
    print('message has been sent')

    server.quit()

check_price()