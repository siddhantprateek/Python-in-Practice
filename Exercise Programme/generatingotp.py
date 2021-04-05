# import django
# print("Django version used:", django.get_version())
import random
# a = 456

# print(len(str(a)))

# m = ["s", "q", "w", "e"]
# n = random.choice(range(10))
# print(n)


def otp_generating():
    otp = ""
    for i in range(4):
        otp += str(random.choice(range(10)))
    return otp


print(otp_generating())


# print(lambda otp: otp for i in range(4): otp += str(random.choice(range(10))))
