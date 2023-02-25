# Домашнє завдання
# Task 1
# Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, що складаються з однієї літери R, за якою слідує
# одна або більше літер b, за якою одна r. Враховувати верхній та нижній регістр.
import re
from turtle import reset

result = re.findall('[Rr][bB]+[Rr]', 'dfmlkmlsdf Rbbbbr jklskdflkmsdsdfsdrbr')
print(result)
# OR
result = re.findall('rb+r', 'dfmlkmlsdf Rbbbbr jklskdflkmsdsdfsdrbr', re.I)
print(result)


# Task 2
# Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).

pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
text = '1234-1234-1234-1234'
print(re.findall(pattern, text))

# Task 3
# Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу.
# Вимоги:
# -Цифри (0-9).
# -лише латинські літери у великому (A-Z) та малому (a-z) регістрах.
# -у тілі мейла допустимі лише символи "_" і "-". Але вони не можуть бути першим символом мейлу.
# -Символ "-" не може повторюватися.

def validation_email(email):
    pattern = r'^([^-_]|\w+)-?\w+@\w+[\.a-zA-Z]+$'
    result = re.search(pattern, email, re.I)
    # print(result)
    return bool(result)

print(f'e-mail: {validation_email("ss-cdsd@google.Com.ua")}')

# Task 4
# Напишіть функцію, яка перевіряє правильність логіну. Правильний логін – рядок від 2 до 10 символів, що містить лише
# літери та цифри.

def check_login(login):
    pattern = r'^[a-zA-Z0-9]{2,10}$'
    result = re.search(pattern, login)
    # print(result)
    return bool(result)

print(check_login('sdF23se'))
