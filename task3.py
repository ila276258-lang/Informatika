list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
middle_index = len(list_players) // 2 # Разделили количество людей в списке по попалам, чтобы определить число до которого будет середина списка
first_team = list_players[:middle_index] # Определив середину списка, первую команду с помощью слайсирования
second_team = list_players[middle_index:] # Аналогично прошлому действию определяем вторую команду
print(first_team)
print(second_team)