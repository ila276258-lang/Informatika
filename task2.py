def find_common_participants (m1, m2, s=","): #Вводим функцию
    common_participants = [] #Создаём нулевой список
    for i in m1.split(s): #Создаём цикл проходящийся по 1 списку
        for k in m2.split(s): #Создаём цикл проходящийся по 2 списку
         if i == k: #Если в 1 списке фамилия = фамилии во второй
            common_participants.append(i) #то записываем в список фамилию
    common_participants.sort() #Сортируем список
    return common_participants #Закрываем функцию


participants_first_group = "Иванов|Петров|Сидоров" #Вводим 1 список
participants_second_group = "Петров|Сидоров|Смирнов" #Вводим 2 список
print(find_common_participants(participants_first_group, participants_second_group, "|")) #Пишем список с палочкой
