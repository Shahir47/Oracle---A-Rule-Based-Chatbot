from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import pickle

know_base = pickle.load(open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Know_Base_Manual.p', 'rb'))
KB_cosine_procss = {}

stop_words = stopwords.words('english')
wnl = WordNetLemmatizer()

for k, v in know_base.items():
    if type(v) == tuple:
        lines = v

        key_procss = []
        for line in lines:
            temp = word_tokenize(line) 
            temp = [wd.lower() for wd in temp if wd.isalnum() and wd not in stop_words]
            n = len(temp)
            temp_dt = {wd:temp.count(wd)/n for wd in set(temp)}
            key_procss.append(temp_dt)
        
        temp_dt = key_procss

    else:
        temp = word_tokenize(v)
        temp = [wd.lower() for wd in temp if wd.isalnum() and wd not in stop_words]
        # temp = [wnl.lemmatize(wd) for wd in temp]
        n = len(temp)
        temp_dt = {wd:temp.count(wd)/n for wd in set(temp)}

    KB_cosine_procss[k] = temp_dt

fhand = open('OneDrive/Desktop/Test.txt', 'w')
for k,v in KB_cosine_procss.items():
    fhand.write(f"{k} ---> {v}\n")

pickle.dump(KB_cosine_procss, open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/ChatBot Files/kb_cosine_procss.p', 'wb'))
