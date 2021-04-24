#Malik Campbell; DS4A Python Program Spring 2021

def translate(file):
    
    """
   - Translate words from a .txt file into Lolspeak, the language of lolcats.
   
   - Arguments: Takes in a file, program promts user to enter filename
   
   - Outputs:   A new file, which is the original translated to Lolspeak and
                saved with _lolcat.txt at the end
    """
    import urllib.request,json

    # Import translation dictionary
    # Dictionary provided by https://github.com/normansimonr/Dumb-Cogs/blob/master/lolz/data/tranzlashun.json
    
    dict = urllib.request.urlopen("https://raw.githubusercontent.com/normansimonr/Dumb-Cogs/master/lolz/data/tranzlashun.json")
    translator = json.loads(dict.read())
    
    #print(translator) #tester

    #Iterate through each word in a file and replace it with its pair in the dictionary
    #Elements that do not have a pair in the dictionary will be appended without change
    #opening file and create new list to store the translated phrase
    
    with open(file, "r") as f:
        file_lines = f.readlines()       
    translated = []
    
    #iterate through each line and translate the words
    for line in file_lines:
        
        #splitting the words by their spaces 
        for word in line.split(" "): 
            if word.lower() in translator:
                translated.append(translator[word.lower()])
            else:
                translated.append(word.lower())
                   
    #save translated to a new file
    #saves file in working directory
    prefix = file.split("/")[-1].split(".")[0]
    
    with open(prefix + "_lolcat.txt" , "w") as lolcat_file:
        for word in translated:
            lolcat_file.write(word + " ")


                       
def main():
    import os
    file = input("Welcome to the lolspeak translator! \n---------------------------------\nEnter the path to the .txt file you would like to translate:\n")
    
    #valid file check
    while os.path.isfile(file) == False:
        if (file == "Q") and (os.path.isfile(file)==False) :
            os._exit(0)
        file = input("Couldn't find that file! Please enter a valid path, or type Q to quit:\n")
     
    #translate 
    translate(file)
    print("Success! Saved to the current working directory.")


if __name__ == '__main__':
    main()