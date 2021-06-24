#!/usr/bin/env python
# coding: utf-8

# # 1

# In[ ]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
tags = requests.get("http://en.wikipedia.org/wiki/Main_Page")
tags
soup = BeautifulSoup(tags.content)
headers = soup.find_all(['h1','h2','h3','h4','h5','h6'])
print(headers,end='\n')


# # 2

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
soup =BeautifulSoup(page.content)
n=[]
for i in soup.find_all('td',class_='titleColumn'):
    n.append(i.a.text)
r=[]
for i in soup.find_all('td',class_='ratingColumn imdbRating'):
    r.append(i.strong.text)
y=[]
for i in soup.find_all('td',class_='titleColumn'):
    y.append(i.span.text)
data={'Title':n,'Rating':r,'Year':y}
op=pd.DataFrame(data)
op.head(100).style.hide_index()


# # 3

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2e9dfa9b-3e4d-4d39-acd2-8af11f252a59&pf_rd_r=VS4ZWNSK7SEADXDZDNH2&pf_rd_s=right-5&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_india_tr_rhs_1')
soup =BeautifulSoup(page.content)
n=[]
for i in soup.find_all('td',class_='titleColumn'):
    n.append(i.a.text)
r=[]
for i in soup.find_all('td',class_='ratingColumn imdbRating'):
    r.append(i.strong.text)
y=[]
for i in soup.find_all('td',class_='titleColumn'):
    y.append(i.span.text)
data={'Title':n,'Rating':r,'Year':y}
op=pd.DataFrame(data)
op.head(100).style.hide_index()


# # 4

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://bookpage.com/reviews')
soup=BeautifulSoup(page.content)
a = soup.find_all('h4',class_='italic')
title,author,genere,bookreview =[],[],[],[]
for i in soup.find_all('h4','italic'):
    temp = i.text
    temp=temp.replace('\n',' ')
    title.append(temp)
for i in soup.find_all('p','sans bold'):
    temp = i.text
    temp=temp.replace('\n',' ')
    author.append(temp)
for i in soup.find_all('p',class_='genre-links hidden-phone'):
    temp = i.text
    temp=temp.replace('\n',' ')
    genere.append(temp)
for i in soup.find_all('p','excerpt'):
    temp = i.text
    temp=temp.replace('\n',' ')
    bookreview.append(temp)
    result={'Title':title,'Auother':author,'Genre':genere,'Review':bookreview}
op = pd.DataFrame(result)
op.head(5).style.hide_index()


# # 5(i)

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
soup=BeautifulSoup(page.content)
r,t,m,p,R=[],[],[],[],[]
for i in soup.find_all('span',class_='u-hide-phablet'):
    r.append(i.text)
for j in soup.find_all('td',class_='table-body__cell u-center-text'):
    t.append(j.text)
for i in range(0,len(t),2):
    m.append(t[i])
for i in range(1,len(t),2):
    p.append(t[i])
for i in soup.find_all('td','table-body__cell u-text-right rating'):
    R.append(i.text)
data = {'Country':r[0:19],'Matches':m,'Points':p,'Rating':R}
op=pd.DataFrame(data)
op.head(10).style.hide_index()


# # 5(ii)

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
soup=BeautifulSoup(page.content)
p,n,r=[],[],[]
for i in soup.find_all('td',class_='table-body__cell rankings-table__name name'):
    temp = i.text
    temp =temp.replace('\n','')
    p.append(temp)
for i in soup.find_all('span',class_='table-body__logo-text'):
    n.append(i.text)
for i in soup.find_all('td',class_='table-body__cell rating'):
    r.append(i.text)
a=min(len(p),len(r),len(n))
data={'PlayerName':p[:a],'Nationality':n[:a],'Ratting':r[:a]}
op=pd.DataFrame(data)
op.head(10).style.hide_index()


# # 5(iii)

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
soup=BeautifulSoup(page.content)
p,n,r=[],[],[]
for i in soup.find_all('td',class_='table-body__cell rankings-table__name name'):
    temp = i.text
    temp =temp.replace('\n','')
    p.append(temp)
