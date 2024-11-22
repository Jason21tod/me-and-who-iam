import requests
import bs4


def get_from_url(url):
    try:
        request_result = requests.get(url)
        print('looking for request result:', request_result.status_code)
        if request_result.status_code != 200:
            return False
        soup = bs4.BeautifulSoup(request_result.text, features='html.parser')
        return soup
    except:
        return False

def get_all_links(soup: bs4.BeautifulSoup):
    """Return the soup or a list with all the links"""
    links = []
    if soup != False:
        for link in soup.find_all('a'):
            hrefs = link.get('href')
            links.append(hrefs)
        return links
    else:
        return soup
    
def separate_all_links(links):
    """Divide the links in two categories 'external' and 'internal' """
    formated_links = {'external_links': [], 'internal_links': []}
    for link in links:
        if 'http' in link:
            formated_links['external_links'].append(link)
        else:
            formated_links['internal_links'].append(link)
    return formated_links

def get_all_images(soup: bs4.BeautifulSoup):
    imgs = soup.find_all('img')
    print(f'Found {len(imgs)} images')
    print(f'Found {imgs} images')
    
    return len(imgs)