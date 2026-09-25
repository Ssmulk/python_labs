fio=input('ФИО: ')
parts=fio.split()
initials=''.join(word[0] for word in parts).upper()+'.'

print(f'Инициалы: {initials}')
print(f'Длина (символов): {len(fio)}')