for i in soup.find_all('span',class_='table-body__logo-text'):
    n.append(i.text)
for i in soup.find_all('td',class_='table-body__cell rating'):
    r.append(i.text)
a=min(len(p),len(r),len(n))
data={'PlayerName':p[:a],'Nationality':n[:a],'Ratting':r[:a]}
op=pd.DataFrame(data)
op.head(10).style.hide_index()


#  # 6(i)

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
soup=BeautifulSoup(page.content)
r,t,m,p,R=[],[],[],[],[]
for i in soup.find_all('span',class_='u-hide-phablet'):
    r.append(i.text)
for j in soup.find_all('td',class_='table-body__cell u-center-text'):
    t.append(j.text)
for i in range(0,len(t),2):
    m.append(t[i])
for i in range(1,len(t),2):
    p.append(t[i])
for i in soup.find_all('td','table-body__cell u-text-right rating'):
    R.append(i.text)
a=min(len(r),len(t),len(m),len(p))
data = {'Country':r[0:a],'Matches':m[0:a],'Points':p[0:a],'Rating':R[0:a]}
op=pd.DataFrame(data)
op.head(10).style.hide_index()


# # 6(ii)

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
soup=BeautifulSoup(page.content)
p,n,r=[],[],[]
for i in soup.find_all('td',class_='table-body__cell rankings-table__name name'):
    temp = i.a.text
    temp =temp.replace('\n','')
    p.append(temp)
for i in soup.find_all('span',class_='table-body__logo-text'):
    n.append(i.text)
for i in soup.find_all('td',class_='table-body__cell rating'):
    r.append(i.text)
a=min(len(p),len(r),len(n))
data={'PlayerName':p[:a],'Nationality':n[:a],'Ratting':r[:a]}
op=pd.DataFrame(data)
op.head(10).style.hide_index()


# # 6(iii)

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
soup=BeautifulSoup(page.content)
p,n,r=[],[],[]
for i in soup.find_all('td',class_='table-body__cell rankings-table__name name'):
    temp = i.a.text
    temp =temp.replace('\n','')
    p.append(temp)
for i in soup.find_all('span',class_='table-body__logo-text'):
    n.append(i.text)
for i in soup.find_all('td',class_='table-body__cell rating'):
    r.append(i.text)
a=min(len(p),len(r),len(n))
data={'PlayerName':p[:a],'Nationality':n[:a],'Ratting':r[:a]}
op=pd.DataFrame(data)
op.head(10).style.hide_index()


# # 7

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://www.amazon.in/s?bbn=1389401031&rh=n%3A1389401031%2Cp_36%3A1318506031&dc&qid=1624432003&rnid=1318502031&ref=lp_1389401031_nr_p_36_3')

code=page.status_code
print(code,'kindly update the url feild by providing link manually')
soup=BeautifulSoup(page.content)
m=[]
for i in soup.find_all('span',class_='a-size-base-plus a-color-base a-text-normal'):
    m.append(i.text)
r =[]
for i in soup.find_all('span',class_='a-icon-alt'):
    temp = i.text
    temp = temp[0:3]
    r.append(temp)
p=[]
for i in soup.find_all('span',class_='a-price-whole'):
    p.append(i.text)
i=[]
for t in soup.find_all('img',class_='s-image'):
    i.append(t['src'])
a=min(len(m),len(p),len(r),len(i))
data={'Mobile Details':m[0:a],'Price':p[0:a],'Rating out of 5':r[0:a],'URL of image':i[0:a]}
op=pd.DataFrame(data).fillna(0)
op
if code!= 200:
    print(f"AMAZON server provide error status code {code} Run agian")


# # 8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.YNLuYugzZPY')
soup =BeautifulSoup(page.content)
d=[]
for i in soup.find_all('div',class_='col-sm-2 forecast-label'):
    d.append(i.text)
dt=[]
for i in soup.find_all('div',class_='col-sm-10 forecast-text'):
    dt.append(i.text)
