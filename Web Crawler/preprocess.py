import re

input_path = 'OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Initial_Files/'

val = 0
while val <= 121:
    val += 1
    filename = f"File_{val}.txt"
    try:
        fhand = open(input_path+filename, 'r')
    except:
        print(f"No file named {filename}")
    else:
        output_path = "OneDrive/Desktop/SEM_2/CS 6320/Practical/Project/Project_1/Files/Processed_Files/"
        file_out = f'Out_File_{val}.txt' 
        fout = open(output_path+file_out, 'w')

        end_punc = ['.', ',', '!', '?', '-', '_', ':', ';'] #If a line ends without these, a fullstop will be added to that line.
        text = '' #we're saving every paragraph from a link as one paragraph

        for line in fhand:
            temp = re.sub('\[.*?\]|\S{20,}|\n', "", line) #the pattern will be replaced with empty string
            temp = re.sub('\s{2,}', " ", temp) #any whitespace of two or more will be replaced with one
            temp = temp.strip()
            if len(temp)>0 and temp[-1] not in end_punc: #this checks if a line ends without punctuation
                temp += " "
            text += temp

        text = ''.join([i if ord(i)<128 else '' for i in text]) #Only keeping Ascii characters


        fout.write(text.strip())