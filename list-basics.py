colors = ['red', 'blue', 'green']
print colors[0]    ## red
print colors[2]    ## green
print len(colors)  ## 3

b = colors # It does not copy the list

# FOR and IN
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print sum  ## 30

list = ['larry', 'curly', 'moe']
if 'curly' in list:
    print 'yay'

for i in range(100):
    print i

list = ['larry', 'curly', 'moe']
list.append('shemp')         ## append elem at end
print list

list.insert(0, 'xxx')        ## insert elem at index 0
print list  

list.extend(['yyy', 'zzz'])  ## add list of elems at end
print list  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print list.index('curly')    ## Return the index 2

list.remove('curly')         ## search and remove that element
list.pop(1)                  ## removes and returns 'larry'
print list  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']