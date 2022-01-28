target = list("quotes".lower())

correct = False
letter_corr = 0
posi_corr = 0
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
for i in range(6):
    temp_ls.clear()
    for j in range(len(target)):
        temp_ls.append("⬛️")
    print("         "," ".join(temp_ls))
print("\n")
print("","  ".join(alpha1))
print(" ".join(clue1))
print("","  ".join(alpha2))
print(" ".join(clue2))
print("===================================================")
for i in range(6):
    ls.append(temp_ls)
tmp_ls = temp_ls[:]
for i in range(len(tmp_ls)):
    tmp_ls[i] = "🟥"
count = 0
while not correct:
    
    guess = list(input("Enter your guess word(could be meaningless): ").lower())
    print("===================================================")
    if len(guess) < len(target) :
        for i in range(len(ls)):
            print("         "," ".join(ls[i]))
        print("\n")
        print("","  ".join(alpha1))
        print(" ".join(clue1))
        print("","  ".join(alpha2))
        print(" ".join(clue2))
        print("===================================================")   
        print("    Your guess's lenght is shorter than target,")
        print("                 Please try again.             ")
        print("===================================================")
        continue
    elif len(guess) > len(target):
        for i in range(len(ls)):
            print("         "," ".join(ls[i]))
        print("\n")
        print("","  ".join(alpha1))
        print(" ".join(clue1))
        print("","  ".join(alpha2))
        print(" ".join(clue2))
        print("===================================================")
        print("    Your guess's lenght is longer than target,")
        print("                 Please try again.             ")
        print("===================================================")
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
                    for i in range(len(alpha1)):
                        if alpha1[i].lower() == guess[j]:
                            clue1[alpha1.index(guess[j].upper())] = "🟨"
                        if alpha2[i].lower() == guess[j]:
                            clue2[alpha2.index(guess[j].upper())] = "🟨"
                    tmp_ls[j] = "🟨"
                    guess[j] = "-"

                    break
                else:
                    if (guess[j]).upper() in alpha1:
                        if clue1[alpha1.index(guess[j].upper())] != "🟩":
                            clue1[alpha1.index(guess[j].upper())] = "🟥"
                    elif (guess[j]).upper() in alpha2:
                        if clue2[alpha2.index(guess[j].upper())] != "🟩":
                            clue2[alpha2.index(guess[j].upper())] = "🟥"
    ls[count] = tmp_ls[:]
    if correct:
        for i in range(6-count-1):
            ls.pop()
    for i in range(len(ls)):
        print("         "," ".join(ls[i]))
    print("\n")
    print("","  ".join(alpha1))
    print(" ".join(clue1))
    print("","  ".join(alpha2))
    print(" ".join(clue2))
    if not correct:
        print("===================================================")
    count +=1
    for i in range(len(tmp_ls)):
            tmp_ls[i] = "🟥"    
    if count == 6 and not correct:
        print("The number you can try is limited, try again later.")
        break
    target = verified_target[:]         
if correct:
    print("===================================================")
    print("Congratuations, please wating for next word target.")
    print(f"===================|Wordle {count}/6|====================")