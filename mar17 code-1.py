s=input()
vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
l=[i for i in s if i not in vowels]
[print(i,end='') for i in l]