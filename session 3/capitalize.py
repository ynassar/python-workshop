# Here, our goal is to write a python function that takes a string and returns the same string with each word capitalized,
# except for stopwords (the, in, etc..), unless the stopword is the first word in the string.
# i.e 'friends' -> 'Friends', 'rick and morty' -> 'Rick and Morty', 'the man in the high castle' -> 'The Man in the High Castle'.

#  To accomplish this, we use the string.capitalize() function, which returns the string with the first letter capitalized.
#  We first split the string into it's words, then capitalize the first word, then capitalize each consecutive word unless 
#  the word is a stopword, then rejoin the strings.
