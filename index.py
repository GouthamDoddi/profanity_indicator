# lets assume the profanity_list contains words with profanity degree value
# as the index of the word in the list
profanity_list = ['word1', 'word2', 'word3' ....'word-n']

# code to convert paragraph to list of sentences
# asume the list of sentance are placed in list

list_of_sentences = [....]

profanity_indicator = []

for n in range(0, len(list_of_sentences)):
    for word in profanity_list:
    if profanity_indicator[n]: 
        profanity_indicator += list_of_sentences[n].count(word)
    profanity_indicator = list_of_sentences[n].count(word)


# profanity_indicator will have a value corresponding to the list_of_sentences
# for every index in the list_of_sentences there will be a value in the profanity_indicator
# at the same index

# time complexety 
# list_of_sentence lenght is N and profanity_list is M
# O(N^M)
