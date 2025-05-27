"""
Assigment 5: Reverse a List using Recursion
Submitted by Zainab Abdulhasan
Submitted: October 24, 2024
"""


def reverse_a_list(my_list):
    """ Reverse the order of my_list using recursion """

    # Display the current length of the list, just to see how the recursion works
    print(f"The length of my_list is now: {len(my_list)}")

    # Base case: If there's only one item left, we can't reverse it further, so return it
    if len(my_list) == 1:
        return my_list

    # Recursive case: Take the last item and add it to the result of reversing the rest
    return [my_list[-1]] + reverse_a_list(my_list[:-1])


def main():
    # Create a list of letters a to z using one line of code (list comprehension)
    alphabet = [chr(i) for i in range(97, 123)]  # ASCII numbers 97-122 represent 'a' to 'z'

    # Print the alphabet list (a to z)
    print(alphabet)

    # Call reverse_a_list and print the reversed alphabet (z to a)
    print(reverse_a_list(alphabet))

    # Print the original alphabet again to show it wasn't changed
    print(alphabet)


if __name__ == "__main__":
    main()



"""
"C:\\Users\\zandu\\python projects\\Assignment-5\\.venv\\Scripts\\python.exe" "C:\\Users\\zandu\\python projects\\Assignment-5\\Assignment-5.py"
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
The length of my_list is now: 26
The length of my_list is now: 25
The length of my_list is now: 24
The length of my_list is now: 23
The length of my_list is now: 22
The length of my_list is now: 21
The length of my_list is now: 20
The length of my_list is now: 19
The length of my_list is now: 18
The length of my_list is now: 17
The length of my_list is now: 16
The length of my_list is now: 15
The length of my_list is now: 14
The length of my_list is now: 13
The length of my_list is now: 12
The length of my_list is now: 11
The length of my_list is now: 10
The length of my_list is now: 9
The length of my_list is now: 8
The length of my_list is now: 7
The length of my_list is now: 6
The length of my_list is now: 5
The length of my_list is now: 4
The length of my_list is now: 3
The length of my_list is now: 2
The length of my_list is now: 1
['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
"""