# -*- coding: cp1251 -*-

#В текстовом файле построчно хранятся адреса
#Неповрежденный вид: 394090, г. Воронеж, ул. Ленина, д. 3, кв. 1
#Во входном файле могут быть пропущены индексы и искажен формат записи дома.
#На основе прочей информации восстановить индекс и записать в output.txt
#Если не удалось восстановить, в fail.txt

f = open('input.txt','r')
lines = f.readlines()

def has_index(address):
    index = 0;
    if address[0].isdigit() == False:
        index = 1
    elif len(address[0]) != 6:
        index = 2
    return index

def get_data(inp):
    res = ()
    data = inp.split(',')
    start = 0
    
    error = has_index(data)
    if error == 0:
        index = data[0]#index
    elif error == 1:
        index = None#index
        start = 1
    else:
        index = None#index
        start = 0
        
    city = data[1-start].split(" ")[2-start]#city
    street = data[2-start].split(" ")[2]#street
    house_inp = data[3-start].split(" ")#house
    if len(house_inp) == 1:#only digit
        house = house[1]
    else:
        for symbol in house_inp:
            if symbol.isdigit():
                house = symbol
    flat = data[4-start].split(" ")[2]
    res = (index, city, street, house, flat)
    return res

# index, city, street, house, flat
base = []
dic = {}

for addr in lines:
    base.append(get_data(addr))
    
for addr in base:
    if addr[0] != None:
        dic[(addr[1], addr[2], addr[3])] = addr[0]
        
good = open("output.txt", "w")
bad = open("fail.txt", "w")

for addr in base:
    Index = addr[0]
    City = addr[1]
    Street = addr[2]
    House = addr[3]
    key = (City, Street, House)
    if Index == None and not dic.has_key(key):
        bad.write('c. %s, st. %s, h. %s, fl. %s' % addr[1:])
    else:
        good.write(dic[key] + ' , c. %s, st. %s, h. %s, fl. %s' % addr[1:])
good.close()
bad.close()
quit()
