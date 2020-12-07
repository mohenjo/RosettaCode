for n in range(1, 101):
    expr = ""
    if not n % 3:
        expr += "Fizz"
    if not n %5:
        expr += "Buzz"
    if not expr:
        expr = str(n)
    print(expr)


