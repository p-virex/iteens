  
# https://webdevblog.ru/algoritmy-sortirovki-v-python/
from random import randint

nums = list()

for _ in range(20):
    nums.append(randint(0, 500))

print(nums)

for i in range(len(nums)):
    # Мы предполагаем, что первый элемент несортированного сегмента является наименьшим
    min_value_ind = i
    # Этот цикл перебирает несортированные элементы
    for j in range(i + 1, len(nums)):
        if nums[j] < nums[min_value_ind]:
            min_value_ind = j
    # Поменять местами значения самого низкого несортированного элемента с первым несортированным
    a = nums[min_value_ind]
    b = nums[i]
    nums[i] = a
    nums[min_value_ind] = b
    # или вот так в одну строку
    # nums[i], nums[min_value_ind] = nums[min_value_ind], nums[i]

print(nums)
