def utility(s):
    #code here
    for i in range(len(s)):
        if ((i==0) or (i%2 == 0)):
            print(s[i],end="")