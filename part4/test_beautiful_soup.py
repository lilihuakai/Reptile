from bs4 import BeautifulSoup


# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# """
# html = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
#         <p class="story">...</p>
# """
# html = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#         </p>
#         <p class="story">...</p>
# """
# html = """
# <html>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#             Hello
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
# """
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')
# CSS选择器
for li in soup.select('li'):
    print('Get text:', li.get_text())
    print('String:', li.string)
# print(soup.select('.panel .panel-body'))
# print(soup.select('ul li'))
# print(soup.select('#list-2 .element'))
# print(type(soup.select('#list-2 .element')[0]))

# find()
# print(soup.find(attrs={'id': "list-1"}))
# print(soup.find(name='ul'))
# print(type(soup.find(name='ul')))
# print(soup.find(class_='list'))


# find_all()
# print(soup.find_all(attrs={'id': "list-1"}))
# print(soup.find_all(attrs={'name': "elements"}))
# print(soup.find_all(name='ul'))
# print(type(soup.find_all(name='ul')[0]))
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
#     for li in ul.find_all(name='li'):
#         print(li.string)


# print('Next Sibling', soup.a.next_sibling)
# print('Next Sibling', soup.a.next_sibling.string)
# print('Prev Sibling', soup.a.previous_sibling)
# print('Next Sibling', list(enumerate(soup.a.next_siblings)))
# print('Prev Sibling', list(enumerate(soup.a.previous_siblings)))
# print(type(soup.a.parents))
# print(list(enumerate(soup.a.parents)))
# print(soup.a.parent)
# for i, child in enumerate(soup.p.descendants):
# for i, child in enumerate(soup.p.children):
    # print(i, child)
# print(soup.p.contents)
# print(soup.head.title)
# print(type(soup.head.title))
# print(soup.head.title.string)
# soup = BeautifulSoup('<p>Hello</p>', 'lxml')
# print(soup.title.name)
# print(soup.title)
# print(type(soup.title))
# print(soup.prettify)
# print(soup.title.string)
# print(soup.head)
# print(soup.p)
# print(soup.p['class'])
# print(soup.p['name'])
# print(soup.p.attrs)
# print(soup.p.attrs['name'])
# print(soup.p.string)
