# Напишите функцию, которая кодирует сообщение шифром encrypt_caesar(msg, shift) Цезаря и возвращает его. 
# Шифр Цезаря заменяет каждую букву в тексте на букву, которая отстоит в алфавите на некоторое фиксированное число позиций.
# В функцию передается сообщение и сдвиг алфавита. 
# Если сдвиг не указан, то пусть ваша функция кодирует сдвиг алфавита на 3 позиции:

def encrypt_caesar(msg, shift):
  res = ''
  for sym in msg:
    if 1040 <= ord(sym) <= 1103:
      if ord(sym) > 1071 and ord(sym) + shift > 1103:
        res += chr(1072 + (ord(sym) + shift - 1103) - 1)
      elif ord(sym) <= 1071 and ord(sym) + shift > 1071:
        res += chr(1040 + (ord(sym) + shift - 1071) - 1)
      else:
        res += chr(ord(sym) + shift)
    else:
      res += sym
  print(res)


def decrypt_caesar(msg, shift):
  res = ''
  for sym in msg:
    if 1040 <= ord(sym) <= 1103:
      if ord(sym) >= 1072 and ord(sym) - shift < 1072:
        res += chr(1103 - (1072 - (ord(sym) - shift) - 1))
      elif ord(sym) >= 1040 and ord(sym) - shift < 1040:
        res += chr(1071 - (1040 - (ord(sym) - shift) - 1))
      else:
        res += chr(ord(sym) - shift)
    else:
      res += sym
  print(res)

encrypt_caesar('Да здравсвует Цезарь', 3)
decrypt_caesar('Йе мйхезцзшкч Ыкмехб', 3)