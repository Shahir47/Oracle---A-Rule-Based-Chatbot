import collections
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from collections import Counter
import math
import re
import pickle
import urllib
from urllib import request
from bs4 import BeautifulSoup
import re

collections.Callable = collections.abc.Callable

#We'll collect all the games from these 3 links
list_ps4_1 = 'https://en.wikipedia.org/wiki/List_of_PlayStation_4_games_(A%E2%80%93L)'
list_ps4_2 = 'https://en.wikipedia.org/wiki/List_of_PlayStation_4_games_(M%E2%80%93Z)'
list_ps5 = 'https://en.wikipedia.org/wiki/List_of_PlayStation_5_games'

store_links = {}
#following links will be excluded
exclude_link = ['/wiki/Polygon_(website)', '/wiki/Youtube', '/wiki/Rock_Paper_Shotgun', '/wiki/GameSpot', '/wiki/Gamepressure', \
                '/wiki/Eurogamer', '/wiki/Radio_Times', '/wiki/Engadget', '/wiki/Official_U.S._PlayStation_Magazine', '/wiki/PlayStation:_The_Official_Magazine', \
                '/wiki/PlayStation_Official_Magazine_%E2%80%93_UK', '/wiki/PlayStation_Official_Magazine_%E2%80%93_Australia', '/wiki/PlayStation_Underground', \
                '/wiki/Double_Life_(PlayStation_ad)', '/wiki/Mountain_(advertisement)', '/wiki/PlayStation_Blog', '/wiki/Game_Informer', '/wiki/VG247', '/wiki/Destructoid', \
                '/wiki/Slitherine_Software', '/wiki/IGN', '/wiki/Outright_Games', '/wiki/Push_Square', '/wiki/Anime_News_Network', '/wiki/Arcade_Archives', '/wiki/Arcade_Game_Series', \
                '/wiki/Wikipedia:Link_rot', '/wiki/PQube', '/wiki/NME', '/wiki/Zotrix', '/wiki/Gamesindustry.biz', '/wiki/YouTube', '/wiki/Jeuxvideo.com']

url_list = [list_ps4_1, list_ps4_2, list_ps5]

for url in url_list:
  try:
    html = request.urlopen(url, timeout=20).read().decode('utf8')
  except:
    print("error")
  else:
    soup = BeautifulSoup(html, "lxml")

    #first we'll find all the links associated with games
    for link in soup.find_all('a'): 
        lk = link.get("href")
        if(str(link.parent).startswith('<i>')): #In all three sites the page link of games got <i> tags. This helps to exclude other links that is not our concern
          include = 'wiki'
          exclude = 'wiki/List|wiki/Help|wiki/Category|wikipedia' #we'll exclude links of this format
          if(re.search(include, str(lk)) != None and re.search(exclude, str(lk)) == None):
            if lk not in exclude_link:
              store_links[link.text] = 'https://en.wikipedia.org/' + lk #we are getting part of a link with beautiful soup. So, making it whole.

game_main = {}

#For all the games, we'll extract the first paragraph that conatins the info of the game (summary)
for key, url in store_links.items():
  try:
    html = request.urlopen(url, timeout=20).read().decode('utf8')
  except:
    print("error")
  else:
    soup = BeautifulSoup(html, "lxml")
    i = 0
    print(key)
    for p in soup.select('p'):
      i += 1
      if(i == 2): #almost in all the case the second p tag is the acutal first content paragraph
        game_main[key] = p.get_text()
      if(i > 2):
        break

to_be_deleted = [] #if we get no paragraph for a game, we simply delete that.
for key in game_main.keys():
  if len(game_main[key]) == 1:
    to_be_deleted.append(key)

for key in to_be_deleted:
  del game_main[key]

for key, val in game_main.items():
  temp = re.sub('\[.*?\]', "", val) #processing the values and removing unwanted characters
  key = ''.join([i if ord(i)<128 else '' for i in key]) #taking only ascii characters
  temp = ''.join([i if ord(i)<128 else '' for i in temp])

  game_main[key] = temp


pickle.dump(game_main, open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Game_Base.p', 'wb'))


# Merges with know_base_sent:
know_base = pickle.load(open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Know_Base_Sent.p', 'rb'))

know_base_final = {}

for key, val in know_base.items():
  know_base_final[str(key)] = val

for key, val in game_main.items():
  know_base_final[str(key)] = val


pickle.dump(know_base_final, open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Know_Base_Merged.p', 'wb'))