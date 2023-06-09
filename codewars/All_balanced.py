import re
# def balanced_parens(n):
#     result =[]
#     for i in range(1, n+1):
#         a='('*i
#         b=[['(']*(n-i),[')']*n]
#         #print(b)
#         for _ in range(len(b[0])+len(b[1])):
#             if a.count('(')-a.count(')')==0:
#                 a+=b[0].pop()
#             else:
#                 a+=b[1].pop()
#         result.append(a)
#     print(result)

def balanced_parens(n):
    result =[]
    if n==0:
        return ['']
    if n==1:
        return ['()']
    else:

        for el in balanced_parens(n-1):
            for _ in range(2):
                result.append(''.join(['('+el+')']))
            result.append(el+'()')
            result.append('()'+el)
        for i in range(2,n):
            for x in balanced_parens(i):
                for y in balanced_parens(n-i):
                    result.append(''.join([x + y]))







    return list(set(result))

#print(balanced_parens(4))

a = ['(((())))', '((()()))', '((())())', '((()))()',
     '(()(()))', '(()()())', '(()())()', '(())()()',
     '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']
b = ['(((())))', '((()()))', '((())())', '((()))()',
     '(()(()))', '(()()())', '(()())()', '(())(())',
     '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']
c = ['((((()))))', '(((()())))', '(((())()))', '(((()))())', '(((())))()',
 '((()(())))', '((()()()))', '((()())())', '((()()))()', '((())(()))',
 '((())()())', '((())())()', '((()))(())', '((()))()()', '(()((())))',
 '(()(()()))', '(()(())())', '(()(()))()', '(()()(()))', '(()()()())',
 '(()()())()', '(()())(())', '(()())()()', '(())((()))', '(())(()())',
 '(())(())()', '(())()(())', '(())()()()', '()(((())))', '()((()()))',
 '()((())())', '()((()))()', '()(()(()))', '()(()()())', '()(()())()',
 '()(())(())', '()(())()()', '()()((()))', '()()(()())', '()()(())()',
 '()()()(())', '()()()()()']
print(set(b)-set(balanced_parens(4)))
print(set(c)-set(balanced_parens(12)))