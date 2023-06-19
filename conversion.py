def bin_to_dec(n):
    dec = 0
    p = 0
    while n!=0:
        rem = n%10
        dec = dec + rem * 2**p
        n = n//10
        p = p + 1
    return dec


def oct_to_hex(n):
    n = int(n,8)
    print("decimal equivalent of octal :",n)
    hexa = hex(n)
    return hexa


n = int(input("Enter binary number: "))
print("Decimal: ", bin_to_dec(n))
n = input("Enter octal number(0-7)")
n = "0o" + n
print("Hexadecimal number is: ", oct_to_hex(n))

