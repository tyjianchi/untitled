import re
str_bk_url1 = str((u'中').encode('utf8'))
str_bk_url2 = (u'中'.encode('utf8'))
str_all=re.compile(str_bk_url2,re.S)
str_bk_url3=str_bk_url2.decode('utf8')
str_ma=re.match(str_all,str_bk_url1)

print(str_ma)