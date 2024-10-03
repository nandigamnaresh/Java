string ="Naresh"
n=string.strip()

vowelcount=0
constantcount=0

for i in n:
    if i in "aeiouAEIOU":
        vowelcount=vowelcount+1
    else:
        constantcount=vowelcount+1

print("The number of vowels in the string is: ",vowelcount)
print("The number of consonants in the string is: ",constantcount)