
def reversing_numeric(num):
    # num1 = str(num)
    # ls = []
    # for i in range(len(num1)):
    #     ls.append(num1[i])
    # ls.reverse()
    # num1 = ""
    # for i in range(len(ls)):
    #    num1 =  num1+str(ls[i])

    return str(num)[::-1]

def finding_nextPalindrome(num):
    pass

def next_palindrome(list, n):
    for i in range(n):
        num = (list[i])
        reversed_num = int(reversing_numeric(num))
        print(reversed_num)
        if reversed_num == list[i]:
            print(f"{num} is palindrome.")
        else:

            print(f"{num} not palindrome. The next palindrome of {num} is : ")


if __name__ == '__main__':
    n = int(input("Enter total number of test cases you want to enter : "))
    ls =[]
    for i in range(n):
        num = int(input("Enter a number here : "))
        ls.append(num)
    next_palindrome(ls, n)


