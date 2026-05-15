# Function to check if string
# starts and ends with 'gfg'
def gfg(S):
    b = S.lower()
    c = S.upper()
    bool1 = b.startswith('gfg') and b.endswith('gfg')
    bool2 = c.startswith('GFG') and c.endswith('GFG')
    if (bool1 and bool2):
        print("Yes")
    else:
        print("No")