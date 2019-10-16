import xml.etree.ElementTree
from collections import deque
x = "<feed xml:lang='en'> \
    <title>HackerRank</title> \
    <subtitle lang='en'>Programming challenges</subtitle> \
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/> \
    <updated>2013-12-25T12:00:00</updated> \
    </feed>"

x11 = '''<feed xml:lang='en'> 
       <title>HackerRank</title> 
       <subtitle lang='en'>Programming challenges</subtitle> 
  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/> 
  <updated>2013-12-25T12:00:00</updated> 
  <entry> 
  	<author gender='male'>Harsh</author> 
    <question type='hard'>XML 1</question> 
    <description type='text'>This is related to XML parsing</description> 
  </entry> 
</feed>'''

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    q = deque()
    q.append((elem, level+1))
    level = 0
    maxdepth = 0
    while len(q) > 0:
        for chd in elem.getchildren():
            q.append((chd, level+1))
        elem, level = q.pop()
        maxdepth = max(level, maxdepth)
        # print("elem is ", elem.tag)
        # print("level is ", level)
        # print("maxdepth is ", maxdepth)

    return maxdepth

node = xml.etree.ElementTree.ElementTree(xml.etree.ElementTree.fromstring(x11))
r = node.getroot()
depth (r, -1)
print(maxdepth)
