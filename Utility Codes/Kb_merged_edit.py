import pickle

know_base = pickle.load(open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Know_Base_Merged.p', 'rb'))


custom_dt = {
    'c1' : 'The first time I played this game, it took me by amaze. The gameplay, the atmosphere, everything is just perfect in this game.\
I highly recommend that you play this game.',
    'c2' : 'Sure here are some of the games I think you might like:',
    'c3' : 'As a chatbot I dont have personalized opinion',
    'c4' : 'I personally like laptop, because its versatile, and you can play and work on the same machine.',
    'c5' : 'Please type: help() to see the features I porivde.',
    'c6' : 'We all know who the noob is. I challenge you to rock-paper-scissor. To compete type: rockpaperscissor()',
    'c7' : 'My name is Oracle.',
    'c8' : 'Like a month or so.',
    'c9' : 'Nah, I do not have any basic human need.',
    'c10': 'Sure.',
    'c11': 'Okk',
    'c12': 'Thank you.',
    'c13': 'You can use Console like Play Station, Xbox, Nintendo, or PC',
    'c14': 'Sorry for the wrong response. As a rule based chatbot my reponses are limited.',
    'c15': 'Do you want to play rock paper scissor. Type: rockpaperscissor()',
    'c16': 'I am a pretty good and skilled player. My KD is always over 2',
    'c17': 'See you. To exit, please type: exit()',
    'c18': 'You are welcome.',
    'c19': 'Ok',
    'c20': 'To improve your performance you have to work hard',
    'c21': 'Ok, I understand.',
    'c22': 'I love PC.'
}


for k, v in custom_dt.items():
    if k not in know_base.keys():
        know_base[k] = v


pickle.dump(know_base, open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Know_Base_Merged_new.p', 'wb'))
