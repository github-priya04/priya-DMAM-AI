# Write a python program that removes all punctuation from a given string.


punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
string1 = "Hello!!!, he said ---and went."


no_punct = ""
for char in string1:
   if char not in punctuations:
       no_punct = no_punct + char


print(no_punct)







