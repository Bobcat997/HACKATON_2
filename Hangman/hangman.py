import random
from hang_visual import rysunek

def comp_choice():
  with open('words.txt', encoding='utf-8') as fopen:
    content = fopen.read()
  content = content.split('\n')
  words = random.choice(content)
  return words


def mask_word(word, letters):
  new_word = ''
  for letter in word:
    if letter.lower() in letters:
      new_word += letter
    else:
      if letter == ' ':
        new_word += ' '
      else:
        new_word += '-'
  return new_word

def menu():
  print(f'do you want to try again ??')
  user_choice = input(f'Y/N ->')
  if user_choice.lower() == 'n':
    print(f'Bye Bye.')
    return
  elif user_choice.lower() == 'y':
    main()
  else:
    print(clear)
    menu()


def main():
  attempt = 9
  rysunek(attempt)
  word = comp_choice()
  l = []
  guessed = False
  while attempt >= 0:
    if l:
      print(f'\nUzyte litery: {set(l)}\n{mask_word(word, l)}\n')
    else:
      print(f'\n{mask_word(word, l)}\n')
    user_input = input('Enter a Letter: ').lower()
    if len(user_input) > 1:
      if user_input.lower() == word.lower():
        print('you guessed!')
        guessed = True
        break
    else:
      if user_input not in word:
        rysunek(attempt)
      l.append(user_input)
    attempt -= 1
  if not guessed:
    print(f'\nUzyte litery: {set(l)}\n{mask_word(word, l)}\n')


main()
menu()