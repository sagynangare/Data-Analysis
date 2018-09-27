from urllib.request import Request, urlopen
import webbrowser
import requests
from bs4 import BeautifulSoup


#another="https://www.zomato.com/bangalore/top-restaurants"
url="https://www.zomato.com/pune/restaurants/mcdonalds"
#w=webbrowser.open(url)
#print(w)
res=requests.get(url)
#print(res.text)
#Used headers/agent because the request was timed out and asking for an agent. 
#Using following code we can fake the agent.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
response = requests.get(url,headers=headers)
content = response.content
soup = BeautifulSoup(content,"html.parser")
#print(soup)
##top_rest = soup.find_all("a",attrs={"class": "ln24 search-page-text mr10 zblack search_result_subzone left"})
##print(top_rest[0])

top_rest = soup.find_all("a",attrs={"class": "ln24 search-page-text mr10 zblack search_result_subzone left"})
list_tr = top_rest[0].find_all("title",attrs={"class": "col-s-8 col-l-1by3"})
'''list_rest =[]
for tr in list_tr:
    dataframe ={}
    dataframe["rest_name"] = (tr.find("div",attrs={"class": "res_title zblack bold nowrap"})).text.replace('\n', ' ')
    dataframe["rest_address"] = (tr.find("div",attrs={"class": "nowrap grey-text fontsize5 ttupper"})).text.replace('\n', ' ')
    dataframe["cuisine_type"] = (tr.find("div",attrs={"class":"nowrap grey-text"})).text.replace('\n', ' ')
    list_rest.append(dataframe)
print(list_rest)
'''

























##lk='http://www.cmegroup.com/trading/products/#sortField=oi&sortAsc=false&venues=3&page=1&cleared=1&group=1'
###sauce = urllib.request.urlopen(url).read()
###soup = bs.BeautifulSoup(sauce, 'lxml')
##req = Request(url)#,headers={'User-Agent': 'Google-Chrome'})
##webpage = urlopen(req).read()
