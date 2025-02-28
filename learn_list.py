
# my_list = [3, 1, 4, 1, 5, 9, 2, 6]
# print(f"my_list {my_list}")
# new_list = sorted(my_list)
# print(f"new_list {new_list}")
# new_list[2] = 10
# print(f"new_list after modifying {new_list}")
# print(f"my_list {my_list}")

# my_list = [1, 2, 3, 4, 5]
# new_list = list(reversed(my_list))
# print(f"my_list {my_list}" )
# print(f"new_list {new_list}" )

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(f"Angka genap: {even_numbers}")


# data_draw = "uhuy"
# data_list = [data_draw] *4


# print(f"data_list {data_list}")

# data_draw = "uhuy"
# data_list = [data_draw] * 4

# print(data_list)  # Output: ['uhuy', 'uhuy', 'uhuy', 'uhuy']

# # Contoh jika Anda mencoba mengubah salah satu elemen:
# data_list[0] = "berubah"
# print(data_list)  # Output: ['berubah', 'uhuy', 'uhuy', 'uhuy']

# data_draw = "uhuy"
# data_list = [[data_draw] for _ in range(4)]
# print(data_list)  # Output: [['uhuy'], ['uhuy'], ['uhuy'], ['uhuy']]

# tidak bisa
# for _ in len(data_list):
#     print(f"_ {_}")

data_list = ["a", "b", "c", "d"]

for i in range(len(data_list)):
    print(i)
    
for a in data_list:
    print(a)