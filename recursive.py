'''Exercise 1 – Print Numbers Down

Write a recursive function:
print_down(n)
The function prints all numbers from n down to 1.
Example:
print_down(5)
Output:
5 4 3 2 1
Requirements:
Use recursion
Base case when n == 0'''

print("Exercise 1 – Print Numbers Down: ")
def print_down(n):
    if n == 0:
        return
    else:
        print(n, end=' ')
        print_down(n-1)

print_down(5)
print()
print()

'''Exercise 2 – Sum of Odd Numbers
Write a recursive function:
sum_odd(n)
The function returns the sum of all odd numbers from 1 to n.
Example:
sum_odd(7)
Result:
1 + 3 + 5 + 7 = 16
Expected output:
16
Notes:
If n is even, skip it Only odd numbers should be added'''


print('Exercise 2 – Sum of Odd Numbers')

def sum_odd(n):
    if n < 1:
        return 0
    else:
        if n % 2 == 0: # If n is even, we decrease --> -1 to make it odd.
            return sum_odd(n-1)

    return n + sum_odd(n-2)
print(sum_odd(7))

print()
print()

'''Exercise 3 – Power Function
Write a recursive function:
power(base, exponent)
The function calculates:
base ^ exponent
Example:
power(2, 4)
Output:
16
Explanation:
2^4 = 2 * 2^3 2^3 = 2 * 2^2 2^2 = 2 * 2^1 2^1 = 2
Base case:
exponent == 0 → return 1'''

print('Exercise 3 – Power Function')
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
print(power(5, 3))

print()
print()

'''Exercise 4 – Maximum in a List
Write a recursive function:
max_in_list(lst)
The function returns the largest number inside the list.
Example:
max_in_list([3, 8, 2, 15, 6])
Output:
15
Hints:
Compare the first element with the maximum of the rest of the list
Concept idea:
max([3,8,2,15,6]) = max(3, max([8,2,15,6]))
Base case:
list with one element'''

print("Exercise 4 – Maximum in a List")
def max_in_list(lst):
    if len(lst) == 1:
        return lst[0]
    elif len(lst) < 1:
        return print('No elements in list')
    else:
        max_rest = max_in_list(lst[1:])
        if lst[0] > max_rest:
            return lst[0]
        else:
            return max_rest
            
print(max_in_list([]))
print('\n')

'''Exercise 5 – Count Even Numbers in a List
Write a recursive function:
count_even(lst)
The function returns how many even numbers exist in the list.
Example:
count_even([2,5,8,7,6,3,10])
Output:
4
Explanation:
Even numbers are:
2, 8, 6, 10
Hints:
Check the first element
Add 1 if it is even
Continue recursion with the rest of the list
Base case:
empty list → return 0'''
print('Exercise 5 – Count Even Numbers in a List')
def count_even(lst):
    if len(lst) == 1:
        if lst[0] % 2 == 0:
            return 1
        else:
            return 0
    else:
        even_num = count_even(lst[1:])
        if lst[0] % 2 == 0:
            even_num = count_even(lst[1:]) + 1
            return even_num
        else:
            return even_num


print(count_even([2,2,4,8,7]))
