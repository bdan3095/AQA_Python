k = int(input("Please enter the number of apples: "))
assert 1 < k < 10001, "The value entered is incorrect"
n = int(input("Please enter the number of kids: "))
assert 1 < n < 10001, "The value entered is incorrect"

print("The number of apples left: ",k % n)
