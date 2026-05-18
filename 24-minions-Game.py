def minion_game(string):
    vowels_set = set("AEIOU")
    stuarts_score = 0
    kevins_score = 0
    n = len(string)
    for i, char in enumerate(string):   # this will traverse throught the string
        if char in vowels_set:          # this will check if it's a vowel then it will be added to the kevin's score
            kevins_score += n - i       # n - i is for len(string) - character[index], if i is at 2 then 6 - 2 = 4 (4 is the score) we moved 3 (0,1,2) positons in the string ,  if the char at that position is vowel then +4 score to kevin else to stuart 
        else: 
            stuarts_score += n - i      # this will add score to stuart's score if its not from vowels group 
    
    if kevins_score > stuarts_score: 
        print('Kevin', kevins_score)
    elif stuarts_score > kevins_score:
        print('Stuart', stuarts_score)
    else :
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)