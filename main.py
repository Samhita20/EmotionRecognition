# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 18:37:44 2020

@author: Samitha
"""


# Cleaning text :
# 1. Create a text file and read text from it
# 2. Convert all the letters into lower case
# 3 . Remove punctuations

import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# generally text from blog articles and web articles, the text will be utf are encoded(expecially on the web)

text = open('read.txt',encoding='utf-8').read()

# converting text to lower case so that we compare easily

lower_case = text.lower()

# str1 and str2 of the maketrans method are used for replacing and str23 is used to delete the punctuations

clean_text = lower_case.translate(str.maketrans('','',string.punctuation ))

# we split the string into separate words and store them into a list : tokenization
# we analyze the words and not sentences

tokenized_words = word_tokenize(clean_text,"english")

# stop words are words which do not convey any meaning or emotion to the text written (eg- prepositions)



# we will remove the stop words from the tokenized words to get the final words used for the analysis

final_words = []
for word in tokenized_words:
    if word not in stopwords.words("english"):
        final_words.append(word)

# NLP Emotion Algorithm
# 1. Check if the words in the final_words list are present in the emotions.txt(word before colon)
#   - open the emotion file
#   - loop through each line and clear it(unnecessary stuff)
#   - extract the word and emotion using split
# 2. If word is present add the emotion to the emotion_list
# 3. Count each emotion in the emotion_list

emotion_list=[]
with open('emotions.txt','r') as file:
    for line in file:
        # clearing unnecessary stuff
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        wordemt = clear_line.split(':')
       
        if wordemt[0] in final_words:
           emotion_list.append(wordemt[1])

# Count the number of times each word of emotion_list appears

w=Counter(emotion_list)
max_sentiment = max(w, key=w.get)
print(max_sentiment)
    

def sentiment_analyze(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if(neg>pos):
        print('Negative sentiment')
    elif(pos>neg):
        print('Positive sentiment')
    else:
        print('Neutral vibe')
  
sentiment_analyze(clean_text)

# Plotting the graph for each of the words

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()