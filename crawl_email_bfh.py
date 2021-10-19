from bs4 import BeautifulSoup
import requests

url = 'https://mcs.unibnf.ch/lecturers-list/page/1/'
response = requests.get(url)
print(url)

html = BeautifulSoup(response.text, 'html.parser')

def get_this_page_emails(html):
    email_list = []
    emails = html.find_all('a', {'class': 'lecturer-email'})
    for email in emails:
        try:
            # <a href="mailto: andreas.fischer@unifr.ch" class="lecturer-email">Email</a>
            href = email.get('href')
            str1, email_link = href.split(': ')
        except Exception as e:
            continue

        email_list.append(email_link)
    return email_list

def get_all_emails(html):
    pagenumber = 2
    email_list = get_this_page_emails(html)
    end = False
    while not end:
        if pagenumber == 5:
            end = True
        next_url = 'https://mcs.unibnf.ch/lecturers-list/page/'+str(pagenumber)+'/'
        print(next_url)
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
