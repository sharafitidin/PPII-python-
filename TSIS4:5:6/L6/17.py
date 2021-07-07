def bold_f(s):
    return "<b>{}</b>".format(s)
def italic_f(s):
    return "<i>{}</i>".format(s)
def underline_f(s):
    return "<u>{}</u>".format(s)
i = int(input("""
    1)Bold
    2)Italic
    3)Underline
    Input: 
"""))
s = input("Write your string: ")
if i == 1:
    print(bold_f(s))
elif i == 2:
    print(italic_f(s))
elif i == 3:
    print(underline_f(s))
else:
    print("Invalid input")