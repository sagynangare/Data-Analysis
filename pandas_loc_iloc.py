import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import html5lib
class Despatcher:
        def __init__(self,date):
                self.date =  date;
                self.url = "http://www.delhisldc.org/Loaddata.aspx?mode="
                self.url = self.url + self.date
                self.htmlList = pd.read_html(self.url,header=0)
                self.df = pd.DataFrame(self.htmlList[1], columns=['TIMESLOT','DELHI','BRPL','BYPL','NDPL','NDMC','MES'])
                self.df['TIMESLOT'] = self.df['TIMESLOT'].apply(lambda x:str(x)[11:])

        def getDataFrame(self):
                return self.df

        def createplot(self,other):
                
                #print(self.df.iloc[[i for i in range(100)], [2]])
                self.df= self.df.iloc[[i for i in range(len(self.df))], [2,3]]
                #plt.figure()
                self.df.plot()
                #self.df.plot(self.df.iloc[[i for i in range(100)], [2]])
                
                #other.df.plot(other.df.BRPL,other.df.DELHI)
                #plt.legend("BRPL","BYPL")
                #plt.xlable("BRPL")
                #plt.ylable("BYPL")
                plt.show()

if __name__ == '__main__':
        despetch  = Despatcher("01/01/2018")
        despetch2 = Despatcher("02/01/2018")
        print(despetch.getDataFrame().head())
        #print(despetch2.getDataFrame().head())
        despetch.createplot(despetch2)
