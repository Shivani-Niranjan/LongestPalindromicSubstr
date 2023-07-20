'''
Longest Palindromic Substring
Given a string A of size N, find and return the longest palindromic substring in A.

Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A

Input 1:
A = "aaaabaaa"

Input 2:
A = "abba

Output 1:
"aaabaaa"

Output 2:
"abba"
'''
 
def longestPalindrome(str):

    n = len(str)
    maxLength = 1
    start = 0
 
    # Nested loop to mark start and end index
    for i in range(n):
        for j in range(i, n):
            flag = 1
 
            # Check palindrome
            for k in range(0, ((j - i) // 2) + 1):
                if (str[i + k] != str[j - k]):
                    flag = 0
 
            # Palindrome
            if (flag != 0 and (j - i + 1) > maxLength):
                start = i
                maxLength = j - i + 1
 
    # to print the palindrome
    for i in range(start, start + maxLength - 1 + 1):
        print(str[i], end="")

 
string = input()
longestPalindrome(string)
