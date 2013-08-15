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
	soundex = soundex[:20].ljust(20, "0") 
	return soundex
 
if __name__ == '__main__':
	#counts = input("enter number of names you want to print code of:")
	#while(counts!=0):
        	name = raw_input("Name :  >>  ")
        	print(search(name))
        	#counts = counts - 1







