import random

def process(s):
    result = ""
    i = 0
    prev = False 
    while(i < len(s)):
        c = s[i]
        threshold = 0.25
        if prev:
            threshold = 0.75
        if i == 0:
            threshold = 2.0
        if random.random() > threshold:
            result += c.upper()
            prev = True 
        else:
            result += c
            prev = False
        if random.random() > 0.025 or c.isspace():
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
