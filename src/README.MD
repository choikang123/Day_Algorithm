### 구현
단순 구현 문제에서 flag를 쓰지 않고 문제를 풀기 위해서는 <br>
negative check을 먼저해서 아닌경우에는 break를 통해 for문을 바로 나가게 하는 것이 팁<br>
처음부터 다 맞는지 확인하면 중간에 틀린거 찾아도 flag로 체크만 해두고 뒤에 불필요한 연산까지 계속 수행해야해서 비효율적


---

### 💻 코드로 보는 시야의 진화

**❌ "이게 맞아?" 를 묻는 방식 (플래그 억지로 쓰기)**

```python
is_perfect = False
for p in problem:
    if p in tool_box:
        is_perfect = True  # 맞는 걸 확인하고 깃발을 듦
    else:
        is_perfect = False # 틀린 걸 확인하고 깃발을 꺾음
        break

```

**✅ "이거 아니지? 당장 나가!" 를 묻는 방식 (님의 깨달음 / 플래그 소멸)**

```python
for p in problem:
    if p not in tool_box:  # 💡 "어? 이거 상자에 없네? (아니지?)"
        break              # 💡 "그럼 이 상자는 가망 없어! 당장 나가!!"

하실까요, 아니면 이 깨달음을 무기 삼아 [연산자 끼워넣기] 풀어보기
```
