def printIncreasingPower(x):
    #code here
    result=1
    count=1
    # Loop to jump in powers of 2
    while(result<=x):
        #code here
        result = count * count
        count+=1
        if(result <=x):
            print (result, end = " ")
        
       #code here