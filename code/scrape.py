import pickle
import requests
from bs4 import BeautifulSoup

BASE = 'http://www.tdcj.state.tx.us/death_row/'
TABLE = 'dr_executed_offenders.html'

def get_links():
    r = requests.get(BASE + TABLE)
    soup = BeautifulSoup(r.text)
    a_tags = soup.find_all('a')
    hrefs = []
    for a in a_tags:
        if a.text == 'Last Statement':
            hrefs.append(a['href'])
    return hrefs

def get_statement(hrefs):
    statements = []
    for href in hrefs:
        url = BASE + href
        r = requests.get(url)
        print 'requesting', url
        soup = BeautifulSoup(r.text)
        this_statement = []
        p_tags = soup.findAll('p')
        for i, p in enumerate(p_tags):
            if p.text == 'Last Statement:':
                # this_statement.append([pt.text for pt in p_tags[(i + 1):]])
                # this_statement.extend(soup.find('.body').text)
                statements.append(p.findParent().text)
    return statements

if __name__ == '__main__':
    hrefs = get_links()
    statements = get_statement(hrefs)
    cleaned = [s.split('Last Statement:')[1] for s in states]
    pickle.dump(cleaned, open('last_statements', 'wr'))
