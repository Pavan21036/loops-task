
# STEP 4: Print numbers from 1 to 100 using for loop
print("STEP 4: Numbers from 1 to 100")
for i in range(1, 101):
    print(i)

print("\n-----------------------------\n")

# STEP 5: Countdown timer using while loop
print("STEP 5: Countdown Timer")
count = 10
while count > 0:
    print(count)
    count -= 1
print("Countdown Finished!")

print("\n-----------------------------\n")

# STEP 6: break and continue example
print("STEP 6: break and continue")

print("Using break:")
for i in range(1, 11):
    if i == 5:
        break
    print(i)

print("\nUsing continue:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

print("\n-----------------------------\n")

# STEP 7: Iterate over string characters
print("STEP 7: String Iteration")
name = "Python"
for char in name:
    print(char)

print("\n-----------------------------\n")

# STEP 8: Multiplication table
print("STEP 8: Multiplication Table")
num = 5
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("\n-----------------------------\n")

# STEP 9: range() with steps
print("STEP 9: range with steps (Even numbers)")
for i in range(0, 21, 2):
    print(i)

print("\n-----------------------------\n")

# STEP 10: Loop with conditions (Even / Odd)
print("STEP 10: Even or Odd")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")

print("\n-----------------------------\n")

# STEP 11: Real-world example - Password attempts
print("STEP 11: Password Login System")
attempts = 3

while attempts > 0:
    password = input("Enter password: ")
    if password == "admin":
        print("Login Successful")
        break
    else:
        print("Wrong password")
        attempts -= 1

if attempts == 0:
    print("Account Locked")
