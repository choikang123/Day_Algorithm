# 스택을 이용해 풀어야 함
import sys
input=sys.stdin.readline

while True:
    stack=[]
    is_flag=True
    str_list=input().rstrip()
    #종료조건 입력이 .라면 반복분 탈출하고 종료
    if str_list==".":
        sys.exit(0)
    else:
        for word in str_list:
            if word=="(":
                stack.append(word)
            elif word==")":
                # 비어있는데 뺄 수는 없으니까
                if not stack:
                    is_flag=False
                    break
                else:
                    if stack[-1]=="(":
                        stack.pop()
                    else:
                        is_flag=False
                        break
            elif word=="[":
                stack.append(word)
            elif word=="]":
                if not stack:
                    is_flag=False
                    break
                else:
                    if stack[-1]=="[":
                        stack.pop()
                    else:
                        is_flag=False
                        break
        # 스택이 비어있는데 빼려고 했거나 스택에 값이 들어있다면
        if not is_flag or stack :
            print("no")
        else:
            print("yes")

        # 스택에 비어있는게 두가지로 나뉨
        # 하나는 끝까지 for문을 돌고나서 스택이 비어있는지
        # 하나는