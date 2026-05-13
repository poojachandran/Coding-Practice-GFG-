class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if flag:
            if a<0 and b<0 :
                return True
            else : 
                return False
        else:
         if (a>=0 and b<0) or (a<0 and b>=0):
               return True
         else:
                return False