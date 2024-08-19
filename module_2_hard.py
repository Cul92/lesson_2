import random

first_list = random.sample(range(3, 21), 18)
print('Первое поле:', first_list)
n = random.choice(first_list)
first_list.remove(n)

print('Случайное число из первого поля:', n)
second_list = []
pairs = []
for i in range(1, 21):
    for j in range(i + 1, 21):
        if n != i and n != j:
            pair_sum = i + j
            if n % pair_sum == 0:
                pairs.append(f"{i}{j}")
output = "".join(pairs)
print(" пароль:", output)
if pairs:
    second_list.append(f"{n} - {''.join(pairs)}")
for result in second_list:
    print(" Пароль  для ", result)
