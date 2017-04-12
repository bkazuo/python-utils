s = 'hi'
print s[1]          ## i
print len(s)        ## 2
print s + ' there'  ## hi there


pi = 3.14
##text = 'The value of pi is ' + pi      ## NO, does not work
text = 'The value of pi is '  + str(pi)  ## yes

# "raw" string literal is prefixed by an 'r' and passes all the chars through without special treatment of backslashes
raw = r'this\t\n and that'
print raw     ## this\t\n and that

not_raw = 'this\t\n and that'
print not_raw

multi = """It was the best of times.
It was the worst of times."""
print multi

# String %
text = "%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down')
print text

# If line is long and you want to break down
text = ("%d little pigs come out or I'll %s and %s and %s"
 % (3, 'huff', 'puff', 'blow down'))
print(text)