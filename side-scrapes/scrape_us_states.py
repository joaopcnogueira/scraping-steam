import requests
import lxml.html

html = requests.get('https://en.wikipedia.org/wiki/U.S._state')
doc = lxml.html.fromstring(html.content)

# pegando os estados
div_states = doc.xpath('//div[@class="div-col"]')[0]
states = div_states.xpath('.//a/text()')

print(states)
