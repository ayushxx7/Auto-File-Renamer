import re,os

episode = open(r"C:\Users\Nilay\Desktop\hack 2017\Auto-File-Renamer-master - Copy\ep_names\Episodes.txt")
episode = episode.read()
extensions = ('.webm','.mkv','.flv','.vob','.ogv', 
  '.ogg','.drc','.gif','.gifv','.mng','.avi','.mov', 
  '.qt','.wmv','.yuv','.rm','.rmvb','.asf','.amv','.mp4',
  '.m4p', '.m4v','.mpg', '.mp2', '.mpeg', '.mpe', '.mpv',
  '.mpg', '.mpeg', '.m2v','.m4v','.svi','.3gp','.3g2','.mxf',
  '.roq','.nsv','.f4v', '.f4p', '.f4a' ,'.f4b','.srt')


path = r"E:\NEW\Books\bored\shows - Copy\Season 4"
loc = os.listdir(path)
#print(path)


pat = r"[Ss]\d\d[Ee]\d\d"



# for i in episode.split('\n'):
# 	#rint(i)
# 	#rint(type(i))
# 	if re.findall(pat,i):
# 		print(i)

for rep in episode.split("\n"):
	for filename in loc:
		
		if filename.endswith(extensions):
		#print(filename)
			extension = filename.split('.')[-1]
			try:
				if (str(re.findall(pat,filename)).upper() == str(re.findall(pat,rep)).upper()):
					print (filename,rep)
					os.rename(path+"\\"+filename,path+"\\"+rep+'.'+extension)

			except Exception as e:
				print(e)
				pass
	
		
