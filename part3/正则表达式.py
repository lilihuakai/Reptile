import re


html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''


# compile()
content1 = "2016-12-15 12:00"
content2 = "2016-12-17 12:55"
content3 = "2016-12-22 13:21"
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)


# sub()
# content = '54ak54yr5oiR54ix5L2g'
# content = re.sub('\d+', '', content)
# print(content)


# findall()
# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(results)

# search()
# content = "Extra stings Hello 1234566 World_This is a Regex Demo Extra stings"
# result = re.search('Hello.*?(\d+).*?Demo', content)
# print(result)



# match()
# 使.匹配包括换行在内的所有字符
# content = '''Hello 1234567 World_This
# is a Regex Demo
# '''
# result = re.match('^Hello.*Demo$', content, re.S)
# print(result)

# content = "Hello 123 4566 World_This is a Regex Demo"
# # content = "Hello 123 4567 World_This is a Regex Demo"
# # print(len(content))
# result = re.match('^Hello.*Demo$', content)
# # result = re.match('^Hello\s(\d+)\sWorld', content)
# # result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group())
# # print(result.group(1))
# print(result.span())
