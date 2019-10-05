def minion_game(string):
    # your code goes here
    stuart_score=0
    kevin_score=0
    kevin_vw=['A','E','I','O','U']
    for idx in range(len(string)):
        char = string[idx]
        if char in kevin_vw:
            kevin_score += 1
            kevin_substring=char
            print(char)
            print(string[idx+1:])
            for kevin_char in string[idx+1:]:
                print(kevin_char)
                kevin_substring += kevin_char 
                print(kevin_substring)
                kevin_score += 1
                print(kevin_score)
        else:
            stuart_score += 1
            stuart_substring= char
            for stuart_char in string[idx+1:]:
                stuart_substring += stuart_char 
                stuart_score += 1 
    if kevin_score > stuart_score:
        print("Kevin {} and stuart {} ".format(kevin_score, stuart_score))
    else:
        print("Stuart {} and Kevin {} ".format(stuart_score, kevin_score))

if __name__ == '__main__':
    s = 'BANANA'
    minion_game(s)
