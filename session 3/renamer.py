# It's time to put it all together!

import os
import guessit

base_dir = './data'

def create_folder_if_not_exists(base_dir, dir_name):
    dir_path = os.path.join(base_dir, dir_name)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

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


for root, dirs, files in os.walk(base_dir):
    for file in files:
        filename, ext = os.path.splitext(file)
        file_path = os.path.join(root, file)
        if not ext in ['.mkv', '.avi', '.mp4']:
            os.remove(file_path)
        else:
            d = guessit.guessit(filename)
            episode_number = d['episode']
            season_number = d['season']
            title = d['title']
            title = capitalize_series_name(title)
            create_folder_if_not_exists(base_dir, title)
            series_folder_path = os.path.join(base_dir, title)
            create_folder_if_not_exists(series_folder_path, 'Season ' + str(season_number))
            new_file_path = os.path.join(series_folder_path, 'Season ' + str(season_number), str(episode_number) + ext)
            os.rename(file_path, new_file_path)

