# Function to return precedence of operators
def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1


def infixToPostfix(s):
    st = []
    result = ""

    for i in range(len(s)):
        c = s[i]


        if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9'):
            result += c


        elif c == '(':
            st.append('(')

        elif c == ')':
            while st[-1] != '(':
                result += st.pop()
            st.pop()

        else:
            while st and (prec(c) < prec(st[-1]) or prec(c) == prec(st[-1])):
                result += st.pop()
            st.append(c)

    while st:
        result += st.pop()

    print(result)


exp = input()
infixToPostfix(exp)