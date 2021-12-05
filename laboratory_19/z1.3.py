"""
Довідник старости. База даних студентів групи: прізвище ім’я по-батькові, дата останнього дня чергування, стать, адреса.
Організувати вибір за довільним запитом. Дані зберігаються в масиві записів, який створюється динамічно.

"""
a = [['Bazeluk_Lidia_Oleksandrivna', '07.09.2021', 'woman', "vulicya_Lisova"],
     ['Brovdi_Vitaliy_Mihalovich', '04.10.2021', 'man', "vulicya_Hreshatik"],
     ['Dovganich_Igor_Olegovich', '05.10.2021', 'man', "vulicya_Ivana-franka"],
     ['Yovbak_Nika_Igorivna', '08.09.2021', 'woman', "vulicya_Volodimirska"],
     ['Mudrenyuk_Sofia_Evgenivna', '03.09.2021', 'woman', "vulicya_Luk/'nivska"],
     ['Telinger_Ergard-Mark_Zholtovich', '07.10.2021', 'man', "vulicya_Kocubinskogo"],
     ['Chaikovskii_Markiian_Yuriyovich', '06.10.2021', 'man', 'vulicya_Markiian_Shashkevicha']]
with open('z3(txt).txt', 'w') as file:
    for i in range(len(a)):
        file.write(' '.join(a[i]) + '\n')
info = str(input('Введіть запит : '))

f = open('z3(txt).txt')
for line in f:
    line1 = line.split(sep=' ')
    if info in line1 or info + "\n" in line1:
        print(*line1[::])
f.close()
