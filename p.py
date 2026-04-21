"""
PYTHON PROGRAMMING EXAM – LAST DAY REVISION (BASICS + LOW/MEDIUM DSA)

How to use this file tonight:
- Memorize the "templates" (the few-liner logic).
- In exam: copy template, change variable names, adjust input/output format.
- Focus on: loops, conditionals, strings, lists, dict, set/tuple, searching, sorting, matrices.

Most-expected questions (from your handwritten list + the provided PDF pages):
- List/Array: sum, max/min, search, reverse, remove duplicates, 2nd largest, sorting, merge alternately
- String: count chars/vowels/consonants, palindrome, anagram-ish frequency, word count
- Dict: swap key/value, filter dict, count occurrences
- Matrix: read/print, transpose, diagonal sum, identity check, add/subtract/multiply (2D lists)
"""

from __future__ import annotations

from collections import Counter
from typing import List, Sequence, Tuple, Dict, Any, Optional


# =============================================================================
# 0) QUICK INPUT TEMPLATES (write once, reuse)
# =============================================================================

def read_ints() -> List[int]:
    return list(map(int, input().split()))


def read_list_n(n: int) -> List[int]:
    return [int(input()) for _ in range(n)]


def read_list_str_n(n: int) -> List[str]:
    # Matches PDF style: "read N elements in a list and display them"
    return [input().strip() for _ in range(n)]


def read_matrix(r: int, c: int) -> List[List[int]]:
    # If exam gives one number per line: use input() in nested loop.
    # If exam gives row-wise: replace body with read_ints().
    mat = []
    for _ in range(r):
        row = [int(input()) for _ in range(c)]
        mat.append(row)
    return mat


# =============================================================================
# 1) NUMBERS (very common)
# =============================================================================

def even_odd_zero(n: int) -> str:
    if n == 0:
        return "Zero"
    return "Even" if n % 2 == 0 else "Odd"


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def count_digits(n: int) -> int:
    return len(str(abs(n)))


def reverse_number(n: int) -> int:
    s = str(abs(n))
    rev = int(s[::-1]) if s else 0
    return -rev if n < 0 else rev


def sum_digits(n: int) -> int:
    return sum(int(d) for d in str(abs(n)))


def is_armstrong(n: int) -> bool:
    # Works for any number of digits (not only 3-digit).
    digits = [int(d) for d in str(abs(n))]
    p = len(digits)
    return n == sum(d ** p for d in digits)


def factorial_iter(n: int) -> Optional[int]:
    if n < 0:
        return None
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans


def factorial_rec(n: int) -> Optional[int]:
    if n < 0:
        return None
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)


def is_palindrome_number(n: int) -> bool:
    s = str(n)
    return s == s[::-1]


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)


def fibonacci_first_n(n: int) -> List[int]:
    # 0,1,1,2,3...
    if n <= 0:
        return []
    if n == 1:
        return [0]
    a, b = 0, 1
    out = [0, 1]
    for _ in range(n - 2):
        a, b = b, a + b
        out.append(b)
    return out


# =============================================================================
# 2) STRINGS (counting, filtering, reversing)
# =============================================================================

VOWELS = set("aeiouAEIOU")


def count_vowels_consonants(s: str) -> Tuple[int, int]:
    v = 0
    c = 0
    for ch in s:
        if ch.isalpha():
            if ch in VOWELS:
                v += 1
            else:
                c += 1
    return v, c


def count_chars(s: str, ignore_space: bool = False) -> int:
    if ignore_space:
        s = "".join(ch for ch in s if not ch.isspace())
    return len(s)


def reverse_string(s: str) -> str:
    return s[::-1]


def is_palindrome_string(s: str, ignore_case_space: bool = True) -> bool:
    if ignore_case_space:
        s = "".join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]


def char_frequency(s: str, only_alpha_numeric: bool = False) -> Dict[str, int]:
    if only_alpha_numeric:
        s = "".join(ch for ch in s if ch.isalnum())
    return dict(Counter(s))


def most_frequent_char(s: str) -> Tuple[str, int]:
    freq = Counter(s)
    ch, cnt = freq.most_common(1)[0] if freq else ("", 0)
    return ch, cnt


def word_count(s: str) -> int:
    # splits by any whitespace
    return len(s.split())


def remove_duplicates_string_keep_order(s: str) -> str:
    seen = set()
    out = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            out.append(ch)
    return "".join(out)


def are_anagrams(a: str, b: str) -> bool:
    # Common exam simplification: ignore case and spaces.
    fa = Counter(ch.lower() for ch in a if ch.isalnum())
    fb = Counter(ch.lower() for ch in b if ch.isalnum())
    return fa == fb


# =============================================================================
# 3) LIST / ARRAY (core DSA)
# =============================================================================

def sum_array(arr: Sequence[int]) -> int:
    return sum(arr)


def max_min_array(arr: Sequence[int]) -> Tuple[Optional[int], Optional[int]]:
    if not arr:
        return None, None
    mx = mn = arr[0]
    for x in arr[1:]:
        if x > mx:
            mx = x
        if x < mn:
            mn = x
    return mx, mn


def linear_search(arr: Sequence[int], target: int) -> int:
    # returns index or -1
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1


def binary_search_sorted(arr: Sequence[int], target: int) -> int:
    # arr must be sorted
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def reverse_array(arr: Sequence[int]) -> List[int]:
    return list(arr[::-1])


def remove_duplicates_list_unordered(lst: Sequence[Any]) -> List[Any]:
    # Fast, but order can change
    return list(set(lst))


