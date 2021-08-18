from bs4 import BeautifulSoup
import requests

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dongsuh.settings")
import django
django.setup()
from main.models import Post

def create_Soup(url): 
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup

def crawled_Dongsuh():
    url = "https://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=019012&nac_inbc=19&nac_inbs=%EB%A9%94%EC%9D%B8%EB%8C%80_best_1023"
    soup = create_Soup(url)
    items = soup.find("div", {'class':'item_gallery_type'}).find_all('li', limit = 8)
    for_link_url = "https://www.dongsuhfurniture.co.kr"

    result = []

    for i, item in enumerate(items):
        furniture_Name = item.find("div", {"class":"item_tit_box"}).get_text().strip()
        furniture_Link = item.find("div", {"class":"item_tit_box"}).find("a")["href"]
        sale_Percentage = item.find("span", {"class":"sale_text"}).get_text().strip()
        current_Price = item.find("strong", {"class":"item_price"}).get_text().strip()
        previous_Price = item.find("del").get_text().strip()
        furniture_Img = item.find("img", {"class":"middle"})["src"]
        print(for_link_url + furniture_Img)
        
        furniture_obj = {
            'furniture_Name' : furniture_Name,
            'furniture_Link' : for_link_url + furniture_Link[2:],
            'sale_Percentage' : sale_Percentage,
            'current_Price' : current_Price,
            'previous_Price' : previous_Price,
            'furniture_Img' : for_link_url + furniture_Img
        }
#         'furniture_Img' : for_link_url + furniture_Img
        

        result.append(furniture_obj)
    return result

if __name__ == "__main__":
    result_Craw = crawled_Dongsuh()
    for item in result_Craw:
        Post(furniture_Name = item['furniture_Name'],\
            furniture_Link = item['furniture_Link'],\
            sale_Percentage = item['sale_Percentage'],\
            current_Price = item['current_Price'],\
            previous_Price = item['previous_Price'],\
            furniture_Img = item['furniture_Img']).save()
        
        # furniture_Img = item['furniture_Img']


