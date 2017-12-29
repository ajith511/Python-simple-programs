def find_sub(sentence):
    sentence = sentence.split()
    for word in sentence:
        sentence.remove(word)
        sentence = " ".join(sentence)
        if sentence.find(word) == -1:
            pass
        else:
            print(word, ' has a substring in another word in the same sentence')
        sentence = sentence.split()
        sentence.append(word)
find_sub("think it's more likely you wanted to mention the third parameter to slice. Needing to get every other character from a string may be an important use case somewhere,but I've never had to   it. Not that there's anything wrong with wanting to show off what you know -- what's the point of knowing things if you can't do that. But the case for relevance to the question is overstated.")