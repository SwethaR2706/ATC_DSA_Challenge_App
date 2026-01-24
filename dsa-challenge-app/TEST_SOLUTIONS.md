# DSA Challenge - Solutions

Use these solutions to verify that the Code Execution System is working correctly for both Python and Java.

## 1. Basic Array Sum (Easy)
**Goal**: Calculate sum of all elements.

### Python
```python
def solution(nums):
    return sum(nums)
```

### Java
```java
class Solution {
    public int solution(int[] nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return sum;
    }
}
```

---

## 2. Find Maximum Element (Easy)
**Goal**: Find the largest element in the array.

### Python
```python
def solution(nums):
    if not nums:
        return 0
    return max(nums)
```

### Java
```java
class Solution {
    public int solution(int[] nums) {
        if (nums.length == 0) return 0;
        int max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > max) {
                max = nums[i];
            }
        }
        return max;
    }
}
```

---

## 3. Count Even Numbers (Easy)
**Goal**: Count number of even integers.

### Python
```python
def solution(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count
```

### Java
```java
class Solution {
    public int solution(int[] nums) {
        int count = 0;
        for (int num : nums) {
            if (num % 2 == 0) {
                count++;
            }
        }
        return count;
    }
}
```

---

## 4. Reverse String (Medium)
**Goal**: Reverse the given string.

### Python
```python
def solution(s):
    return s[::-1]
```

### Java
```java
class Solution {
    public String solution(String s) {
        return new StringBuilder(s).reverse().toString();
    }
}
```

---

## 5. Check Palindrome (Medium)
**Goal**: Check if string reads same backwards.

### Python
```python
def solution(s):
    return s == s[::-1]
```

### Java
```java
class Solution {
    public boolean solution(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
```

---

## 6. Factorial Calculation (Medium)
**Goal**: Calculate n!

### Python
```python
def solution(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

### Java
```java
class Solution {
    public int solution(int n) {
        if (n <= 1) return 1;
        int result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}
```

---

## 7. Binary Search (Hard)
**Goal**: Find target index in sorted array or -1.

### Python
```python
def solution(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
```

### Java
```java
class Solution {
    public int solution(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return -1;
    }
}
```

---

## 8. Bubble Sort (Hard)
**Goal**: Sort array using Bubble Sort.

### Python
```python
def solution(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
```

### Java
```java
class Solution {
    public int[] solution(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (nums[j] > nums[j + 1]) {
                    // swap
                    int temp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = temp;
                }
            }
        }
        return nums;
    }
}
```

---

## 9. Find Missing Number (Hard)
**Goal**: Find missing number in 0..n.

### Python
```python
def solution(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
```

### Java
```java
class Solution {
    public int solution(int[] nums) {
        int n = nums.length;
        int expectedSum = n * (n + 1) / 2;
        int actualSum = 0;
        for (int num : nums) {
            actualSum += num;
        }
        return expectedSum - actualSum;
    }
}
```

---

## 10. Two Sum (Hard)
**Goal**: Find array indices of two numbers that add to target.

### Python
```python
def solution(nums, target):
    prev_map = {}  # val -> index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return []
```

### Java
```java
import java.util.HashMap;

class Solution {
    public int[] solution(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (map.containsKey(diff)) {
                return new int[] { map.get(diff), i };
            }
            map.put(nums[i], i);
        }
        return new int[0];
    }
}
```
