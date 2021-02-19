import matplotlib.pyplot as plt
import numpy as np

def plot_bar_x():
    # this is for plotting purpose
    index = np.arange(len(label))
    plt.bar(index, no_letters)
    plt.xlabel('Letter', fontsize=5)
    plt.ylabel('No of occurences', fontsize=5)
    plt.xticks(index, label, fontsize=5, rotation=30)
    plt.title('Frequency Analysis of the Holy Bible')
    plt.show()

myAlpha = {
    'a':0,
    'b':0,
    'c':0,
    'd':0,
    'e':0,
    'f':0,
    'g':0,
    'h':0,
    'i':0,
    'j':0,
    'k':0,
    'l':0,
    'm':0,
    'n':0,
    'o':0,
    'p':0,
    'q':0,
    'r':0,
    's':0,
    't':0,
    'u':0,
    'v':0,
    'w':0,
    'x':0,
    'y':0,
    'z':0
    }

f = open("holybible.txt",'r')
lines = f.readlines()
f.close()

for line in lines:
    line = line.lower()
    for ch in line:
        if ch in myAlpha:
            myAlpha[ch] += 1

for i in myAlpha:
    print(i, myAlpha[i])

label = []
no_letters = []
for i in range(26):
    currCh = chr(i+97)
    label.append(currCh)
    no_letters.append(myAlpha[currCh])

# print(label)
# print(no_letters)
# index = np.arrange(len(label))

plot_bar_x()

