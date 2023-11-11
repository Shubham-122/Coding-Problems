def palindrome(s):
    stack1=[]
    stack2=[]
    for i in s:
        stack1.append(i)

    for j in range(len(s)-1,-1,-1):
        stack2.append(s[j])
    print(stack2)
    if(stack1==stack2):
        return 'Palindrome'
    else:
        return 'Not Palindrome'


def palindrome_stack(s):
    stack1=[]
    new=''
    for i in s:
        stack1.append(i)
    for i in range(len(s)):
        new+=stack1.pop()
    if(s==new):
        return 'Palindrome'
    else:
        return 'Not Palindrome'

    
        



s=input()
print(palindrome_stack(s))


