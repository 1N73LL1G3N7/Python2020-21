def EuclidsDivisionAlgorithm(a, b):
    if not(isinstance(a, int) and isinstance(b, int)):
        raise ValueError("a and b should be Integers!")
    r = a % b
    if r == 0:
        hcf = b
    else:
        a = b
        b = r
        hcf = EuclidsDivisionAlgorithm(a, b)
    return hcf


print("Welcome to HCF/GCD Calculator programme...")
a = int(input("Enter number a : "))
b = int(input("Enter number b : "))
hcf = EuclidsDivisionAlgorithm(a, b)
print(f"HCF{a, b} = {hcf}")
