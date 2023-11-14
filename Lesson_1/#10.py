# 10 Школярі та яблука
# n школярів ділять k яблук порівну, недільний залишок залишається в кошику.
# Скільки яблук дістанеться кожному школярові та скільки залишиться в кошику?
# Програма отримує на вхід числа n і k - цілі, додатні, не перевищують 10000.

k = int(input("Please enter the number of apples: "))
assert 1 < k < 10001, "The value entered is incorrect"
n = int(input("Please enter the number of kids: "))
assert 1 < n < 10001, "The value entered is incorrect"

print("The number of apples left: ",k % n)
