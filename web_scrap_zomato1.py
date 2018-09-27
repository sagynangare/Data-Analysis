#Test Case of scrape the Name, Phone, Address, The first reviewers Name, The first Reviewers Score, The Review Text and the page link for all the McDonald's listings in Pune on Zomato using Python


import pandas as pd
import sys
from bs4 import BeautifulSoup as bs
import requests
import re

#WE USE CHROME BROWSER TO ANALYSIS THE DATA

city=input("please enter city :")
try:
    #request for pages of McDonalds Restaurant in provided city
    req = requests.get("https://www.zomato.com/"+city+"/restaurants/mcdonalds",\
                       headers={'User-Agent':'chrome/108.1.1.25'})
    #parse the requested row data
    h = bs(req.content,"html.parser")
    #to find the number of pages search contains
    y=h.find_all("div",{"class":"col-l-4 mtop pagination-number"})[0].text
    c=re.findall('([0-9]+)', y)
    pages=[str(i) for i in range(1,int(re.findall('([0-9]+)', y)[-1])+1)]
    #exception call if network problem OR not avilability of McDonalds in the city OR entered city is not root city(mumbai is a root city of thane)
except Exception:
    sys.exit("************"+city+" is not a root city or here no McDonalds Restaurant***********")
    
print("Pages",pages)
list_of_url=[]
#procedure to retrive all link in list
print("\nNETWORK PROCESS:",end=" ")
for j in pages:
    print("***************",end="")
    #one by one page request sent and retrive the raw data
    req = requests.get("https://www.zomato.com/"+city+"/restaurants/mcdonalds?page="+str(j),headers={'User-Agent':'chrome/108.1.1.25'})
    #parse raw data
    h = bs(req.content,"html.parser")
    c=h.find_all("div",{"class":"col-s-6 col-m-4"})
    #get all LIST of URL link in list into l
    for i in c:
        list_of_url.append(i.div.a["href"])
  

j=0
data=[]
print("\nDATA PROCESSING:",end=" ")
for i in list_of_url:
    df={}
    j+=1
    print("*",end="")
    req = requests.get(i,headers={'User-Agent':'chrome/108.1.1.25'})
    h=bs(req.content,"html.parser")
    
    c=h.find_all("div",{"class":"res-main-phone p-relative phone-details clearfix"})[0]
    #get data into DataFrame data values Name,Phone,Address,first reviewers Name,first Reviewers Score,Review Text and page link
    df["Name"]=str(re.findall('(.*?),', c["title"])).strip('[]')
    df["Phone"]=str(re.findall('([+][0-9]+)', c.text.strip())).strip('[]')
    df["Address"]=h.find_all("div",{"class":"borderless res-main-address"})[0].text.strip()
    df["Reviewers Name"]=h.find_all("div",{"class":"header nowrap ui left"})[0].text.strip()
    df["Reviewers Score"]=h.find_all("div",{"class":"rev-text mbot0 "})[0].div["aria-label"]
    df["Review Text"]=h.find_all("div",{"class":"rev-text mbot0 "})[0].text.strip()[39:]
    df["Link"]=i
    #append dataframe to data list
    data.append(df)
df1=pd.DataFrame(data)
#covert dataframe to CSV
df1.to_csv("zomato_"+city+".csv",index=False)
#Reading dat from CSV
d=pd.read_csv("zomato_"+city+".csv")
print(d)
