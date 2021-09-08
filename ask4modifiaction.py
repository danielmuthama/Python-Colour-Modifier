import os
import Option

#ask for more modfication
inp = "yn"
print("Do you wish to continue with the modification")
if os.system("choice /c:%s /n /m \"Yes or No (Y/N)\"" % inp) - 2:
    # if pressed Y
    print("Yes")
else:
    # if pressed N
    print("No")