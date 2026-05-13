class Solution:
    def utility(self, a, b, opr):
        # code here
        match opr:
            case 1:
                c=a+b
                print(c)
            case 2:
                c=a-b
                print(c)
            case 3:
                c=a*b
                print(c)
            case _:
                print("Invalid Input")