# n =int(input("Enter n: "))
# elements=[]
# for i in range(n):
#     val = int(input(f"Enter number {i+1}: "))
#     elements.append(val)
# print(f"array elements are: {elements}")
# print(f"sorted array are: {sorted(elements)}")
# sum = 0
# def sum_elements(elements):
#     for i in range(len(elements)):
#         sum += element[i]
#         return sum
# print(f"sum of all elements are: {sum_elements()}")
# k = int(input(f"Enter kth max to find: "))
# new_elements = sorted(elements)
# new_elements_reversed = elements[::-1]
# print(f"kth max of sorted elements is: {new_elements[-k]}, reversed array are: {new_elements_reversed}")
# def max(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i]>arr[i+1]:
#                 arr[j], arr[j+1]=arr[j+1], arr[j]
#                 return arr
# if i need to find kth max of an array 1. sort the array => print kth elements from the ending 2.
# sentence = input("Enter a sentence: ")
# result = len(sentence.split())
# result2 = len(sentence.replace(" ", ""))
# print(f"no.of words in above sentence are: {result}")
# print(f"no.of alphabets in above sentence are: {result2}")


'''
### 1. Sum of Array/List
arr_sum = np.sum(arr)                             # [numpy]

### 2. Max-Min of Array
arr_max = np.max(arr); arr_min = np.min(arr)      # [numpy]

### 3. Search Element (Find Index)
index = np.where(arr == x)[0]                     # returns array of indices [numpy]

### 4. Reverse List/Array
reversed_arr = arr[::-1]                          # [numpy/pandas]

### 5. Left Rotate by 1
rot_left = np.roll(arr, -1)                       # left rotate [numpy]

### 6. Right Rotate by k
rot_right = np.roll(arr, k)                       # right rotate [numpy]

### 7. Remove Duplicates Unordered
unique_vals = np.unique(arr)                      # [numpy]

### 8. Remove Duplicates Keep Order
unique_inorder = pd.Series(arr).drop_duplicates().values   # [pandas]

### 9. Split +ves and -ves
positives = arr[arr > 0]; negatives = arr[arr < 0]         # [numpy logic]

### 10. Split Even/Odd by Index (positions)
even_index = arr[::2]; odd_index = arr[1::2]              # indices [numpy]
# OR for split on index: a = arr[::2] (even idx); b = arr[1::2] (odd idx)

### 11. Separate Even/Odd Elements
evens = arr[arr % 2 == 0]; odds = arr[arr % 2 != 0]        # [numpy]

### 12. Second Largest (Distinct)
uniq = np.unique(arr); second_largest = uniq[-2] if len(uniq) > 1 else None

### 13. Sorting Array
sorted_arr = np.sort(arr)                         # ascending [numpy]
# descending: sorted_desc = np.sort(arr)[::-1]

### 14. Merge Two Lists Alternately
merged = np.empty((len(a) + len(b),), dtype=a.dtype)
merged[0::2] = a; merged[1::2] = b                # lengths must match [numpy]
# For uneven length: np.concatenate([a, b])

### 15. Common Elements in Two Lists
common = np.intersect1d(a, b)                     # [numpy]
# For sets: set(a) & set(b)

### 16. Move Zeroes to the End
nonzeros = arr[arr != 0]; zeros = arr[arr == 0]; moved = np.concatenate([nonzeros, zeros])  # [numpy]

### 17. Count Occurrence of Element
values, counts = np.unique(arr, return_counts=True)        # [numpy]
# single element count: cnt = (arr == x).sum()

### 18. Position(s) Where Character Occurs in String
positions = [i for i, ch in enumerate(s) if ch == x]

### 19. String: Character Frequency
char_freq = pd.Series(list(s)).value_counts().to_dict()   # [pandas]

### 20. String: Vowel Count
vowel_count = sum(1 for ch in s if ch.lower() in "aeiou")

### 21. String: Find Vowels
vowels = [ch for ch in s if ch.lower() in "aeiou"]

### 22. String: Palindrome
is_palindrome = s == s[::-1]

### 23. String: Remove Duplicates (keep order)
nodupes = ''.join(pd.Series(list(s)).drop_duplicates())

### 24. String: Print Without Duplication
nodup_print = ''.join(sorted(set(s), key=s.index))        # order preserved by key[]

### 25. String: Anagram Test (ignore case/space)
a1 = ''.join(ch.lower() for ch in a if ch.isalnum())
b1 = ''.join(ch.lower() for ch in b if ch.isalnum())
is_anagram = sorted(a1) == sorted(b1)

### 26. Square of Number
sq = np.square(x)                                         # [numpy]

### 27. Reverse a Number
rev_num = int(str(abs(num))[::-1]) * (-1 if num < 0 else 1)

### 28. Prime Numbers (MATLAB/NumPy style)
nums = np.arange(2, N+1)
isprime = np.vectorize(lambda n: all(n % d != 0 for d in range(2, int(n**0.5)+1)))(nums)

### 29. Factorial
fact = np.math.factorial(n)                               # [numpy]

### 30. Matrix: Create & Print
mat = np.array(data)                                      # create from nested list [numpy]
for row in mat: print(*row)                               # print [py style]

### 31. Matrix: Transpose
mat_T = mat.T

### 32. Matrix: Diagonal Sum
diag_sum = np.trace(mat)

### 33. Matrix: Identity Check
is_identity = np.all(mat == np.eye(mat.shape[0]))

### 34. Matrix: Add/Subtract/Multiply
add = np.add(a, b); sub = np.subtract(a, b); mult = np.dot(a, b)   # [numpy]

### 35. Student Marks/Comparison (e.g. mean, top scorer)
student_marks = pd.DataFrame(data, columns=["name","marks"])
top_scorer = student_marks.loc[student_marks["marks"].idxmax()]["name"]

### 36. Dictionary: Access & Count Occurrence
d = pd.Series(lst).value_counts().to_dict()               # freq from list [pandas]

### 37. Dictionary: Swap Key-Value
swapped = dict(zip(d.values(), d.keys()))

### 38. Dictionary: Filter
filtered = {k: v for k, v in d.items() if v > min_value}

### 39. Dictionary: Merge Two Dictionaries
merged_dict = {**d1, **d2}                               # python3.5+/matlab style: structcat
'''