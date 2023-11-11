from collections import deque

def isValid(s):
    hm={"(":")","{":"}","[":"]"}
    st=[]
    for i in s:
        if i in hm:
            st.append(i)
                
        else:
            if len(st)==0:
                return "false"

            elif hm[st[-1]]==i:
                st.pop()
            else:
                return "false"
       
    if len(st)==0:
        return 'true'
    else:
        return 'false'

        
string=input()
print(isValid(string))
