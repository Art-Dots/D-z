#Сгенерировать случайный список из 10 вещественных чисел (в диапазоне от -100 до 100),который
#необходимо отсортировать по возрастанию дробной части.(Хотя бы одно число
#должно иметь дробную часть, не менее 1 знака поле запятой).


from random import uniform
 
num=[uniform(-100, 100) for i in range(10)]
print(num)
print(sorted(num, key=lambda x: abs(x - int(x))))
