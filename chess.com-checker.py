import requests
from bs4 import BeautifulSoup

username = input("Enter username: ")
print('Username: ' + username)
profile_url = 'https://www.chess.com/member/' + username
profile_page = requests.get(profile_url)
soup = BeautifulSoup(profile_page.content, 'lxml')
name = soup.find('div', {'class': 'profile-card-info'})
print('Name: ' + str(name.contents[1].text))

email_url = 'https://www.chess.com/callback/recover-password-data/' + username
email_page = requests.get(email_url)
soup2 = BeautifulSoup(email_page.content, 'lxml')
email = soup2.p
print(email.text)