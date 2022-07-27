import re
import sys

def changetxt(word, f):
	f = open(file, 'a')
	f.write('\n'+word)
	f.close()
   
if sys.argv[1] == "-h":
	print("You can also just say: python3 main.py <file path>\n")
	
if sys.argv[1] != "-h":
	file = sys.argv[1]
	with open(file) as f:
		for word in sorted(set(re.findall('\w+', f.read().lower()))):
			changetxt(word, f)

else:
	file = input("Enter the directory of file:")
	with open(file) as f:
		for word in sorted(set(re.findall('\w+', f.read().lower()))):
			changetxt(word, f)