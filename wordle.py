def clues():
    print("")
    print("","  ".join(alpha1))
    print(" ".join(clue1))
    print("","  ".join(alpha2))
    print(" ".join(clue2))
    return
def line():
    print("===================================================")
    return
def get_word(m, M): 
    w_list = words.words()
    for_random = []
    for i in w_list:
        if len(i) >= m and len(i) <= M :
            for_random.append(i)
    return random.choice(for_random)
    # w_list = ["amogus"] 
    # response_a = requests.get("https://zenquotes.io/api/random") 
    # json_data_a = json.loads(response_a.text) 
    # word_a = json_data_a[0]['q'].split() 
    # for i in word_a: 
    #     if len(i) >= m and len(i) <= M: 
    #         if i.isalpha() and i.islower(): 
    #             w_list.append(i)
    # a = random.choice(w_list[1:]) 
    # response_b = requests.get(f"https://api.datamuse.com/words?ml={a}") 
    # json_data_b = json.loads(response_b.text) 
    # for j in range(len(json_data_b)): 
    #     i = json_data_b[j]["word"] 
    #     if len(i) >= m and len(i) <= M: 
    #         if i.isalpha() and i.islower(): 
    #             w_list.append(i)
    # return random.choice(w_list)

import random
import requests
import json
from nltk.corpus import words



wordle_target = get_word(4,6)
target = list(wordle_target)
correct = False
ls = []
temp_ls = []
verified_target = target[:]
alpha1 = []
alpha2 = []
clue1 = []
clue2 = []
for i in range(13):
    alpha1.append(chr(65+i))
    alpha2.append(chr(78+i))

for i in range(len(alpha1)):
    clue1.append("⬛️")
    clue2.append("⬛️")
for j in range(len(target)):
        temp_ls.append("⬛️")
print("")
for i in range(6):
    ls.append(temp_ls)
    print("         "," ".join(temp_ls))
clues()
line()
tmp_ls = temp_ls[:]
for i in range(len(tmp_ls)):
    tmp_ls[i] = "🟥"
count = 0
while not correct:  
    guess = list(input("Enter your guess word(could be meaningless): ").lower())
    line()
    if "".join(guess) not in words.words() :
        print("")
        for i in range(len(ls)):
                print(f"         "," ".join(ls[i]))
        clues()
        line()
        print("        There is no this word in library.")
        line()
        continue
    if len(guess) != len(target):
        print("")
        for i in range(len(ls)):
                print("         "," ".join(ls[i]))
        clues()
        if len(guess) < len(target):
            line()  
            print("    Your guess's length is shorter than target,")
            print("                 Please try again.             ")
            line()
            continue
        elif len(guess) > len(target):
            line()
            print("    Your guess's length is longer than target,")
            print("                 Please try again.             ")
            line()
            continue
    if guess == verified_target :
        correct = True
    for i in range(len(target)):
        if guess[i] == target[i]:
            if guess[i].upper() in alpha1:
                clue1[alpha1.index(guess[i].upper())] = "🟩"
            elif guess[i].upper() in alpha2:
                clue2[alpha2.index(guess[i].upper())] = "🟩"
            tmp_ls[i] = "🟩"
            guess[i] = "-"
            target[i] = "*"
    if not correct:
        for i in range(len(target)):
            for j in range(len(guess)):
                if target[i] == guess[j]:
                    if guess[j].upper() in alpha1 and clue1[alpha1.index(guess[j].upper())] != "🟩":
                        clue1[alpha1.index(guess[j].upper())] = "🟨"
                    elif guess[j].upper() in alpha2 and clue2[alpha2.index(guess[j].upper())] != "🟩":
                        clue2[alpha2.index(guess[j].upper())] = "🟨"
                    tmp_ls[j] = "🟨"
                    guess[j] = "-"
                    break
                else:
                    if (guess[j]).upper() in alpha1:
                        if clue1[alpha1.index(guess[j].upper())] != "🟩" and clue1[alpha1.index(guess[j].upper())] != "🟨":
                            clue1[alpha1.index(guess[j].upper())] = "🟥"
                    elif (guess[j]).upper() in alpha2:
                        if clue2[alpha2.index(guess[j].upper())] != "🟩" and clue2[alpha2.index(guess[j].upper())] != "🟨":
                            clue2[alpha2.index(guess[j].upper())] = "🟥"
    ls[count] = tmp_ls[:]
    if correct:
        for i in range(6-count-1):
            ls.pop()
    print("")
    for i in range(len(ls)):
        print("         "," ".join(ls[i]))
    clues()
    if not correct:
        line()
    count +=1
    for i in range(len(tmp_ls)):
            tmp_ls[i] = "🟥"    
    if count == 6 and not correct:
        print("The number you can try is limited, try again later.")
        print('''          The target's word is "{}".             '''.format("".join(verified_target)))
        line()
        break
    target = verified_target[:]         
if correct:
    line()
    print("Congratuations, please wait for next word target.")
    print(f"==================|Wordle {count}/6|=====================")