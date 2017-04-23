import os

#This file reads the episode list and renames the system files accordingly.
#I am unable to find the updated version of this file, will have to work on this from scratch again.
#It is not as simple as it looks, there are way too many discrepancies that need to be taken care of.


#Leaving the comments for now. 


path = r"C:\Users\Ayush\Downloads\South park Season S01-18 1080p Complete x265 Hevc uncensorced\Season #01\Extra\Season #01"
#names = os.listdir(path)

f = open(r"C:\Users\Ayush\PycharmProjects\Wikipedia\out18.txt",'r')
#dir = os.listdir(r"C:\Users\Ayush\Downloads\South park Season S01-18 1080p Complete x265 Hevc uncensorced\Extra\Season #01")
list = f.readlines()
#for x in list:
 #   print(str(x))
'''
x = 0
while x!=len(list):
    print(list[int(x)])
    x += 1
print(list)
d = os.listdir()
#if 'test' in d:
  #  print(d)

print(d)
print (', '.join(map(str, d)))
a = ', '.join(map(str, d))

for x in a:
    if 'test' in x:
     print(x)




for filename in os.listdir("."):
    if filename.startswith("test"):
        test = open(filename,'w')
        test.write(filename)
        test.close()

'''

y = 0
num = 1
for filename in os.listdir(r"C:\South\SP19"):
    #if filename.startswith("test"):
    os.rename("C:\South\SP19\\"+filename,"C:\South\SP19\\"+str(num)+' - '+list[int(y)].strip('\n')+'.mkv')
    y += 1
    num += 1

#os.rename(filename, filename[7:])
#for x in list:
  #  print(x)
#os.rename('o.txt','o2.txt')s
#for x in list:
#y = 0
    #os.rename(dir(x))
#for x in list:
 #   os.rename(d[y],x)
  #  y += 1


#print(dir[0])

#lines = [line.rstrip('\n') for line in open(r"C:\Users\Ayush\PycharmProjects\Wikipedia\out.txt")]
#for x in lines:
 #   print(x)
#f.close()

f.close()