def remove_duplicates_list_keep_order(lst: Sequence[Any]) -> List[Any]:
    # Keeps original order (expected in many exams)
    return list(dict.fromkeys(lst))


def second_largest_distinct(arr: Sequence[int]) -> Optional[int]:
    # Returns 2nd DISTINCT largest, else None.
    first = second = None
    for x in arr:
        if first is None or x > first:
            if x != first:
                second = first
            first = x
        elif x != first and (second is None or x > second):
            second = x
    return second


def merge_alternatively(a: Sequence[Any], b: Sequence[Any]) -> List[Any]:
    # [a0,b0,a1,b1,...] then leftover
    out = []
    n = max(len(a), len(b))
    for i in range(n):
        if i < len(a):
            out.append(a[i])
        if i < len(b):
            out.append(b[i])
    return out


def rotate_right_by_k(arr: Sequence[Any], k: int) -> List[Any]:
    # Very common: rotate array k times
    if not arr:
        return []
    k %= len(arr)
    return list(arr[-k:] + arr[:-k]) if k else list(arr)


def bubble_sort(arr: Sequence[int]) -> List[int]:
    a = list(arr)
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def selection_sort(arr: Sequence[int]) -> List[int]:
    a = list(arr)
    n = len(a)
    for i in range(n):
        mi = i
        for j in range(i + 1, n):
            if a[j] < a[mi]:
                mi = j
        a[i], a[mi] = a[mi], a[i]
    return a


def insertion_sort(arr: Sequence[int]) -> List[int]:
    a = list(arr)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def count_occurrences_list(lst: Sequence[Any]) -> Dict[Any, int]:
    # "access element and count occurrence" type question
    return dict(Counter(lst))


# =============================================================================
# 4) TUPLE / SET (often asked as "convert / combine")
# =============================================================================

def combine_tuples(t1: Tuple[Any, ...], t2: Tuple[Any, ...]) -> Tuple[Any, ...]:
    return t1 + t2


def list_to_tuple(lst: Sequence[Any]) -> Tuple[Any, ...]:
    return tuple(lst)


# =============================================================================
# 5) DICTIONARY (swap, filter, frequency)
# =============================================================================

def swap_key_value(d: Dict[Any, Any]) -> Dict[Any, Any]:
    # Note: if values repeat, later keys overwrite earlier keys.
    return {v: k for k, v in d.items()}


def filter_dict_by_value(d: Dict[Any, int], min_value: int) -> Dict[Any, int]:
    # Example: keep items with value >= min_value
    return {k: v for k, v in d.items() if v >= min_value}


def dict_frequency_from_list(lst: Sequence[Any]) -> Dict[Any, int]:
    freq: Dict[Any, int] = {}
    for x in lst:
        freq[x] = freq.get(x, 0) + 1
    return freq


# =============================================================================
# 6) MATRIX / 2D LISTS (from your PDF)
# =============================================================================

def print_matrix(mat: Sequence[Sequence[Any]]) -> None:
    for row in mat:
        print(*row)


def transpose(mat: Sequence[Sequence[int]]) -> List[List[int]]:
    if not mat:
        return []
    r, c = len(mat), len(mat[0])
    return [[mat[i][j] for i in range(r)] for j in range(c)]


def diagonal_sum(mat: Sequence[Sequence[int]]) -> int:
    # for square matrix
    return sum(mat[i][i] for i in range(min(len(mat), len(mat[0]) if mat else 0)))


def is_identity_matrix(mat: Sequence[Sequence[int]]) -> bool:
    # identity: diagonal 1, others 0 (square)
    if not mat:
        return False
    n = len(mat)
    if any(len(row) != n for row in mat):
        return False
    for i in range(n):
        for j in range(n):
            if i == j:
                if mat[i][j] != 1:
                    return False
            else:
                if mat[i][j] != 0:
                    return False
    return True


def add_matrices(a: Sequence[Sequence[int]], b: Sequence[Sequence[int]]) -> List[List[int]]:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def subtract_matrices(a: Sequence[Sequence[int]], b: Sequence[Sequence[int]]) -> List[List[int]]:
    # Matches PDF: "find their difference"
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def multiply_matrices(a: Sequence[Sequence[int]], b: Sequence[Sequence[int]]) -> List[List[int]]:
    # Standard matrix multiplication: (r x k) * (k x c) = (r x c)
    if not a or not b:
        return []
    r, k = len(a), len(a[0])
    if any(len(row) != k for row in a):
        raise ValueError("Matrix A is not rectangular")
    if not b or any(len(row) != len(b[0]) for row in b):
        raise ValueError("Matrix B is not rectangular")
    if len(b) != k:
        raise ValueError("Incompatible shapes for multiplication")
    c = len(b[0])
    out = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            s = 0
            for t in range(k):
                s += a[i][t] * b[t][j]
            out[i][j] = s
    return out


# =============================================================================
# 7) PATTERNS (short, but exam loves it)
# =============================================================================

def star_triangle(n: int) -> None:
    for i in range(1, n + 1):
        print("*" * i)


def number_triangle(n: int) -> None:
    for i in range(1, n + 1):
        print(*range(1, i + 1))


# =============================================================================
# 8) SMALL PYTHON BASICS (must-know)
# =============================================================================

def demo_args_kwargs(a: int, b: int = 10, *args: int, **kwargs: Any) -> int:
    # exam friendly: default arg + *args + **kwargs
    return a + b + sum(args) + int(kwargs.get("extra", 0))


cube = lambda x: x ** 3  # noqa: E731 (kept for revision)


# =============================================================================
# NOTE: This file is a revision sheet.
# In exam you’ll mostly write an input->process->print script using these templates.
# =============================================================================