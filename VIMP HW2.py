import pandas as pd
import numpy as np
import sqlite3 as sq
con=sq.connect("Railways2.db")
c=con.cursor()
def gen_date():
    m1=""
    
    while True:
        y=int(input("Enter Year:"))
        m=int(input("Enter Month:"))
        d=int(input("Enter Day:"))
        if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
            if(d>31):
                print("invalid")
                continue
            else:
                print("valid")
                break
        elif(m==4 or m==6 or m==9 or m==11):
            if(d>31):
                print("invalid")
                continue
            else:
                print("valid")
                break
        elif(m==2 and y%4==0):
            
            if(d>29):
                print("invalid")
                continue
            else:
                print("valid")
                break
            
        elif(m==2 and y%4!=0):
            if(d>28):
                print("invalid")
                continue
            else:
                print("valid")
                break
    if m<10:
        m1=m1+'0'+str(m)
    return str(d)+"/"+m1+"/"+str(y)
    
    
def store():
    q=gen_date()
    df=pd.read_html("http://www.delhisldc.org/Loaddata.aspx?mode={}".format(q))
    g=q.replace("/","_",-1)
    df[1][0:][0:].to_sql("raill{}".format(g),con,if_exists='append')
    print("SUCCESSFUL")

def view():
    print("WELCOME TO VIEW:")
    q=gen_date()
    g=q.replace("/","_",-1)
    try:
        sf=pd.read_sql_query("select * from raill{}".format(g),con)
    except:
        print("Table does not exists")
    finally:
        print(sf)
    #df=pd.read_html("http://www.delhisldc.org/Loaddata.aspx?mode={}".format(q))
    #print(df[1])


while True:
    t=int(input("HI..if Want to create new database type 1 , if want to view previous type 0, if exit type 2:"))
    if(t==1):
        store()
    elif(t==0):
        view()
    else:
        break
    
        
