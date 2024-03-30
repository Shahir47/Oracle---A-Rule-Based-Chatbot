import pickle

forbidden_link = ['https://en.wikipedia.org//wiki/Hierarchical_file_system', 'https://en.wikipedia.org//wiki/Wikipedia:User_pages',\
                  'https://en.wikipedia.org//wiki/Wikipedia:PROJGUIDE#Task_forces', 'https://en.wikipedia.org//wiki/Wikipedia:Community_portal'\
                  'https://en.wikipedia.org//wiki/File:Toolo_church-Helsinki1.jpg', 'https://en.wikipedia.org//wiki/Wikipedia:WikiProject_Council/Directory/Science#Economics'\
                  , 'https://en.wikipedia.org//wiki/Category:WikiProjects', 'https://en.wikipedia.org//wiki/T%C3%B6%C3%B6l%C3%B6', 'https://en.wikipedia.org//wiki/T%C3%B6%C3%B6l%C3%B6',\
                    'https://en.wikipedia.org//wiki/ISO_7002', 'https://en.wikipedia.org//wiki/Palohein%C3%A4', 'https://en.wikipedia.org//wiki/Palohein%C3%A4',\
                        ]


fobidden_wiki_link = ['/wiki/Main_Page', '/wiki/Wikipedia:Contents', '/wiki/Portal:Current_events', '/wiki/Special:Random', '/wiki/Wikipedia:About', '/wiki/Help:Contents',\
                      '//en.wikipedia.org/wiki/Wikipedia:Contact_us', '/wiki/Help:Introduction', '/wiki/Wikipedia:Community_portal', '/wiki/Special:RecentChanges',\
                        '/wiki/Wikipedia:File_upload_wizard', '/wiki/Main_Page', '/wiki/Special:Search', '/wiki/Help:Introduction', '/wiki/Special:MyContributions',\
                        '/wiki/Special:MyTalk']

pickle.dump(forbidden_link, open("OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Utility Files/forbidden_link.p", 'wb'))
pickle.dump(fobidden_wiki_link, open("OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Utility Files/forbidden_wiki_link.p", 'wb'))


