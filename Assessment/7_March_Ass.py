# Prog.9
# Password Strength Validator
# A password is strong if:
# 1. Length >= 8
# 2. Contains at least one uppercase letter
# 3. Contains at least one digit
# 4. Contains at least one special character (@, #, $)

class Solution:
    def strong_passwords(self, passwords):
        strong = []

        for pwd in passwords:
            if len(pwd) < 8:
                continue

            has_upper = False
            has_digit = False
            has_special = False

            for ch in pwd:
                if ch.isupper():
                    has_upper = True
                elif ch.isdigit():
                    has_digit = True
                elif ch in "@#$":
                    has_special = True

            if has_upper and has_digit and has_special:
                strong.append(pwd)

        return strong


# -------- Main Program --------

# Taking input from user
passwords = input("Enter passwords separated by space: ").split()

# Creating object of Solution class
obj = Solution()

# Calling the function
result = obj.strong_passwords(passwords)

# Printing strong passwords
print("Strong Passwords:", result)