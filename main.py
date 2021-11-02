#a palindrome is a word, phrase, number or other sequence of characters which reads the same backwards
#as forward, For example madam or level
def check_p():

    count = 1
    while count<=10: #user to enter ten words and check which ones are palindromes
        n = str(input("Enter a word to check whether its a  palindrome:"))
        count +=1
        if n == n[::-1]:
            print("{} is a palindrome".format(n))
        else:
            print("{} is not a palindrome".format(n))

check_p()