dc=[]
for i in soup.find_all('p',class_='short-desc'):
  dc.append(i.text)
t=[]
for i in soup.find_all('p',attrs={'temp temp-low','temp temp-high'}):
    t.append(i.text)
a=min(len(d),len(dt),len(dc),len(t))
data={'Period':d[0:a],'Short Description':dc[0:a],'Temperature':t[0:a],'Description':dt[0:a]}
op=pd.DataFrame(data)
op


# # 9

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://internshala.com/fresher-jobs')
soup =BeautifulSoup(page.content)
jo=[]
for i in soup.find_all('div',class_='heading_4_5 profile'):
    temp=i.text
    temp=temp.replace('\n','')
    jo.append(temp)
c=[]
for i in soup.find_all('div',class_='heading_6 company_name'):
    temp=i.text
    temp=temp.replace('\n','')
    temp=temp.replace(' ','')
    c.append(temp)
s,temp,j=[],[],[]
for i in soup.find_all('div',class_='item_body'):
    temp.append(i.text)
for i in range(1,len(temp),3):
    j.append(temp[i][:])
for i in j:
    temp=i.replace('\n','')
    temp=temp.replace(' ','')
    s.append(temp)
d,temp,j=[],[],[]
for i in soup.find_all('div',class_='item_body'):
    temp.append(i.text)
for i in range(2,len(temp),3):
    j.append(temp[i][:])
for i in j:
    temp=i.replace('\n','')
    temp=temp.replace(' ','')
    d.append(temp)
a=min(len(j),len(c),len(s),len(d))
data={'JobTitle':jo[0:a],'Company Name':c[0:a],'CTC':s[0:a],'ApplyDate':d[0:a]}
op=pd.DataFrame(data).style.hide_index()
op


# # 10

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://www.nobroker.in/property/sale/bangalore/multiple?searchParam=W3sibGF0IjoxMi45MzUxOTI5LCJsb24iOjc3LjYyNDQ4MDY5OTk5OTk5LCJwbGFjZUlkIjoiQ2hJSkxmeVkyRTRVcmpzUlZxNEFqSTd6Z1JZIiwicGxhY2VOYW1lIjoiS29yYW1hbmdhbGEifSx7ImxhdCI6MTIuOTc4MzY5MiwibG9uIjo3Ny42NDA4MzU2LCJwbGFjZUlkIjoiQ2hJSmtRTjNHS1FXcmpzUk5oQlFKcmhHRDdVIiwicGxhY2VOYW1lIjoiSW5kaXJhIE5hZ2FyIn0seyJsYXQiOjEyLjkzMDc3MzUsImxvbiI6NzcuNTgzODMwMiwicGxhY2VJZCI6IkNoSUoyZGRsWjVnVnJqc1JoMUJPQWFmLW9ycyIsInBsYWNlTmFtZSI6IkpheWFuYWdhciJ9XQ==&radius=2.0')
soup =BeautifulSoup(page.content)
n=[]
for i in soup.find_all('a',class_='nb__3CnI6'):
    n.append(i.attrs.get('title'))
ad=[]
for i in soup.find_all('div',class_='nb__2CMjv'):
    ad.append(i.text)
a,p,t,temp,f=[],[],[],[],[]
for i in soup.find_all('div',class_='font-semi-bold heading-6'):
    temp.append(i.span)
for i in range(2,len(temp),3):
    p.append(temp[i])
for i in range(0,len(p)):
    t.append(str(p[i]))
for i in t:
    tp=i.replace('<span>','')
    tp=tp.replace('</span>','')
    tp=tp.replace('<','')
    tp=tp.replace('-','')
    tp=tp.replace('>','')
    tp=tp.replace('!','')
    f.append(tp)
e,w=[],[]
for i in soup.find_all('div',class_='font-semi-bold heading-6'):
    w.append(i.text)
for i in range(1,len(w),3):
    e.append(w[i])

data={'Name':n,'Location':ad,'Price':f,'EMI':e}
op=pd.DataFrame(data)
op.style.hide_index()

