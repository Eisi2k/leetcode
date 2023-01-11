x = 122

#Version 1: Int -> String and slicing

def isPalindrome(x):

    #convert into string
    if type(x) != str:
        x = str(x)

    #comparison with string-slicing
    result = x == x[::-1]
    return result


ergebnis = isPalindrome(x)
print(ergebnis)

#Follow up Question: Using int

num = 12222

def isPalindrome_v2(num):

    #dummy variable
    reversed_num = 0

    #While-loop for reversring integer
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return (num == reversed_num)

ergebnis = isPalindrome(num)
print("Solution: ", ergebnis)

