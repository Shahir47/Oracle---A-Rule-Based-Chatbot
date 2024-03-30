from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pickle
import sys
import random
import re
import copy
import math

#global variables
know_base = pickle.load(open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Know_Base_Merged.p', 'rb'))
user_info = pickle.load(open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/ChatBot Files/user_info.p', 'rb'))
greet_conv = pickle.load(open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/ChatBot Files/greetings_conv.p', 'rb'))
game_base = pickle.load(open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Know_Base_Game.p', 'rb'))
#
kb_cosine = pickle.load(open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/ChatBot Files/kb_cosine_procss.p', 'rb'))

rps_rand_target = random.choice([4,5,6,7]) #this will be used to trigger the info about rock_paper_scissor game

name = None
last_que = ''
stop_words = stopwords.words('english')
#end of global variables

game_list = list(game_base.keys())
sid = SentimentIntensityAnalyzer()

#It will save user_info and will exit from the game
def exit_():
    global user_info
    if name != None:
        user_info[name]['lastConv'] = last_que
        pickle.dump(user_info, open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/ChatBot Files/user_info.p', 'wb'))
    sys.exit()

#this is used to greet an existing user
def old_user_greetings():
    temp = random.choice(greet_conv['old'])
    temp2 = random.choice(greet_conv['old_game']) 
    print(f"Welcome Back {name.upper()}. {temp} {temp2} {user_info[name]['favtGame']}?") #Welcome and reminder about old game
    inpt = input('> ')
    #response:
    greet_que_sent = sid.polarity_scores(inpt)
    if(greet_que_sent['pos'] > greet_que_sent['neg']):
        print(random.choice(greet_conv['greet_que_pos']))
    elif(greet_que_sent['pos'] < greet_que_sent['neg']):
        print(random.choice(greet_conv['greet_que_neg']))
    else:
        print("Ok, Thank you for sharing")
    
    #Last saved conversation:
    if(user_info[name]['lastConv'] != ''):
        print(f"In our last conversation we talked about, '{user_info[name]['lastConv']}'")
    
    return

#this is used to greet a new user 
def new_user_greetings():
    temp = random.choice(greet_conv['new'])
    print(f"Hello {name.upper()}. {temp}") #Welcome
    user_info[name] = {}
    user_info[name]['name'] = name.upper()
    
    print("I would love to know you a bit better. What is your favourate game?")
    inpt = input('> ')
    user_info[name]['favtGame'] = inpt #save favourite game name
    print(random.choice(greet_conv['game_choice']))


#from here everything starts
def brain():
    global name, last_que

    greetings()
    #the progarm won't go forward until it has user's name
    while(True):
        if(name != None):
            break
        print(f"{random.choice(greet_conv['name_que'])} (Nickname)")
        inpt = input('> ')
        if inpt == 'help()': help_()
        elif inpt == 'exit()': exit_()
        elif inpt == '': continue
        else:
            name = inpt.lower()

    if(name in user_info.keys()): #Old User
        old_user_greetings()
    
    else: #New User
        new_user_greetings()

    #start of question-answer:
    print("""\nWhat do you want to talk about today?""")

    rps_rand = 0 #when this will equal to rps_rand_target we'll generate info about rock_paper_scissor game
    while(True): #this keeps runnig until exit() is called
        rps_rand += 1
        inpt = input('> ')
        if(inpt != "exit()" and inpt != 'help()'):
            last_que = inpt

        if(inpt == 'help()'): help_()
        if(inpt == 'exit()'): exit_()
        if(inpt == 'rockpaperscissor()'): rockPaperScissor()

        if(inpt != 'help()' and inpt != 'exit()' and inpt != 'rockpaperscissor()'):
            text = copy.deepcopy(inpt)

            prediction = cosine_sim(text) #this calls the cosine similarity function and gets a key of the know_base or 0
            if prediction == 0: #we handeled 0 prediction in the follwoing two ways
                if(re.findall('why|how|who|where|when|what|whose', text.lower()) != None and len(text.split(" ")) == 1):
                    print(random.choice(greet_conv['req_more_info'])) #if the prediction is 0 and the user input was only a word
                else:
                    print(random.choice(greet_conv['zero_prediction']))
            else:
                print(know_base[prediction])
                if(prediction == 'c2'): #if users asks for games suggestions
                    temp_game_list = random.sample(game_list, 5)
                    tgl_i = 0
                    for tgl in temp_game_list:
                        tgl_i += 1
                        print(f"{tgl_i}. {tgl}")
                
                if(prediction == 'c10'):#if users want to talk about anything the chatbot says
                    print(random.choice(list(know_base.values())))

        if(rps_rand == rps_rand_target): #this is when the bot introduces the functinality of the rock paper scissor
            print("\n***** Do you want to play rock paper scissor!!! type: rockpaperscissor() to play *****\n")
        print("\n")




def main():
    brain()
        
#provides user with information on what facilites the chatbot offers
def help_():
    print("""
I am so exited that you are here. Even though I would love to talk about many things, but since I play games all
the time I didn't get enough time to enhance my communication skills. Therefore, my responses would be limited and 
sometimes I might talk off the topic, slightly. I hope you understand. Some of the topics I would love to talk about:
               
* Answering your queries about video games (I'll try my best). Some example queries:
          * "What is a video game".
          * "Suggest me some video games".
          * "Tell me something interesting".
          * "What video game do you like".
          * You can query about a game by its name, I will try my best to answer.

*And, I can play Rock Paper Scissor with you. To play type: 'rockpaperscissor()' 
          """)


def greetings(): 
    print("""
   ██████╗ ██████╗  █████╗  ██████╗██╗     ███████╗
  ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██║     ██╔════╝
  ██║   ██║██████╔╝███████║██║     ██║     █████╗  
  ██║   ██║██╔══██╗██╔══██║██║     ██║     ██╔══╝  
  ╚██████╔╝██║  ██║██║  ██║╚██████╗███████╗███████╗
   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚══════╝

%****************************************************%    
%                      Options                       %
%        (Please Type the option as stated):         %
%              > help()        > exit()              %
%****************************************************%                    
          """)
    
    print("Hello There! I am Oracle. I love to talk about Video Games!!!") 


def cosine_inner(key, dt, query_dt):
        dot_ = 0
        query_ = 0
        kb_ = 0

        for k_q, v_q in query_dt.items():
            temp = dt.get(k_q, 0)
            dot_ += temp * v_q
            query_ += v_q * v_q
            # kb_ += temp * temp
        
        for k_kb, v_kb in dt.items():
            kb_ += v_kb * v_kb

        denom = math.sqrt(query_) + math.sqrt(kb_)
        cosine = dot_ /denom if denom != 0 else 0
        return cosine

def cosine_sim(query):
    query = word_tokenize(query)
    query = [word.lower() for word in query if word.lower() not in stop_words and word.isalnum()]
    # query = [WordNetLemmatizer().lemmatize(word) for word in query]
    q_len = len(query)
    query_dt = {wd:query.count(wd)/q_len for wd in set(query)}

    #cosine calculation
    result = 0
    result_doc = ''
    for key, dt in kb_cosine.items():
        if(type(dt) == list):
            for dt_ in dt:
                cosine = cosine_inner(key, dt_, query_dt)
                if result < cosine and cosine != 0:
                    result = cosine
                    result_doc = key

        else:    
            cosine = cosine_inner(key, dt, query_dt)

            if result < cosine and cosine != 0:
                result = cosine
                result_doc = key
    
    return (result_doc if result != 0 else 0)




def rps_score_print(bot_score, player_score):
    print(f"Current Standings: Oracle: {bot_score} vs {name}: {player_score}")

#this is the implementation of the rock paper scissor game
def rockPaperScissor():
    print("\n*************** Rock Paper Scissor ***************")
    print("*** Type : 'exit_game()' to exit the game. ***")
    game_val = ['rock', 'paper', 'scissor']
    count_game = 0
    while(True):
        count_game += 1
        print(f"This is game no. {count_game}")
        bot_score = 0
        player_score = 0
        while(True):
            print("\n")
            print("Rock...Paper...Scissor")
            g_inpt = input('> ')
            bot_input = random.choice(game_val)
            if(g_inpt == 'exit_game()') : return
            if(g_inpt == 'exit()'): exit_()
            if(g_inpt == 'help()'): help_()
            else:
                print(f"Oracle draw: {bot_input}.", end = " ")
                if(g_inpt.lower() not in game_val):
                    bot_score += 1
                    print("For invalid input the point goes to me!!!")
                elif(bot_input == 'rock' and g_inpt.lower() == 'paper'): player_score += 1
                elif(bot_input == 'paper' and g_inpt.lower() == 'rock'): bot_score += 1
                elif(bot_input == 'paper' and g_inpt.lower() == 'scissor'): player_score += 1
                elif(bot_input == 'scissor' and g_inpt.lower() == 'paper'): bot_score += 1
                elif(bot_input == 'rock' and g_inpt.lower() == 'scissor'): bot_score += 1
                elif(bot_input == 'scissor' and g_inpt.lower() == 'rock'): player_score += 1
                else:
                    print("The input is a draw")
                
                rps_score_print(bot_score, player_score)
                if(bot_score == 3 or player_score == 3):
                    if(bot_score == 3): print(f"***** {random.choice(greet_conv['player_lost_rpc'])} *****")
                    if(player_score == 3): print(f"***** {random.choice(greet_conv['bot_lost_rpc'])} *****")
                    print("Do you want to play another round? You can type: 'exit_game()' anytime to leave the game.")
                    print("\n")
                    break

if __name__ == '__main__':
    main()