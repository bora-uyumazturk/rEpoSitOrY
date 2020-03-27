import random

def process(s):
    result = ""
    i = 0
    while(i < len(s)):
        c = s[i]
        if random.random() > 0.5:
            result += c.upper()
        else:
            result += c
        if random.random() > 0.05 or c.isspace():
            i+=1
    return result

if __name__ == "__main__":
    print("Input lowercase string to mAkE iT wEirD, press Enter to quit.")
    while True:
        s = input("->")
        if s == "":
            break
        s_new = process(s)
        print(s_new)
