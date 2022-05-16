# Створити словник характеристик довільного автомобіля
# (марка, модель, рік, двигун і тд.) +
print("Practice 2.1 \n")

myCar = {
    "Brand": "Suxuki",
    "Model": "Vitara",
    "Model year": "2021",
    "Engine": {
        "Engine type": "Inline",
        "Number of cylinders": "4",
        "Fuel type": "Petrol",
        "Fuel System": "Direct Injection",
        "Engine Position": "Front",
    },
    "Transmission": {
        "Transmission Gearbox type": "manual",
        "Number of speeds": "6 speed",
    }
}
print(myCar)

# Видалити зі словника і вивести на еран рік автомобіля. +
print("Practice 2.2 \n")

a = myCar.pop("Model year")
print(a)
print(myCar)

# Створити дві довільні множини чисел, знайти спільні елементи в них +
print("Practice 2.3 \n")

s1 = {0, 1, 2, 3, 4, 5, 4, 7, 8, 9}
s2 = {17, 18, 19, 1, 2, 3, 14, 15, 16, 0}
print(s1.intersection(s2))

# За допомогою клавіатури заповнити дві змінні password i repeat_password
# надрукувати True в консоль якщо вони рівні в іншому випадку False. +
print("Practice 2.4 \n")

print('встановлення паролю')
password = (input('Прошу ввести ваш новий пароль:'))
repeat_password = (input('Прошу повторити ваш новий пароль:'))
if password == repeat_password:
    print("Дякую, все гаразд. Перевіряйте далі.")
else:
    print("Паролі не співпадають. Спробуйте ще :)")
# На всяк випадок
print((password == repeat_password))

# Створити довільний список, перетворити його в tuple i вивести перші три елементи. +
print("Practice 2.5 \n")
mal_lst = ["one", 2, "three", 4, 5, 6, 7, 8, 9, 10, 11, 12]
mal_tap = tuple(mal_lst)
print(mal_tap[0: 3])

# Знайти mod (остача від цілечисленого ділення) 121 на 7 -
print("Practice 2.6\n")
num1 = 121
num2 = 7
print(num1 % num2)

# Знайти div (цілечислене ділення ) 121 на 7 +
print("Practice 2.7 \n")
print(num1 // num2)

# Обчислити 2 в степіні 10 ( 2^10 ) +
print("Practice 2.8 \n")
c = 2 ** 10
print(c)
