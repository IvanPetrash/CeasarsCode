alfavit =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ12345678901234567890'
nextbukva = int(input('Шаг шифровки: '))    
message = input("Сообщение для шифровки: ").upper()
rezultat = ''
for s in message:
    bukva = alfavit.find(s)    
    new_bukva = bukva + nextbukva
for s in message:
    bukva = alfavit.find(s)
    new_bukva = bukva + nextbukva
    if s in alfavit:
        rezultat += alfavit[new_bukva]  
    else:
        rezultat += i
print (rezultat)
