from bs4 import BeautifulSoup
import requests, json

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

def get_organic_results():
    html = requests.get('https://www.ebay.com/sch/i.html?_nkw=Dior%20Saddle%20Bag&_sop=10&rt=nc&_udhi=1500').text
    soup = BeautifulSoup(html, 'lxml')

    data = []
    for item in soup.select('.s-item__wrapper.clearfix'):
        title = item.select_one('.s-item__title').text
        link = item.select_one('.s-item__link')['href']

        try:
            price = item.select_one('.s-item__price').text
        except:
            price = None

        try:
            image = item.select_one('.s-item__image-wrapper img')['src']
        except:
            image = None

        data.append({
            'item': {'title': title, 'link': link, 'price': price, 'image': image},

        })

    print(json.dumps(data, indent = 2, ensure_ascii = False))


get_organic_results()
