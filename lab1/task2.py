import function


begin_list = []
finish_list = []
print("Input size list")
size = function.check_correct_int_input()
for i in range(size):
    begin_list.append(function.check_correct_int_input())
finish_list = function.check_terms(begin_list)
print("Sum new list = ", sum(finish_list))
print("Size new list = ", len(finish_list))
print("Big list: ", begin_list if sum(begin_list) > sum(finish_list) else finish_list)