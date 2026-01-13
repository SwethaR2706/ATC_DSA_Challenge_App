# DSA Coding Challenge - User Guide

## Getting Started

### Launching the Application

1. Double-click `DSA_Challenge.exe` to start the application
2. The registration screen will appear

### Registration

![Registration Screen]

1. **Enter Your Name**: Type your full name
2. **Enter Your Email**: (Optional) Provide your email address
3. **Select Language**: Choose either Python or Java
   - ⚠️ **Important**: You cannot change language after starting the contest
   - For Java: Ensure JDK is installed on your system
4. Click **"Start Contest"** to begin

## Contest Interface

### Main Window Layout

The contest interface consists of:

1. **Top Bar**
   - Participant name and selected language
   - Contest timer (counts down from 2 hours)
   - Current score out of 100

2. **Left Panel - Problem List**
   - Shows all 10 problems
   - Click any problem to view it
   - Format: "Problem Number. Problem Title"

3. **Right Panel - Problem View**
   - **Problem Description**: Full problem statement with examples
   - **Code Editor**: Write your solution here
   - **Submit Button**: Test your code
   - **Result Display**: Shows verdict after submission

### Solving Problems

#### Step 1: Select a Problem
- Click on any problem from the left panel
- The problem description will load on the right

#### Step 2: Read the Problem
- Carefully read the problem statement
- Note the input/output format
- Check the examples
- Understand the constraints

#### Step 3: Write Your Code
- The editor will have starter code with the function signature
- **Important**: Your function must be named `solution`
- Write your logic inside the `solution` function
- Do not change the function name or signature

**Python Example:**
```python
def solution(nums, target):
    # Your code here
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
```

**Java Example:**
```java
class Solution {
    public int[] solution(int[] nums, int target) {
        // Your code here
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[] {seen.get(complement), i};
            }
            seen.put(nums[i], i);
        }
        return new int[0];
    }
}
```

#### Step 4: Submit Your Code
- Click the **"Submit Code"** button
- Wait for the verdict (usually takes 1-5 seconds)
- Check the result displayed below the submit button

### Understanding Verdicts

| Verdict | Meaning | Score |
|---------|---------|-------|
| ✓ **Accepted** | All test cases passed | +10 marks |
| ✗ **Wrong Answer** | Some test cases failed | 0 marks |
| ✗ **Compilation Error** | Code has syntax errors | 0 marks |
| ✗ **Runtime Error** | Code throws an exception | 0 marks |
| ✗ **Time Limit Exceeded** | Code takes longer than 5 seconds | 0 marks |

### Scoring System

- Each problem is worth **10 marks**
- Total possible score: **100 marks**
- Only **Accepted** submissions earn marks
- You can submit multiple times for the same problem
- Best submission counts (if you solve it correctly later)

### Contest Timer

- Contest duration: **2 hours** (7200 seconds)
- Timer is displayed in the top-right corner
- Format: HH:MM:SS
- Contest automatically ends when timer reaches 00:00:00
- You can manually end the contest early by clicking **"End Contest"**

### Ending the Contest

**Automatic End:**
- Contest ends when timer reaches zero
- Results screen appears automatically

**Manual End:**
- Click **"End Contest"** button
- Confirm when prompted
- Results screen will appear

## Results Screen

After the contest ends, you'll see:

### Your Performance

1. **Total Score**: Your final score out of 100
2. **Problems Solved**: Number of problems you solved correctly
3. **Performance Level**: 
   - 🥇 **Gold**: Score ≥ 80 (8+ problems)
   - 🥈 **Silver**: Score 50-79 (5-7 problems)
   - 🥉 **Bronze**: Score < 50 (< 5 problems)

### Submission Summary

- Shows your best submission for each problem
- Lists problems you didn't attempt
- Format: "Problem X: Verdict (Score marks)"

## Tips for Success

### General Tips

1. **Read Carefully**: Understand the problem before coding
2. **Check Examples**: Verify your logic with given examples
3. **Test Edge Cases**: Think about special cases
4. **Manage Time**: Don't spend too long on one problem
5. **Submit Early**: Get feedback on your approach

### Python-Specific Tips

- Use built-in functions and data structures
- Remember to return the result, not print it
- Use `pass` as placeholder while thinking
- Common imports are available: `json`, `math`, `collections`, etc.

### Java-Specific Tips

- Ensure JDK is installed before starting
- Use proper data types for return values
- Remember to import necessary classes
- Arrays and ArrayLists are commonly used

### Common Mistakes to Avoid

❌ **Changing function name**
```python
def twoSum(nums, target):  # Wrong! Must be 'solution'
```

❌ **Printing instead of returning**
```python
def solution(nums, target):
    print([0, 1])  # Wrong! Use return
```

❌ **Infinite loops**
```python
def solution(n):
    while True:  # Will cause Time Limit Exceeded
        pass
```

❌ **Not handling edge cases**
```python
def solution(nums):
    return nums[0]  # What if nums is empty?
```

## Troubleshooting

### Problem: Code won't submit
- **Check**: Is the contest still active?
- **Check**: Did you write any code?
- **Solution**: Ensure timer hasn't reached zero

### Problem: Getting Compilation Error
- **Check**: Syntax errors in your code
- **Check**: Function name is `solution`
- **Check**: Proper indentation (Python)
- **Check**: Missing semicolons or braces (Java)

### Problem: Getting Runtime Error
- **Check**: Array index out of bounds
- **Check**: Division by zero
- **Check**: Null pointer exceptions
- **Solution**: Add error handling and validation

### Problem: Getting Time Limit Exceeded
- **Check**: Infinite loops in your code
- **Check**: Algorithm complexity (should be efficient)
- **Solution**: Optimize your algorithm

### Problem: Getting Wrong Answer
- **Check**: Logic errors in your code
- **Check**: Test with the given examples
- **Check**: Consider edge cases
- **Solution**: Debug and test more thoroughly

## Keyboard Shortcuts

- **Tab**: Indent code
- **Shift + Tab**: Unindent code
- **Ctrl + A**: Select all code
- **Ctrl + C**: Copy
- **Ctrl + V**: Paste
- **Ctrl + Z**: Undo
- **Ctrl + Y**: Redo

## Good Luck!

Remember:
- Stay calm and focused
- Read problems carefully
- Test your code mentally before submitting
- Manage your time wisely
- Don't give up on difficult problems

**May the best coder win!** 🏆
