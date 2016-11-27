import pandas as pd
import os  

i=0
root='./populations' #/expanded.race.by.hispanic/yr1992_2013.seer9.plus.sj_la_rg_ak/'

#for f in os.listdir(root):
for dirName, subdirList, fileList in os.walk(root):
    for f in fileList:
        #fname=root+f
        fname=dirName+"/" + f
        print "fname: ",fname
        if fname[-3:]=="txt":
            #if fname[-3:]
            print "r: ", root, " d: ", dirName, "s ", subdirList
            data = pd.read_csv(fname, sep=" ", header = None)
            df= pd.DataFrame()
            data.columns = ['text']

            print data.head()
            df["year"]=data['text'].str[0:4]
            df["st_postal"]=data['text'].str[4:6]
            df["st_FIPS"]=data['text'].str[6:8]
            df["county_FIPS"]=data['text'].str[8:11]
            df["registry"]=data['text'].str[11:13]
            df["race"]=data['text'].str[13:14]
            df["origin"]=data['text'].str[14:15]
            df["sex"]=data['text'].str[15:16]
            df["age"]=data['text'].str[16:18]
            df["population"]=data['text'].str[18:]

            print "fname: ", fname
            print "i: ",i
            print df.head()
            i+=1

            df.to_csv("parsed"+str(i)+".csv", sep='\t', index=False)
