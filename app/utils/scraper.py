import gzip

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


def scrape_performance(symbol: str):
    url = f"https://www.marketwatch.com/investing/stock/aapl"
    headers = {
        "Sec-Ch-Ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"', 
        "Sec-Ch-Ua-Mobile": "?0", 
        "Sec-Ch-Ua-Platform": '"Linux"', 
        "Upgrade-Insecure-Requests": "1", 
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36", 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1", 
        "Sec-Fetch-Dest": "document", 
        "Accept-Encoding": "gzip, deflate, br, zstd", 
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7", 
        "Priority": "u=0, i"}

    req = Request(url, headers=headers)
    response = urlopen(req)
    if response.status != 200:
        raise ValueError(f"Erro ao acessar a página para {symbol}")

    html = response.read()
    decoded_data = gzip.decompress(html).decode('utf-8')
    soup = BeautifulSoup(decoded_data, 'html.parser')

    performance_data = {}
    performance_section = soup.find(
        "table",
        class_="table table--primary no-heading c2"
    )
    if not performance_section:
        raise ValueError(f"Seção de desempenho não encontrada para {symbol}")

    if performance_section:
        rows = performance_section.find_all('tr', class_='table__row')
        for row in rows:
            key = row.find('td', class_='table__cell').get_text(strip=True)
            
            value_item = row.find('li', class_='content__item value ignore-color')
            value = value_item.get_text(strip=True) if value_item else None

            performance_data[key] = value

    return performance_data
