str1 = input()
str2 = input()
str3 = input()

len_arr = [len(str1), len(str2), len(str3)]
len_arr.sort()

print(len_arr[2] - len_arr[0])