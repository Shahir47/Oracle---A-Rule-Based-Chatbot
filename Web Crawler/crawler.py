#Python Version 3.11.5
import collections
from urllib import request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re
import copy
import random
import pickle

collections.Callable = collections.abc.Callable

initial_links = ['https://en.wikipedia.org/wiki/Video_game',\
                'https://en.wikipedia.org/wiki/History_of_video_games',\
                'https://en.wikipedia.org/wiki/List_of_video_games_considered_the_best']

#links that should be discarded
forbidden_links = pickle.load(open("OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Utility Files/forbidden_link.p", 'rb'))
forbidden_wiki_links = pickle.load(open("OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Utility Files/forbidden_wiki_link.p", 'rb'))

inter_links = copy.deepcopy(initial_links)
wiki_links = copy.deepcopy(initial_links)

final_links = copy.deepcopy(initial_links)
link_count = 3

def valid_link(url): #this returns whether a link should be selected or not
    try:
      html_vl = request.urlopen(url, timeout=20).read().decode('utf8')  
    except:
      return False
    else:
      if url in forbidden_links: return False
      else:
        doc_len = ''
        soup_vl = BeautifulSoup(html_vl, 'lxml')

        for p in soup_vl.find_all('p'):
          doc_len += p.get_text()
        doc_len = len(doc_len.split(' '))

        return False if doc_len < 50 else True

def link_extractor(url, type):
  global inter_links, final_links, link_count, wiki_links

  try:
    html = request.urlopen(url).read().decode('utf8')
  except HTTPError as http_e:
    print(http_e.code)
  except URLError as url_e:
    print(url_e.reason)

  else:
    soup = BeautifulSoup(html, "lxml")
    temp_links = list()

    #Extraction of all the links
    for link in soup.find_all('a'):
        lk = link.get("href")
        exclude = 'wiki|pdf|facebook|twitter|login|sign|scholar.google|semanticscholar|jstor|news|books.google.com|youtube|salon|doi' #link with this will be excluded
        include = 'http'

        #For all other types of links
        if(type == 'other' and re.search(exclude, str(lk)) == None and re.search(include, str(lk)) != None):
          if(re.search('http.*://web.archive.org.*/http', lk) != None): #link fro this files needs some modification
            lk = re.sub('http.*://web.archive.org.*/http', 'http', lk)
          temp_links.append(lk)
        
        #For wiki links
        wiki_pattern = '/wiki/Category|/wiki/File|/wiki/Portal|/wiki/Wikipedia|/wiki/Special|/wiki/Template|/wiki/ISBN|/wiki/Doi\
          /wiki/S2CID|identifier|publisher|website|/wiki/Talk' #links with these patterns will be excluded
        if(type == 'wiki' and isinstance(lk, str) and re.search('^/wiki/', lk) != None and re.search(wiki_pattern, lk) == None):
          if lk not in forbidden_wiki_links:
            temp_links.append('https://en.wikipedia.org/' + lk)

    k = 20 if url in initial_links else 2
    if type == "wiki":
      k = 5 if url in initial_links else 1

    k = min(k, len(temp_links))
    i = 1
    
    total = 90
    if type == "wiki":
      total = 120

    #Suitable link selection
    while i<=k and link_count <= total and temp_links:
      rand_link = random.choice(temp_links)
      print(rand_link)

      if(rand_link not in final_links and valid_link(rand_link)):
        if type == 'other':
          inter_links.append(rand_link)
        if type == 'wiki':
          wiki_links.append(rand_link)

        final_links.append(rand_link)
        i += 1
        link_count += 1

      else:
        temp_links.pop(temp_links.index(rand_link))

      print(link_count)


def iterator_(list_, total_, point_, switch_): #'total_' is for the no of links we'll extract, after 'point_' we'll extract randomly
  while(len(list_) > 0):
    if link_count > total_:
      break
    if(link_count > point_):
      rand_indx = list_.index(random.choice(list_))
      item = list_.pop(rand_indx)
    else:
      item = list_.pop(0)

    link_extractor(item, switch_)

#Start Here: <----------------
iterator_(inter_links, 70, 30, 'other') #This for links which are not from wikipedia.

iterator_(wiki_links, 120, 95, 'wiki')

filename = f"OneDrive\Desktop\SEM_2\CS 6320\Practical\Project\Project_1\Files\links_list.txt" #This saves all the 121 links from which we'll generate text file below
fhand = open(filename, 'w')
for url in final_links:
  fhand.write(url)
  fhand.write('\n')



#Generate Initial Files
print("\n\n***** Generating Files: *****\n\n")

filename = f"OneDrive\Desktop\SEM_2\CS 6320\Practical\Project\Project_1\Files\links_list.txt"
fhand = open(filename, 'r')

val = 0

for url in fhand:
  print("working with--->", url)
  val += 1
  filename = f"File_{val}"
  path = f"OneDrive\Desktop\SEM_2\CS 6320\Practical\Project\Project_1\Files\Initial_Files\{filename}.txt"
  fout = open(path, 'w')

  html = request.urlopen(url).read().decode('utf8')
  soup = BeautifulSoup(html, "lxml")
  for p in soup.select('p'):
    try:
        content = p.get_text()
        fout.write(content)
        fout.write("\n")
    except:
        print('couldn\'t write')