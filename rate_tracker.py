import requests
import bs4
from datetime import date
from py_email import send_email


def main():
    r = requests.get('https://www.arvest.com/rates')
    r.raise_for_status()
    s = bs4.BeautifulSoup(r.text, 'html.parser')
    e = s.select(
        'body > main > div.row > div.col-main-right > div:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(3)')
    today_rate = float(e[0].text[:-1])
    with open('rate_history.csv','r') as f_in:
        lines = f_in.readlines()
        yesterday_rate = float(lines[-1].split(',')[-1])
    today = date.today().strftime('%Y%m%d')
    with open('rate_history.csv', 'a') as f_out:
        f_out.write(f'{today},{today_rate}\n')
    if today_rate != yesterday_rate:
        subj = f'The mortgage rate has changed.\n'
        body = (f'Today: {today_rate}\n'
                f'Yesterday: {yesterday_rate}')
        send_email(subj, body)


if __name__ == '__main__':
    main()
