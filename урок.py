words = input()
user_count_letter = int(input())
words = "carrot, potato, onion, tomato, carrot, cucumber"

#1
words = words.replace(" ", "")
list = words.split(",")
print(list)

#2
lowregistr = words.lower()
print(lowregistr)

#3
letters = set()
for i in range(len(list)):
    for j in range(len(list[i])):
        letters.add(list[i][j])

print(len(letters))

#4

maxcount = 0
for i in range(len(list)):
    if list[i].count("o") > maxcount:
        maxcount = list[i].count("o")
max_o = []
for i in range(len(list)):
    if list[i].count("o") == maxcount:
        max_o.append(list[i])

print(max_o)
    
#5 и 6

vegetables_dict = {

}


for i in range(len(list)):
    vowels = list[i].count("i") + list[i].count("o") + list[i].count("a") + list[i].count("e") + list[i].count("u") + list[i].count("y")
    vegetables_dict.update({list[i]: vowels})

print(vegetables_dict)
print(max(vegetables_dict, key = vegetables_dict.get))   


# 7

words_nocommo = words.replace(",", "")
mid_value = len(words_nocommo) / len(list)
list_max_value = []
for i in range(len(list)):
    if len(list[i]) >= mid_value:
        list_max_value.append(i)
print(list_max_value)


# 8
tuple_list = tuple(list[::-1])
print(tuple_list)

# 9
list_beggining_ck = []
for i in list:
  if i[0] == 'c' or i[0] =='k':
    list_beggining_ck.append(i)
if len(list_beggining_ck)>0:
  print(list_beggining_ck)
else:
  print('Нет таких овощей')

# 10
word_more_letter = []
for i in list:
  if len(i)>user_count_letter:
    word_more_letter.append(i)
print(word_more_letter)




