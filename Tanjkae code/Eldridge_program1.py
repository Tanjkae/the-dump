import time
"""
Eldridge-program1.py
Logan Eldridge
print Hello World,your name,your class,and the date+time.
9/6/2022
notes: this program uses the inport time line
""" 
#print "hello, world"
print ("hello, world")

def main():
    #print name and class
    print("Logan Eldridge")
    print("CIS 110 Program 1")
    #print time Program was run
    print(time.asctime( time.localtime(time.time())))
main()