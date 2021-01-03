#          e Leo Coding challenge
# 2 variables, print which is higher/the same - completed
# 3 var, a/b/c, print in order from largest to smallest -completed
a = 7
b = 7
c = 7
if a > b and a > c:
    print("a is the largest number")
    if b > c:
        print("b is the middle number")
        print("c is the smallest number")
    if b < c:
        print("c is the middle number")
        print("b is the smallest number")
if b > a and b > c:
    print("b is the largest number")
    if a > c:
        print("a is the middle number")
        print("c is the smallest number")
    if a < c:
        print("c is the middle number")
        print("a is the smallest number")

if c > a and c > b:
    print("c is the largest number")
    if a > b:
        print("a is the middle number")
        print("b is the smallest number")
    if a < b:
        print("b is the middle number")
        print("a is the smallest number")

if a == b == c:
    print("ALL NUMBERS ARE THE SAME!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
if a == b == c == 7:
    print("JACKPOT!!!!!!!!!!!!! ALL NUMBERS ARE 7!!!!!!!!!!!!!!!!!!!!!")

