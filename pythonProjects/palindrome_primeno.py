import string
special = string.punctuation
def palindr(sentence):
    for i in special:
        sentence.replace(i,"")
    palindrome = []
    words = sentence.split(' ')
    print("splitted are",words)
    print(words)
    for word in words:
        if word ==word[::-1]:
            palindrome.append(word)
        return palindrome
    
sentence =input("Enter the Sentence: ")
print(palindr(sentence))