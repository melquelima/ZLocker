import string
import random


def randomPassword(uppercase=1,lowercase=4,numbers=1,signals=1):
    uper = string.ascii_uppercase
    lower = string.ascii_lowercase
    numb = string.digits
    sign = string.punctuation
    u = ''.join(random.choice(uper) for i in range(uppercase))
    l = ''.join(random.choice(lower) for i in range(lowercase))
    n = ''.join(random.choice(numb) for i in range(numbers))
    s = ''.join(random.choice(sign) for i in range(signals))
    return f"{u}{l}{n}{s}"



