import pickle
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import math

# know_base = pickle.load(open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Know_Base_Sent.p', 'rb'))
know_base = pickle.load(open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Know_Base_Merged.p', 'rb'))

stop_words = stopwords.words('english')

kb_tfidf = {}
kb_idf = {}
tf = {}

#kb_tfidf_format:
# kb_tfidf = {
#     'doc_1' : {
#         'word1': 'val1',
#         'word2': 'val2'
#     }
# }

#tf
for key, val in know_base.items():
    lt = word_tokenize(val)
    # lt = val.split(" ")

    temp = [word.lower() for word in lt if word.lower() not in stop_words and word.isalnum()]
    # temp = [WordNetLemmatizer().lemmatize(word) for word in temp]
    n = len(temp)

    temp = {word:temp.count(word)/n for word in set(temp)}
    tf[key] = temp

#idf
temp = []
for dt in tf.values():
    temp += list(dt.keys())

kb_idf = Counter(temp)

n = len(tf)

for key, val in kb_idf.items():
    kb_idf[key] = 1 + math.log(n/val)

#tf_idf
for key, val in tf.items():
    temp = {}
    for k, v in val.items():
        temp[k] = v*kb_idf[k]
    kb_tfidf[key] = temp

    
pickle.dump(kb_idf, open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/ChatBot Files/kb_idf.p', 'wb'))
pickle.dump(kb_tfidf, open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/ChatBot Files/kb_tfidf.p', 'wb'))