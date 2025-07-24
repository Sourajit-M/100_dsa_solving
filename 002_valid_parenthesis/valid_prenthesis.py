from collections import deque
def valid_parenthesis(str):
  stack = deque()

  for ch in str:
    if ch in "({[":
      stack.append(ch)
    else:
      if not stack:
        return False
      top = stack[-1]
      if (ch==')' and top=='(') or (ch=='}' and top=='{')  or (ch==']' and top=='[') :
        stack.pop()
      else:
        return False
      
  return not stack

str = "({[]})"
print(valid_parenthesis(str)) 