import pickle

#pickle to text

# kb = pickle.load(open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Know_Base_Merged.p', 'rb'))

# fhand = open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/kb_merged_Manual.txt', 'w')

# for k, v in kb.items():
#     fhand.write(f"{k}\t{v}\n")


#text to pickle
kb_manual = {}

fhand = open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/kb_merged_Manual.txt', 'r')
for line in fhand:
    line = line.strip()
    
    lt = line.split("\t")
    if(len(lt) == 1): continue
    key = lt[0]
    val = lt[1]

    if '<mct>' in val:
        lt1 = val.split('<mct>')
        val = tuple(lt1[:-1])

    kb_manual[key] = val

pickle.dump(kb_manual, open('OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Know_Base_Manual.p', 'wb'))