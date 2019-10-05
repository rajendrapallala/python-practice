from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
from collections import Counter
from collections import deque

def namedtup_example():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    nostds = 5
    fields="ID         MARKS      NAME       CLASS"
    cols=namedtuple("cols",",".join(fields.split()))
    l = list()
    s=0
    vals="1          97         Raymond    7\n2          50         Steven     4\n3          91         Adrian     9\n4          72         Stewart    5\n5          80         Peter      6"
    for line in vals.split('\n'):
        a=cols(*line.split())
        s += int(a.MARKS)
    print(s/nostds)

def ordereddict():
    n = int(input())
    d = OrderedDict()
    for i in range(n):
        key, val = input().rsplit(maxsplit=1)
        d[key] = d.setdefault(key,0) + int(val)
    for i1,i2 in d.items():
        print(i1, i2)


if __name__ == "__main__":

    ############################# Counter ###########################################
    print("In collection practice module")

    str=" I've recently tried to switch from Eclipse to IntelliJ as a debugger for my university course, and I'm really enjoying the auto-completion, Chronon backwards debugging and other nice features. But there's one thing that bugs the living hell out of me: I just want to run the current file! \
    In Eclipse, the \"Run\" button was intelligent enough to simply run the current file if it contained a main method, and use the last-ran file otherwise. But in IntelliJ, just running a file is much more complicated. You have to create a Run Configuration of the right file, and then select that Run Configuration, instead of just opening the file you want. This is a big hassle for me, especially since I have many different classes with main methods in most homeworks and projects. \
    I found that on Macs, Ctrl + FN + Shift + F10 will \"Run Context Configuration\", which is almost what I'm looking for. But for some reason, this key binding doesn't have an equivalent toolbar button that switches to the context configuration and just runs it, which would solve all my problems! Can anyone help me out? \
    "
    # start with empty counter and add words like x[word] = x[word] + 1 ... /
    # this is taking defaultdict object and when we first try to query key  x[word], /
    # key gets added then value will be set to 1 and then value gets increamented if same key encountered
    x=Counter()
    for word in str.split():
        x[word] += 1
    print(x)

    # Instantiate counter object with list
    c=Counter(str.split())
    print(c)
    print(c.most_common(10))

    print(sum(c.values()))

    print(list(c))
    print(list(c.items()))
    print(c.clear())
    print(c)

    # Counter with key value pairs
    kv = Counter(first=1, second=2)
    print(kv)
    kv2 = Counter({"first":1, "second":2})
    print(kv2)
    #both result in   Counter({'second': 2, 'first': 1})

    ############################# Deque ###########################################
    dq = deque("test")
    dq.append(" after")
    dq.appendleft("before ")
    print(dq)
    #deque(['before ', 't', 'e', 's', 't', ' after'])

    dq.popleft()
    print(dq)
    #deque(['t', 'e', 's', 't', ' after'])

    ############################# defaultdict ###########################################
    dict = defaultdict(int)
    print(dict["test"])

    dict1 = defaultdict(lambda:"")
    print(dict1["test"])
    # never throws KeyError.. if key not already present  it assigns the default object.
    #object could be an int or any other fuction

    ############################# OrderedDict ###########################################

    od = OrderedDict()
    od["first"]=1
    od["second"]=2

    od1 = OrderedDict()
    od1["second"]=2
    od1["first"]=1

    print (od , "\n" , od1)
    # od1 not equal to od .. it would be equal if its normal dict

    ############################# NamedTuple ###########################################

    Dog=namedtuple("x", "att1  att2 att3")
    d = Dog(att1=3, att2=4, att3=5)
    print(d.att1)
    print(d[0])
    namedtup_example()
