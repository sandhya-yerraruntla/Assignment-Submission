from collections import Counter
sentence = input("Enter a sentence : ")
sen = sentence.split(" ")
for i in range(0,len(sen)):
    sen[i] = "".join(sen[i])
    sent = Counter(sen)
    s = " ".join(sent.keys())
print(s)
