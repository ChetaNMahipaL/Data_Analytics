import string
import os
from wordcloud import WordCloud

import matplotlib.pyplot as plt

with open("stopwords.txt", "r") as stop_words_file:
    stop_words = set(stop_words_file.read().splitlines())
    
with open("sh.txt", "r") as input_file:
    input_text = input_file.read()


input_text = input_text.translate(str.maketrans("", "", string.punctuation))
input_text = input_text.lower()

with open("filteredtext.txt", "w") as output_file:
    for word in input_text.split():
        if word not in stop_words:
            output_file.write(word + " ")


with open('filteredtext.txt', 'r') as file:
    text = file.read()

# Generate a word cloud from the text
wordcloud = WordCloud(width=4000, height=2000, background_color='white', max_words=20000).generate(text)

# Display the word cloud using matplotlib
plt.figure(figsize=(24, 24))
plt.imshow(wordcloud)
plt.axis('off')

wordcloud.to_file('wordcloud.png')

with open('filteredtext.txt', 'r') as file:

    text = file.read()

# Split the text into individual words
words = text.split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

most_common_word = None
most_common_count = 0

for word, count in word_counts.items():
    if count > most_common_count:
        most_common_word = word
        most_common_count = count
        
total_length = 0
word_count = 0

for word in words:
    length = len(word)
    total_length += length
    word_count += 1

average_length = total_length / word_count

print(f'The most common word is "{most_common_word}"')

print(f'The average word length is {average_length:.0f}')

os.remove("filteredtext.txt")
