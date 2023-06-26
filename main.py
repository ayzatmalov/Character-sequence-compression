text_for_comp = input('Введите последовательность символов: ')

first = text_for_comp[0]
count = 0
result = ''

for char in text_for_comp:
    if char == first:
        count += 1
    else:
        result += first + str(count)
        first = char
        count = 1

result += first + str(count)
print(result)