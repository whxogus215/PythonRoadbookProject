#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')


# In[2]:


get_ipython().system('pip install lxml')


# In[10]:


import requests
from bs4 import BeautifulSoup

# '범죄도시2'의 네이버 영화 리뷰 링크
url = "https://movie.naver.com/movie/bi/mi/review.naver?code=192608"
# html 소스 가져오기
res = requests.get(url)

# html 파싱
soup = BeautifulSoup(res.text, 'lxml')  ## res.text는 requests Get 메서드를 사용해서 가져온 리소스이다.

# 리뷰 리스트
ul = soup.find('ul', class_="rvw_list_area")
lis = ul.find_all('li') ## 자료형 List

# 리뷰 제목 출력
count = 0
for li in lis:
    count += 1
    print(f"[{count}th] ", li.a.string)




# In[ ]:




