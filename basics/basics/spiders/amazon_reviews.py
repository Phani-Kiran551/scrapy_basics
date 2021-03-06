from logging import raiseExceptions
import requests, logging
from bs4 import BeautifulSoup
from csv import DictWriter

class AmazonReviews:
    def __init__(self, url, review_list):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        self.url = url
        self.review_list = review_list
        logger.info("function for declaring all the required variables in the class.")


    def get_soup(self):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        r = requests.get('http://localhost:8050/render.html', params = {'url': self.url})
        soup = BeautifulSoup(r.text, 'html.parser')
        logger.info("returns the html tags obtained from the url given through an object named soup.")
        return soup

    def get_reviews(self, soup):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        reviews = soup.find_all('div', {'data-hook': 'review'})
        field_names = ['product','title','rating','body']
        try:
            for item in reviews:
                
                review = {
                'product': soup.title.text.replace('Amazon.in:Customer reviews: ', ''),
                'title' : item.find('a', {'data-hook': 'review-title'}).text.strip(),
                'rating' : float(item.find('i',{'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
                'body' : item.find('span', {'data-hook': 'review-body'}).text.strip(),
                }
                
                try:
                    with open('basics/basics/reviews.csv', 'a') as f_object:
                        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
                        dictwriter_object.writerow(review)
                        f_object.close()
                except:
                    print('Cannot open the file reviews.csv')

        except:
            print('Could not find any reviews.')
        logger.info("Saves the reviews of each customers in event.csv file.")

def main():
    object = AmazonReviews('https://www.amazon.in/Akatsuki-Cosplay-Village-Costume-Accessory/product-reviews/B01NGT5HYO/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews', [])
    get_soup_tags = object.get_soup()
    object.get_reviews(get_soup_tags)

if __name__ == '__main__':
    main()