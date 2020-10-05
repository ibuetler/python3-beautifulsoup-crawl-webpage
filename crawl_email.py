from bs4 import BeautifulSoup
import requests

url = 'https://deutschschweiz.swisswine.ch/de/produzent?page=1'
response = requests.get(url)

html = BeautifulSoup(response.text, 'html.parser')

def get_this_page_emails(html):
    email_list = []
    emails = html.find_all('li', {'class': 'email'})
    for email in emails:
        try:
            email_link = email.find('span')
            email_text = email_link.text
        except Exception as e:
            continue

        email_list.append(email_text)
    return email_list

def get_all_emails(html):
    pagenumber = 2
    email_list = get_this_page_emails(html)
    end = False
    while not end:
        if pagenumber == 55:
            end = True
        next_url = 'https://deutschschweiz.swisswine.ch/de/produzent?page='+str(pagenumber)
        next_response = requests.get(next_url)
        next_html = BeautifulSoup(next_response.text, 'html.parser')
        temp = get_this_page_emails(next_html)
        email_list += temp
        pagenumber += 1

    return email_list


email_list = get_all_emails(html)

def create_CSV_file_emails(list):

    with open('emails.csv', 'w') as csv_file:
        for entry in list:
            csv_file.write(entry)
            csv_file.write('\n')



create_CSV_file_emails(email_list)