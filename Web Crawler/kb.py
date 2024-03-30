from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from collections import Counter
import math
import re
import pickle


path = "/Users/Asus/OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Processed_Files/"

documents = {}
doc_tokens = {}
doc_sent_tokens = {}
vocab = set()
important_dict = {}
know_base = {}

doc_val = 0
val = 0
stop_words = set(stopwords.words('english'))

def generate_docs():
    global documents, doc_val, val

    while val<=121:
        val += 1
        filename = f"Out_File_{val}.txt"
        try:
            fhand = open(path+filename, 'r')
        except:
            continue

        else:
            raw_text = fhand.read()
            doc_val += 1
            documents[f"doc_{doc_val}"] = raw_text


def pre_process():
    global documents, stop_words, doc_tokens

    for id, text in documents.items():
        temp = word_tokenize(text)
        temp = [item.lower() for item in temp if item.lower() not in stop_words and item.isalpha()]
        doc_tokens[id] = temp


def tfIdf_calc():
    global vocab, important_dict

    vocab_all = []
    tf = {}

    for id, lt in doc_tokens.items():
        n = len(lt)
        vocab = vocab.union(set(lt))
        vocab_all += list(set(lt))

        counter_ = Counter(lt)
        for k, v in counter_.items():
            counter_[k] = v/n
        tf[id] = counter_

    idf = Counter(vocab_all)
    doc_num = len(doc_tokens)
    print(f"Document number is : {len(doc_tokens)}")

    for k, v in idf.items():
        idf[k] = 1 + math.log(doc_num/v)
        # idf[k] = math.log((1+doc_num)/(1+v)

    for id, lt in tf.items():
        temp = {}
        for key in lt.keys():
            temp[key] = lt[key]*idf[key]

        temp_len = min(len(temp), 45)
        important_list = []
        for t_key, t_val in sorted(temp.items(), key = lambda x : -x[1]):
            if(temp_len == 0):
                break
            important_list.append(t_key)
            temp_len -= 1

        important_dict[id] = important_list


#Start from here <-------------------
generate_docs()
pre_process()
tfIdf_calc()


#filtering important words
fhand = open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Utility Files/not_important_words.txt', 'r')
not_important = fhand.read().split(" ")

for lt in important_dict.values():
  to_be_deleted = []

  for i in range(len(lt)):
    if lt[i] in not_important or len(lt[i]) == 1:
        to_be_deleted.append(i)

  for item in sorted(to_be_deleted, reverse=True):
    lt.pop(item)


#create sent tokenize
for key, value in documents.items():
  doc_sent_tokens[key] = sent_tokenize(value)

def already_exist_in_know_base(line):
  for lt in know_base.values():
    if line in lt:
      return False
  return True


#knowledge base
for key, value in important_dict.items():
  sent_list = doc_sent_tokens[key]

  for line in sent_list:
    for word in value:
      if word in line.split(" "):
        if word in know_base.keys() and len(know_base[word]) > 7:
          continue
        else:
          if already_exist_in_know_base(line):
            know_base[word] = know_base.get(word, []) + [line]


#Sentence level knowledge base creation:
know_base_sent = {}

count_ = 0
for lt in know_base.values():
  for line in lt:
    count_ += 1
    know_base_sent[count_] = line


pickle.dump(know_base_sent, open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Know_Base_Sent.p', 'wb'))