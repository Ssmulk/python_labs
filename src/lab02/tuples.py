def format_record(rec: tuple[str, str, float]) -> str:
    if type(rec) != tuple:  # Проверка на кортеж
        raise TypeError('входные данные должны быть кортежем')
    gpa = round(rec[2], 2)
    if not (0.0 <= gpa <= 5.0):
        raise ValueError('GPA должен быть в диапазоне от 0.0 до 5.0')
    fio = rec[0].split()
    if len(fio) == 0:
        raise ValueError('напиши имя')
    name = fio[0].lower()
    gr = rec[1]
    if len(gr) == 0:
        raise ValueError('напиши группу')
    
    if len(fio) == 3:
        fio1 = f'{name[0].upper() + name[1:]} {fio[1][0].upper()}.{fio[2][0].upper()}.'
    else:
        fio1 = f'{name[0].upper() + name[1:]} {fio[1][0].upper()}.'
    fio1 = f'{fio1.strip()}, гр. {gr.strip()}, GPA {gpa:.2f}'
    return fio1

print(format_record(('Иванов Иван Иванович', 'BIVT-25', 4.6)))
print(format_record(('Петров Пётр', 'IKBO-12', 5.0)))
print(format_record(('Петров Пётр Петрович', 'IKBO-12', 5.0)))
print(format_record(('сидорова анна сергеевна', 'ABB-01', 3.999)))