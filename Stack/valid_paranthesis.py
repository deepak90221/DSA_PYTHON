def isBalanced(s):
    st = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            st.append(s[i])
        else:
            if st and (
                (st[-1] == '(' and s[i] == ')') or
                (st[-1] == '{' and s[i] == '}') or
                (st[-1] == '[' and s[i] == ']')
            ):
                st.pop()
            else:
                return False
    return len(st)==0

if __name__ == "__main__":
    s = input()
    print("Yes" if isBalanced(s) else "No")
