import re
s = 'GeeksForGeeks: A. computer3 science portal for geeks'
# s=input("enter the string in which have to be find")
match =re.search(r'geeks',s)
print('Start Index:',match.start())
print('End Index:', match.end())

# \	Used to drop the special meaning of character following it
# []	Represent a character class
# ^	Matches the beginning
# $	Matches the end
# .	Matches any character except newline
# |	Means OR (Matches with any of the characters separated by it.
# ?	Matches zero or one occurrence
# *	Any number of occurrences (including 0 occurrences)
# +	One or more occurrences
# {}	Indicate the number of occurrences of a preceding regex to match.
# ()	Enclose a group of Regex
print("dkfjs")
match =re.search(r'\.', s)
print(match)
match = re.search(r'[0,3]',s) #match = re.search(r'[0-3]',s)
print(match)
match =re.search(r's|b', s)
print("dkfjs",match)

