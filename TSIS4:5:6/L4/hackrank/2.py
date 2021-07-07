import re
s = input()
pattern = r"[.,]"
print("\n".join(re.split(pattern, s)))