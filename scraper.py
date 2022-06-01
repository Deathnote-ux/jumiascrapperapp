from bs4 import BeautifulSoup
import requests

base_url = 'https://www.jumia.com.ng'
html = '''
<!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.min.css') }}">
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
        <title>Scraper App - Result Index</title>
      </head>
      <body>
        <div class="table-responsive" style="width: 70%; margin-left: 15%;">
          <h1 style="margin-top: 20px; margin-bottom: 20px;">
            {{ type }}
            <a class="btn btn-lg btn-primary" href="{{ request.referrer }}" style="float: right;">Back To Homepage</a>
          </h1>
          <table class="table table-striped table-bordered" >
            <tr>
              <th>
              Name
              </th>
              <th>
              Price (₦)
              </th>
              <th>
              Link
              </th>
            </tr>
          </table>
        </div>
      </body>
    </html> 
'''


def get_phones(min_price, max_price):
    # url to the page where data is to be scraped
    url = 'https://www.jumia.com.ng/smartphones/?price_discount=50-100'

    # continue with the required code here
    page = requests.get(url).text
    doc = BeautifulSoup(page, 'html.parser')
    soup_1 = BeautifulSoup(html, 'html.parser')

    p_names = doc.find_all(class_=('info'))
    for p_name in p_names:
        name_td = p_name.h3.string
        if name_td is None:
            continue
        else:
            td_name = soup_1.new_tag('td')
            td_name.append(name_td)
            tr = soup_1.new_tag('tr')
            tr.append(td_name)
            soup_1.table.append(tr)

    p_prices = doc.find_all(class_=('prc'))
    for p_price in p_prices:
        price_td = p_price.string
        if price_td is None:
            continue
        elif min_price >= price_td and max_price <= price_td:
            td_price = soup_1.new_tag('td')
            td_price.append(price_td)
            tr = soup_1.new_tag('tr')
            tr.append(td_price)
            soup_1.table.append(tr)

    p_links = doc.find_all("article", {"class": "prd _fb col c-prd"})
    for p_link in p_links:
        link_p = p_link.find("a", {"class": "core"}).get('href')
        td_link = soup_1.new_tag('td')
        link_a = soup_1.new_tag('a', href=f"{link_p}")
        td_link.append(link_a)
        tr = soup_1.new_tag('tr')
        tr.append(td_link)
        soup_1.table.append(tr)

    # end by writing the updated HTML to file
    with open('templates/product_index.html', 'w', encoding="utf-8") as html_file:
        html_file.write(soup_1.prettify())  # you can always change 'soup_1' to your desired variable name


def get_electronics(min_price, max_price):
    # url to the page where data is to be scraped
    url = 'https://www.jumia.com.ng/electronics/'
    # continue with the required code here
    page = requests.get(url).text
    doc = BeautifulSoup(page, 'html.parser')
    soup_1 = BeautifulSoup(html, 'html.parser')

    for e_name in e_names:
        ename_td = e_name.string
        if ename_td is None:
            continue
        else:
            # td = soup_1.new_tag('td')
            # td.string = name_td
            etd_name = soup_1.new_tag('td')
            etd_name.append(ename_td)
            tr = soup_1.new_tag('tr')
            tr.append(etd_name)
            soup_1.table.append(tr)

    e_prices = doc.find_all(class_=('prc'))
    for e_price in e_prices:
        eprice_td = e_price.string
        if eprice_td is None:
            continue
        elif min_price >= eprice_td and max_price <= eprice_td:
            etd_price = soup_1.new_tag('td')
            etd_price.append(eprice_td)
            tr = soup_1.new_tag('tr')
            tr.append(etd_price)
            soup_1.table.append(tr)

    e_links = doc.find_all("article", {"class": "prd _box _hvr"})
    for e_link in e_links:
        elink_td = e_link.find("a", {"class": "core"}).get('href')
        etd_link = soup_1.new_tag('td')
        elink_a = soup_1.new_tag('a', href=f"{elink_td}")
        etd_link.append(elink_a)
        tr = soup_1.new_tag('tr')
        tr.append(etd_link)
        soup_1.table.append(tr)

    # end by writing the updated HTML to file
    with open('templates/product_index.html', 'w', encoding="utf-8") as html_file:
        html_file.write(soup_1.prettify())  # you can always change 'soup_1' to your desired variable name
