import re
f = open("text.txt", "r")
textFile = f.read()

bin = r"\nБИН.*(?P<BIN>\b[0-9]+)"
name = r"\nФилиал.*(?P<Name>\b[A-Z]+)"

textBin = re.search(bin, textFile).group("BIN")
textName = re.search(name, textFile).group("Name")

print(textBin)
print(textName)

itemPatternTxt = r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
itemPattern = re.compile(itemPatternTxt)

for i in re.finditer(itemPattern, textFile):
    print(i.group("name") + "\n" + " " + i.group("count")+ "\n" + i.group("price") + "\n"+ i.group("total1"))

timePattern = r"\nВремя: (?P<Time>\b[0-9].*\n{1}(?P<Address>.*))"
timeTxt = re.search(timePattern, textFile).group("Time")
adressTxt = re.search(timePattern, textFile).group("Address")
print(timeTxt)
f.close()