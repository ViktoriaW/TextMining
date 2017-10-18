#mini project 3

import requests
import matplotlib.pyplot as plt
import string

wuthering_heights_full_text = requests.get('http://www.gutenberg.org/cache/epub/768/pg768.txt').text


def text_file(wuthering_heights_full_text):
    """Function which is creating histogram and are putting all words from text_line in the histogram dictionary """
    histo = dict()
    wuthei = open(wuthering_heights_full_text)
    for line in wuthei:
        text_line(line, histo)
    return histo

def text_line(line, histo):
    """Function which is checking a line in in the text and is replacing punctuation and whitespace and making all characters
    lowercase"""
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        if word.isalpha():                      #added this line for my revision, is taking away all of the punctuation and numbers, so now only words in my dictionary!
            histo[word] = histo.get(word, 0) + 1

histo = text_file('Wuthering_heights.link.txt')

def least_common_words(histo):
    """Function is printing the amount of words that is only mentioned once (frequency = 1)"""
    list_of_tuples = []
    for word, freq in histo.items():
        list_of_tuples.append((freq, word))
    list_of_tuples.sort()
    words_with_freq1 = []
    for freq, word in list_of_tuples:
        if freq == 1:
            words_with_freq1.append(word)
    return words_with_freq1

def num_occurence(histo, num):
    list_of_tuples = []
    for word, freq in histo.items():
        list_of_tuples.append((freq, word))
    list_of_tuples.sort()
    words_with_num = []
    for freq, word in list_of_tuples:
        if freq == num:
            words_with_num.append(word)
    return len(words_with_num)

def occurence(histo):
    list_of_i = []
    list_of_occurence = []
    for i in range(5000):
        list_of_occurence.append(num_occurence(histo,i))
        list_of_i.append(i)
    return list_of_i , list_of_occurence

xaxis, yaxis = occurence(histo)



#This first graph is an overview of my data, you can see that there are multiple words in the lower frequencies that
#are decreasing.

plt.plot(xaxis, yaxis, 'ro')
plt.axis([0, 5000, 1, 5000])
plt.xlabel('Frequency')
plt.ylabel('Number of words ')
plt.show()

#Chose to comment out my plots here since I have them in my report, wrote a describing text to them

#Two plots underneath shows that there are a lot of words which are printed 1-25 times. It is decreasing more after 50 times.

# plt.plot(xaxis, yaxis, 'ro')
# plt.axis([0, 200, 1, 250])
# plt.xlabel('Frequency')
# plt.ylabel('Number of words ')
# plt.show()

# plt.plot(xaxis, yaxis, 'ro')
# plt.axis([0, 200, 0, 40])
# plt.xlabel('Frequency')
# plt.ylabel('Number of words ')
# plt.show()

#Last plot shows the high frequency words. There are a lot of words in the higher frequencies that don’t have any number of words.
#But there are a few words appearing ~4800 times or ~3700 times.

# plt.plot(xaxis, yaxis, 'ro')
# plt.axis([30, 5000, 1, 12])
# plt.xlabel('Frequency')
# plt.ylabel('Number of words ')
# plt.show()


# -------------------End of project --------------------------------

#code i wrote but did not use for the final project

eng = ['the' , 'he', 'at', 'but', 'there', 'of', 'was', 'be', 'not', 'use', 'and', 'for', 'this', 'what', 'an', 'a', 'on', 'have', 'all', 'each', 'to', 'are', 'from', 'were', 'which', 'in', 'as', 'or', 'we', 'she', 'is', 'with', 'in', 'when', 'do',
         'you', 'his', 'had', 'your', 'how', 'that', 'they', 'by', 'can', 'their', 'it', 'I', 'word', 'said', 'i',  'her', 'my', 'me', 'if']

def most_common_words(histo):
    """Creating a list of tuples to be able to sort the list after frequency. Returning the 50 first elements in the list
    (the 50 most common words in the book and their frequency)"""
    list_of_tuples = []
    for word, freq in histo.items():
        list_of_tuples.append((freq, word))
    list_of_tuples.sort(reverse = True)
    return list_of_tuples[:50]

def subtract(histo, common_words):
    res = dict()
    for word in histo.keys():
        if word not in common_words:
            res[word] = histo[word]
    return res
