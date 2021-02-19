import matplotlib.pyplot as plt
import numpy as np

def plot_bar_x():
    # this is for plotting purpose
    index = np.arange(len(label))
    plt.bar(index, no_words)
    plt.xlabel('Letter', fontsize=8)
    plt.ylabel('No of occurences', fontsize=8)
    plt.xticks(index, label, fontsize=8, rotation=30)
    plt.title('Frequency of top words in the text file')
    plt.show()

myDictionary = {}
try:
    f = open("romeojuliet.txt",'r')
    lines = f.readlines()
    f.close()
except FileNotFoundError:
    print("File not available. ")

for line in lines:
    line = line.lower().split()
    for wrd in line:
        if wrd.isalpha() == True:
            if wrd in myDictionary:
                myDictionary[wrd] += 1
            else:
                myDictionary[wrd] = 1

print("Found",len(myDictionary),"words!")

topWords = {}
for wrd in myDictionary:
    if myDictionary[wrd] > 50:
        topWords.update({wrd:myDictionary[wrd]})

topWords = dict(sorted(topWords.items(), key = lambda item: item[1]))
# dict(sorted(x.items(), key=lambda item: item[1]))
# for i in topWords:
#    print(i, topWords[i])

label = []
no_words = []
for wrd in topWords:
    label.append(wrd)
    no_words.append(topWords[wrd])

# print(label)
# print(no_letters)
# index = np.arrange(len(label))

plot_bar_x()