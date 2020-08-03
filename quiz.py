import random
def get_def_and_pop(word_list , ord_dict):                       
    random_index = random.randrange(len(word_list))
    word = word_list.pop(random_index)
    definition = words_Dictionary.get(word)
    return word, definition
def get_word_and_def(rawStr):                                 
    word, definition = rawStr.split(',' , 1)
    return word, definition
data = open("Vocabulary_list.csv" , "r")                            
words_List = data.readlines()
words_List.pop(0)                                                 
words_Set = set(words_List)
data = open("Vocabulary_set.csv" , "w")
data.writelines(words_Set)
words_Dictionary = dict()                                             
for rawStr in words_Set:
    word, definition = get_word_and_def(rawStr)
    words_Dictionary[word] = definition
while True:                                                      
    words_List = list(words_Dictionary)
    sel_list = []
    for x in range(4):
        word, definition = get_def_and_pop(words_List , words_Dictionary)
        sel_list.append(definition)
    random.shuffle(sel_list) 
    print(word)
    print("*******************************************************")
    for i, selection in enumerate(sel_list):
        print(i+1 , selection)   
    selection = int(input("Enter 1 2 3 or 4 ; 0 for Exit"))
    if sel_list[selection - 1] == definition:
        print("This is Correct ! \n") 
    elif selection == 0:
        exit(0)
    else:
        print("This is Incorrect")