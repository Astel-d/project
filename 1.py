f = open('vacancy.csv', 'r', encoding = 'utf-8')

title = f.readline().split(';')

all_vacancy = f.readlines()
all_vacancy_list = []

f.close()



def sort(A, pose):
    """
    Функция сортировки пузырьком. Сравниваем все элементы
    списка и перемещаем их между друг другом

    A - массив, который подлежит сортировке
    pose - индекс значения в данном массиве, по которому будет производиться сортировка
    
    """
    for i in range(len(A)-1):
        for j in range(len(A)-2, i-1, -1):
            if A[j+1][pose] <= A[j][pose]:
                A[j][pose], A[j+1][pose] = A[j+1][pose], A[j][pose]

    return A


for vacancy in all_vacancy:
    all_vacancy_list.append(vacancy.replace('\n', '').split(';'))

f = open('vacancy_new.csv', 'w', encoding = 'utf-8')
f.write('Company;Role;Salary\n')

companis = {}    
for vacancy in all_vacancy_list:
    if vacancy[4] not in companis:
        companis[vacancy[4]] = [[vacancy[3], vacancy[0]]]
    else:
        companis[vacancy[4]].append([vacancy[3], vacancy[0]])


all_vacancy_list_s = []

for company in companis:
    sorted_company = sort(companis[company], 1)
    all_vacancy_list_s.append([company, sorted_company[-1][0], sorted_company[-1][1]])

for vacancy in all_vacancy_list_s:
    f.write(f'{vacancy[0]};{vacancy[1]};{vacancy[2]}\n')

f.close()

all_vacancy_list_s = sort(all_vacancy_list_s, 2)

print(f'{all_vacancy_list_s[-1][0]}-{all_vacancy_list_s[-1][1]}-{all_vacancy_list_s[-1][2]}')
print(f'{all_vacancy_list_s[-2][0]}-{all_vacancy_list_s[-2][1]}-{all_vacancy_list_s[-2][2]}')
print(f'{all_vacancy_list_s[-3][0]}-{all_vacancy_list_s[-3][1]}-{all_vacancy_list_s[-3][2]}')

