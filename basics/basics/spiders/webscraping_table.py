from logging.config import dictConfig
from http import request
import requests, json, logging
from bs4 import BeautifulSoup

class WebScraping:
    def __init__(self, url):
        self.url = url
    
    def web_scraping(self):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        dictionary = {}
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        league_table = soup.find('table', class_ = 'standing-table__table callfn')
        for team in league_table.find_all('tbody'):
            rows = team.find_all('tr')
            for row in rows:
                p1_team = row.find('td', class_ = 'standing-table__cell standing-table__cell--name').text.strip()
                p1_points = row.find_all('td', class_ = 'standing-table__cell')[9].text
                print(p1_team, p1_points)
                dictionary.update({p1_team:p1_points})

        with open('output.json', 'w') as outfile:
            json.dump(dictionary, outfile)
        
        logger.info("returns all the scraped data from the selected columns in the table present in the website.")

def main():
    object = WebScraping('https://www.skysports.com/premier-league-table')
    object.web_scraping()

if __name__ == '__main__':
    main()