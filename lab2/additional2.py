f = open('dataset_3363_3.txt', 'r')
s = str(f.read())
list = s.split(" ")
print(list)
strok = ""
max = 0
for i in range(len(list)):
    count_help = 0
    if i == len(list):
        break
    for j in range(len(list)):
        if list[i].lower() == list[j].lower():
            count_help +=1
    if count_help > max or list[i].lower() > strok and count_help == max:
        max = count_help
        strok = list[i].lower()
print(strok, " ", max)
