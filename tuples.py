tuple = (1, 2, 'hi')
print len(tuple)  ## 3
print tuple[2]    ## hi
# tuple[2] = 'bye'  ## NO, tuples cannot be changed
tuple = (1, 2, 'bye')  ## this works
print tuple

# To createa a size-1 tuple, the lone element must be followed by a comma.
tuple = ('hi',)
print tuple

(x, y, z) = (42, 13, "hike")
print z  ## hike

