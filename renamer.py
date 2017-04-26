import os

#This file reads the episode list and renames the system files accordingly.
#I am unable to find the updated version of this file, will have to work on this from scratch again.
#It is not as simple as it looks, there are way too many discrepancies that need to be taken care of.


path = r"C:\South2\S2"

f = open(r"ep_names\Season 2 Episodes.txt",'r')

extensions = ('.webm','.mkv','.flv','.vob','.ogv', 
  '.ogg','.drc','.gif','.gifv','.mng','.avi','.mov', 
  '.qt','.wmv','.yuv','.rm','.rmvb','.asf','.amv','.mp4',
  '.m4p', '.m4v','.mpg', '.mp2', '.mpeg', '.mpe', '.mpv',
  '.mpg', '.mpeg', '.m2v','.m4v','.svi','.3gp','.3g2','.mxf',
  '.roq','.nsv','.f4v', '.f4p', '.f4a' ,'.f4b','.srt')
list = f.readlines()


y = 0
for filename in os.listdir(path):
    if filename.endswith(extensions):
      print(filename)
      extension = filename.split('.')[-1]
      try:
        os.rename(path+"\\"+filename,path+"\\"+list[int(y)].strip('\n')+'.'+extension)
      
      except Exception as e:
          print(e)
          pass
    y += 1



f.close()
