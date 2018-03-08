# Here, our goal is to write a python function that takes a string and returns the same string with each word capitalized,
# except for stopwords (the, in, etc..), unless the stopword is the first word in the string.
# i.e 'friends' -> 'Friends', 'rick and morty' -> 'Rick and Morty', 'the man in the high castle' -> 'The Man in the High Castle'.

#  To accomplish this, we use the string.capitalize() function, which returns the string with the first letter capitalized.
#  We first split the string into it's words, then capitalize the first word, then capitalize each consecutive word unless 
#  the word is a stopword, then rejoin the strings.

def capitalize_series_name(series_name):
    """ series_name = 'tHe man iN the high castle """
    tokens = series_name.split(' ')
    capitalized_tokens = []
    capitalized_tokens.append(tokens[0].lower().capitalize())
    stopwords = ['and', 'if', 'in', 'for', 'the']
    for token in tokens[1:]:
        lower_token = token.lower()
        if not lower_token in stopwords:
            capitalized_tokens.append(lower_token.capitalize())
        else:
            capitalized_tokens.append(lower_token)
    return ' '.join(capitalized_tokens)

print(capitalize_series_name('tHe man iN the high castle'))
    