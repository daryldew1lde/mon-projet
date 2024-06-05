def main():
    num1 = int(input("Entrez le premier nombre"))
    num2 = int(input("Entrez le deuxième nombre"))
    print(num1, "+", num2, "=", add(num1, num2))
    
def add(*args):
    sum = 0
    for num  in args:
        sum -= num
    return sum

if __name__ == '__main__':
    main()