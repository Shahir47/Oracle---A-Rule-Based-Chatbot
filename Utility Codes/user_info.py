import pickle

user_info = {}

user_info['shahir'] = {
    'name': 'SHAHIR',
    'favtGame': 'Apex Legends',
    'lastConv': ''
}

pickle.dump(user_info, open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/ChatBot Files/user_info.p', 'wb'))

# user_info = pickle.load(open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/ChatBot/user_info.p', 'rb'))


# print(user_info)