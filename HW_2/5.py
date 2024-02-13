def password_level(s):
    if len(s) < 8:
        return ("Недопустимый пароль")
    if s.isdigit() or s.islower() or s.isupper():
        return ("Ненадежный пароль")
    if s.isalpha():
        return ("Слабый пароль")
    else:
        return ("Надежный пароль")


b = ""
while b != "Надежный пароль":
    password = str(input("Придумайте пароль: "))
    b = password_level(password)
    print(b)

password_1 = ""
while password != password_1:
    password_1 = str(input("Введите пароль повторно: "))
    if password != password_1:
        print("Пароли НЕ совпадают")

print("Пароли совпадают")
