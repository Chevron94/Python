import os

class Address:
    def __init__(self, index, country,city,street,house,flat):
        self.addr = []
        self.addr.append(index)
        self.addr.append(country)
        self.addr.append(city)
        self.addr.append(street)
        self.addr.append(house)
        self.addr.append(flat)
    def GetSep(self):
        return ' '
    
    def Form_Output_String(self,sep):
        tmp = ' '+sep+' '
        return ('%s.' % tmp.join(self.addr))
    
    def __str__(self):
        return self.Form_Output_String(self.GetSep())

    def Print_To_File(self,txt):
        txt.write(self.Form_Output_String(self.GetSep())+'\n')
                
class Russian_Address(Address):
    def GetSep(self):
        return ','
    
class International_Address(Address):
    def GetSep(self):
        return '/'
    
class Address_Book:
    def __init__(self):
        self.address_list = []
    def append(self, address):
        self.address_list.append(address)
    def print_to_file(self, filename):
        txt = open(filename, 'w')
        for i in self.address_list:
            i.Print_To_File(txt)
        txt.close()
    

add = Russian_Address('394090','Россия','Воронеж','Новосибирская','27','280')
add1 = International_Address('394090','Россия','Воронеж','Новосибирская','27','280')
ad_book = Address_Book()
ad_book.append(add)
ad_book.append(add1)
ad_book.print_to_file('test.txt')
print add
print add1
