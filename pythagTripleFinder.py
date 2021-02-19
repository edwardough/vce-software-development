mx = int(input("What's the maximum number you want to search up to? "))
# increment max otherwise it won't be included in the search
mx += 1
for a in range(1,mx):
    for b in range(1,mx):
        for c in range(1,mx):
            lhs = a**2 + b**2
            rhs = c**2
            if lhs == rhs:
                print("Pythag triple found!",a,b,c)
