import requests
import lxml.html

html = requests.get('https://store.steampowered.com/explore/new/')
doc = lxml.html.fromstring(html.content)

# pegando o conteúdo da aba Lançamentos populares
new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]

# pegando os títulos dos jogos
titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')

# pegando os preços dos jogos
prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')

# pegando as classificações dos jogos
tags_divs = new_releases.xpath('.//div[@class="tab_item_top_tags"]')
tags = [div.text_content() for div in tags_divs]
tags = [tag.split(', ') for tag in tags]

# pegando a plataforma dos jogos
platforms_div = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []

for game in platforms_div:
    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    platforms = [t.get('class').split(' ')[-1] for t in temp]
    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')
    total_platforms.append(platforms)

# retornando os dados em um json
output = []
for info in zip(titles, prices, tags, total_platforms):
    resp = {}
    resp['title'] = info[0]
    resp['price'] = info[1]
    resp['tags'] = info[2]
    resp['platforms'] = info[3]
    output.append(resp)

print(output)
