from lxml import etree


text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*[2]')
print(result)
result = html.xpath('//li[1]/following-sibling::*')
# result = html.xpath('//li[1]/a/text()')
# print(result)
# result = html.xpath('//li[last()]/a/text()')
# print(result)
# result = html.xpath('//li[position()<3]/a/text()')
# print(result)
# result = html.xpath('//li[last()-2]/a/text()')
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
# result = html.xpath('//li[contains(@class, "li")]/a/text()')
# result = html.xpath('//li/a/@href')
# result = html.xpath('//li[@class="item-0"]//text()')
# result = html.xpath('//li[@class="item-0"]/a/text()')
# result = html.xpath('//li[@class="item-0"]/text()')
# result = html.xpath('//li[@class="item-0"]')
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
# result = html.xpath('//a[@href="link4.html"]/../@class')
# result = html.xpath('//ul//a')
# result = html.xpath('//li/a')
# result = html.xpath('//li')
# result = html.xpath('//*')
print(result)
# print(result[0])
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))



