import textwrap

def count_sub_string_non_overlapping(string:str, substr):
    return string.count(substr)
def count_sub_string(string:str,substr):
    substr_len=len(substr)
    cnt=0
    for i in range(0,len(string)+1):
        if string[i:i+substr_len] == substr:
            cnt += 1
    return cnt
def swapcase(str):
    return str.swapcase()
    
def swapcase_custom(str):
    return ''.join([char.upper() if char.islower() else char.lower() for char in str])

def wrap_text(txt, max_width):
    return '\n'.join(textwrap.wrap(txt, max_width))

if __name__ == "__main__":
    cnt = count_sub_string_non_overlapping("ABCDCDC","CDC")
    print(cnt) # count 1
    cnt1= count_sub_string("ABCDCDC","CDC")
    print(cnt1)
    ls=[0,1,3,4,8]
    #ls.pop()
    #ls.remove(ls1)
    print(ls)
    ls.pop()
    print(ls)
    print(swapcase("The Told store 'A' was not never ending, therefore had left"))
    print(swapcase_custom("The Told store 'A' was not never ending, therefore had left"))
    print(wrap_text("The Told store 'A' was not never ending, therefore had left",4))