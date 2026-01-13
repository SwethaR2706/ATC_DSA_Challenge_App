**IMPORTANT CODE FORMAT:**

Your code should ONLY contain the `solution` function definition. 

❌ **DO NOT:**
- Call the function yourself
- Print the result
- Add test code

✅ **CORRECT FORMAT:**
```python
def solution(nums, target):
    # Your code here
    return [0, 1]
```

❌ **WRONG FORMAT:**
```python
def solution(nums, target):
    return [0, 1]

# DON'T DO THIS:
nums = [2,7,11,15]
target = 9
result = solution(nums, target)
print(result)  # ← This causes errors!
```

The judging system will automatically call your function with test inputs and check the output.
