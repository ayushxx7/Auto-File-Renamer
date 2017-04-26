from bs4 import BeautifulSoup as bs
import urllib.request as ur
import re

#This file is for scraping the episode names from Wikipedia.
#After running this, do check whether all episodes were properly scraped or not.


#paste appropriate link from Wikipedia [format is https://en.wikipedia.org/wiki/List_of_Series_Name_episodes {how convenient for further automation}]
wiki = "https://en.wikipedia.org/wiki/List_of_South_Park_episodes"

header = {'User-Agent': 'Mozilla/5.0'}  # Needed to prevent 403 error on Wikipedia
req = ur.Request(wiki, headers=header)
page = ur.urlopen(req)
soup = bs(page,'html.parser')

#n = int(input('how many seasons?'))
n = int(20)
table = soup.findAll('table',attrs={'class':"wikitable plainrowheaders wikiepisodetable"}) #fixed format for episode list table for every series
t = 0


#I am using a counter to get all the episode names of all seasons in one go.

while t!=n:
    ep_num = 1
    with open('ep_names\\Season ' + str(t + 1) + ' Episodes.txt','w') as f:

        for row in table[t].findAll('tr',{'class':'vevent'}):
            
            #could've used findAll('tr')[1:]: as well
            cells = row.findAll('td')
        
        #safety first
            try:
                #name = cells[1].a.string.strip()  // earlier method, not universal
                #print(type(name))
                name = cells[1].get_text() # probably universal
                #if name.startswith('"') and name.endswith('"'):
        
                #minor discrepancies taken care of    
                if '"' in name:
                    name = re.sub('"','',name)
                if '\?' in name:
                    name = re.sub('\?','',name)
                if ':' in name:
                    name = re.sub(':', ' -', name)
        
                #zfill adds 0s to make names consistent.
                f.write('S'+str(t+1).zfill(2)+'E'+str(ep_num).zfill(2)+ " " +name + '\n')
                ep_num += 1
               # f.write(name+'\n')
            except Exception as e:
                f.write('\n***'+str(e)+'****\n')
                pass  #no interruptions.
    t+=1


