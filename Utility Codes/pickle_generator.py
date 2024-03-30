import pickle

greet_conv = {
    'name_que': ['What is your name?', 'Can I know your name, please?', 'Would you kindly share your name?'],
    'new' : ['It is nice to meet you.', 'I am happy that you chose me over chatGPT.', 'I cordially welcome you.'],
    'old' : ['I am happy to see you again.', 'I hope you are doing great.', 'Feels like it has been ages since we last met.'],
    'game_choice': ['That is a great game.', 'Great Choice!!!', 'Awsome, it is also in my wish list.'],
    'old_game' : ['How is your grinding going on', 'Are you still enjoing'],
    'player_lost_rpc': ["Go play Roblox.", "Hurrah, I won.!!!", "GG"],
    'bot_lost_rpc': ['You won because you are a hacker.', 'Only if I had a better PC, I would have won.', "Congrats you won."],
    'zero_prediction': ["I am having hard time understanding this query.", "Will you please rephrase your question?"],
    'low_prediction': ["Sorry, but I have limited knowledge in this area.", "Sorry, I am unable to answer this."],
    'req_more_info': ["Can you tell me more?", "Will you please elaborate?"],
    'greet_que_pos': ["I am happy you are enjoying it.", "Nice to hear that."],
    'greet_que_neg': ["I think you can take a break, and then you'll enjoy it again.", "I am sorry to hear that.", "That's sad"]
}


pickle.dump(greet_conv, open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/ChatBot Files/greetings_conv.p', 'wb'))
