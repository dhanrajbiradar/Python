#Reverse the string without slicing
def rev_string(string):
    rev_str=""         #empty string
    for i in string:
        rev_str=i+rev_str   #+ is used to concatinate string
    return rev_str

str="HELLO"     #use raw_input() function through keyboard
RevStr=rev_string(str)

print "reverse string is=",RevStr


