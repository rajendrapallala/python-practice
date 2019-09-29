import re
'''
regual expresions 
  -- Non Repition special characters
     . zero or single character match (except new line)
     ^ beginging
     $ at end

  -- Repition special characters
     * zero or many of prevous chars
     + one or more previous character match
     ? zero or ONE previous character match
     {m} exact m number of previous char copies
     {m,n} min m number of previous char and max of n number of previous char copies
     {m,n}?  in non-greedy version, it will match only the min 
     *? , +? and ?? are in non-greedy versions of *, +, ?

  -- pattern defination chars
     [] represents set of chars, to match one of chars between [ and ]
     | or , for matching pattern a or pattern b
     () group identification and retrive this group using '\'group number
     (?:) non-capturing group
     ()? optional group


'''

if __name__ == "__main__":
    # simple match
    teststr = " some where test word present"
    if re.search("test", teststr):  #true
        print("the word 'test' found")
    
    if not re.match("test", teststr): #true , match find only at the begining
        print("the word 'test' not matched")
    
    if re.match(" some ", teststr): #true
        print(" the match worked when string searched for beginging word or entire string")

    if re.match("\ssome", teststr): #true
        print(" the match worked when string searched for beginging word or entire string")

