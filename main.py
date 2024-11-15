list_strok = []
list_join = []
list_split = []

kolvo_strok = int(input("Введите количество строк в вашем списке: "))
if kolvo_strok <= 0 :
    print("Вы ввели не верное количество строк,попробуйте еще раз")
else:
    for i in range(0,kolvo_strok):
        list_strok.append(str(input(f"Введите вашу строку,стоящую под индексом {i} ")))

list_join = "".join(list_strok)
list_split = list_join.split()
unikalni = len(set(list_split))

print(f"В тексте,из строк,которые вы ввели,различных слов содержится: {unikalni}")



