from random import randint

WELCOME_MESS = 'Добро пожаловать в игру "Угадай число"'
count = 0

print(WELCOME_MESS)

def new_game(answer_user):
  if answer_user == 'Да' or answer_user == 'да':
    value = randint(1,100)
    game(value)
  else:
    print('До свидания!')

def game(value):
  attempt = 0
  print('Загадано число от 1 до 100, попробуйте угадать')
  while True:
    print('Ваше число:')
    number = input()
    attempt += 1
    if int(number) > value:
      print(f'Введенное Вами число больше загаданного.')
    elif int(number < value:
      print(F'Введенное Вами число меньше загаданного.')
    else:
      print(f'Вы угадали число c {attempt} попытки! Поздравляем!')
      break

print('Хотите сыграть в игру угадай число?')
answer_user = input()
new_game(answer_user)