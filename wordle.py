target = list("hello".lower())

correct = False
letter_corr = 0
posi_corr = 0
ls = []
temp_ls = []
verified_target = target[:]
for i in range(6):
    temp_ls.clear()
    for j in range(len(target)):
        temp_ls.append("⬛️")
    print(" ".join(temp_ls))
for i in range(6):
    ls.append(temp_ls)
tmp_ls = temp_ls[:]
for i in range(len(tmp_ls)):
    tmp_ls[i] = "🟥"
count = 0
while not correct:
    
    guess = list(input("Enter your guess word(could be meaningless): ").lower())
    if len(guess) < len(target) :
        for i in range(len(ls)):
            print(" ".join(ls[i]))
        print("===========================================")
        print("Your guess's lenght is shorter than target,")
        print("             Please try again.             ")
        print("===========================================")
        continue
    elif len(guess) > len(target):
        for i in range(len(ls)):
            print(" ".join(ls[i]))
        print("===========================================")
        print("Your guess's lenght is longer than target,")
        print("             Please try again.             ")
        print("===========================================")
        continue
    if guess == verified_target :
        for i in range(len(tmp_ls)):
            tmp_ls[i] = "🟩"
        correct = True
    for i in range(len(target)):
        for j in range(len(guess)):
            if target[i] == guess[j]:
                if i == j:
                    tmp_ls[j] = "🟩"
                    guess[j] = "-"
                else:
                    tmp_ls[j] = "🟨"
                    guess[j] = "-"
                    break
    ls[count] = tmp_ls[:]
    if correct:
        for i in range(6-count-1):
            ls.pop()
    for i in range(len(ls)):
        print(" ".join(ls[i]))
    count +=1
    for i in range(len(tmp_ls)):
            tmp_ls[i] = "🟥"    
    if count == 6 and not correct:
        print("The number you can try is limited, try again later.")
        break         
if correct:
    print("===================================================")
    print("Congratuations, please wating for next word target.")
    print(f"===================|Wordle {count}/6|====================")