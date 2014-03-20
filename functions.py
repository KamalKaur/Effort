import itertools

"""
%% functions.py %%

This file is defines some important functions that are then called in views.py file. 
 
"""
def search(name):     # Added.....
	"""Get the soundex code for the string. Soundex is a phonetic algorithm
	which converts the given string into a code based on its pronounciation"""
	name = name.upper() 
	soundex = "" 
	soundex += name[0] 
	dictionary = {"BFPV": "1", "CGJKQSXZ":"2", "DT":"3", "L":"4", "MN":"5", "R":"6", "AEIOUHWY":"."} 
	for char in name[1:]: 
		for key in dictionary.keys(): 
			if char in key: 
				code = dictionary[key] 
				if code != soundex[-1]:
					soundex += code 
	soundex = soundex.replace(".", "")
	soundex = soundex[:5].ljust(4, "0") 
	return soundex

def split_line(name):

    # split the text
    words = name.split()

    # for each word in the line:
    for word in words:

        # prints each word on a line
        print(word)
	

if __name__ == '__main__':
	#counts = input("enter number of names you want to print code of:")
	#while(counts!=0):
        	name = raw_input("Enter a word :  >>  ")
#        	print(search(name))
		B=[]
		fields = ['foo', 'bar', 'baz']
#		phoneticsArray = [["this","thus"],["is","as","ease"],["it","at","eat"]]
		print name.split(' ')
		k = name.split(' ')
		#print name.split() for printing the list... same e gall a uper vali o :D
		l = [ search(x) for x in k ]
		print l
		for field in fields:
			lookup = "%s__contains" % field
			print lookup
		#m = l[0] for printing first element of list
		#print m

# for learning difference in append and extend
#		for word in l:
#			B.extend([word])
#			print "extending"
#			print B	
#		C=[]
#		for word in l:
#			C.append([word])
#			print "Appending"
#			print C


#		print phoneticsArray
		
#		stringsArray=[]
#		for string in itertools.product(*phoneticsArray):
#			stringsArray.append(string)
#		print stringsArray
        	#counts = counts - 1









