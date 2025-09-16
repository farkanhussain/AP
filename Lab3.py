from collections import Counter

def analyse_sentence(sentence):
    words= sentence.lower().split()
    total_words=len(words)
    unique_words=len(set(words))
    most_common= Counter(words).most_common(1)[0]

    return total_words, unique_words, most_common

sentence="Python is great, python is fun, python is useful"
total,unique,common=analyse_sentence(sentence)
print("Total words: ",total)
print("Unique words: ",unique)
print("Most common words: ",common[0], "appears",Common[1],"times")
