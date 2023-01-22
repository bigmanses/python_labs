
f = open('dataset_3363_4.txt', 'r')
math = 0
physic = 0
language = 0
count = 0
for s in f:
    list = s.strip().split(';')
    print((int(list[1]) + int(list[2]) + int(list[3])) / 3)
    math += int(list[1])
    physic += int(list[2])
    language += int(list[3])
    count += 1
print(math/count, " ", physic/count, " ", language/count)

