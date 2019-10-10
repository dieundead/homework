print (" *** СОРТИРОВКА ПУЗЫРЬКОМ ***")
arr_bubble = [406, 67, 926, 852, 682, 802, 265, 14, 676, 912, 645, 404, 537, 952, 132]
print ("Неотсортированный массив:", arr_bubble)
length_bubble = len(arr_bubble)
for i in range (0, length_bubble-1):
    for j in range (0, length_bubble-i-1):
        if arr_bubble[j] > arr_bubble[j+1]:
            arr_bubble[j], arr_bubble[j+1] = arr_bubble[j+1], arr_bubble[j]
    print (i+1, "- й проход цикла: ")
    print (arr_bubble)
print ("Отсортированный массив: ", arr_bubble)

print (" ")
print (" *** СОРТИРОВКА ВСТАВКАМИ ***")
arr_insertion = [978, 238, 59, 133, 258, 556, 612, 744, 620, 878, 341, 970, 59, 814, 547]
print ("Неотсортированный массив:", arr_insertion)
length_insertion = len(arr_insertion)
for i in range(0, length_insertion):
    temp = arr_insertion[i]
    j = i-1
    while j >= 0 and temp < arr_insertion[j]:
        arr_insertion[j+1], arr_insertion[j] = arr_insertion[j], arr_insertion[j+1]
        j -= 1
    print(i + 1, "- й проход цикла: ")
    print(arr_insertion)
print("Отсортированный массив: ", arr_insertion)

print (" ")
print (" *** СОРТИРОВКА ВЫБОРОМ ***")
arr_selection = [400, 169, 399, 590, 405, 168, 323, 671, 234, 941, 398, 42, 412, 710, 483]
print ("Неотсортированный массив:", arr_selection)
length_selection = len(arr_selection)
i = 0
while i < length_selection-1:
    m = i
    j = i+1
    while j<length_selection:
        if arr_selection[j] < arr_selection[m]:
            m=j
        j += 1
    arr_selection[i], arr_selection[m] = arr_selection[m], arr_selection[i]
    i += 1
print("Отсортированный массив: ", arr_selection)









