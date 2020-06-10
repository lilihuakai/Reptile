from pyquery import PyQuery as pq


html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
# html = '''
# <div class="wrap">
#     Hello, World
#     <p>This is a paragraph.</p>
#  </div>
# '''


doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(second)')
print(li)


# remove()
# wrap = doc('.wrap')
# wrap.find('p').remove()
# print(wrap.text())


# attr(),text(),html()
# li = doc('.item-0.active')
# print(li)
# li.attr('name', 'link')
# print(li)
# li.text('change item')
# print(li)
# li.html('<span>Change item</span>')
# print(li)


# addClass() removeClass()
# li = doc('.item-0.active')
# print(li)
# li.removeClass('active')
# print(li)
# li.addClass('active')
# print(li)


# a = doc('a')
# a = doc('.item-0.active a')
# print(a, type(a))
# print(a.attr('href'))
# print(a.attr.href)
# print(a.text())
# print(a.html())
# li = doc('.list .item-0.active')
# lis = doc('li').items()
# print(lis)
# for li in lis:
    # print(li, type(li))
# print(li)
# print(str(li))
# print(li.siblings('.active'))
# print(li.siblings())
# items = doc('.list')
# print(items)
# print(type(items))
# lis = items.parents()
# lis = items.parent()
# lis = items.children('.active')
# lis = items.children()


# find()
# lis = items.find('li')
# print(lis)
# print(type(lis))


# doc = pq(filename='demo.html')
# doc = pq(url='https://cuiqingcai.com')
# print(doc('#container .list li'))
# print(type(doc('#container .list li')))
# print(doc('title'))
# print(doc('li'))
