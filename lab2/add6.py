f = open('dataset_3380_5.txt', 'r')
klass = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

count_class = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


for s in f:
    person = " ".join(s.strip().split("\t")).split(" ")
    klass[int(person[0]) - 1] += float(person[2])
    count_class[int(person[0]) - 1] += 1

for i in range(len(klass)):
    print(i+1, str(klass[i]/count_class[i]) if count_class[i] != 0 else "-")