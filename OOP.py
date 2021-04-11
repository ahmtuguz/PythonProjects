# class Person:
#     address="No information"
#     def __init__(self,name,year):
#         self.name=name
#         self.year=year
#     def calculateYear(self):
#         return 2021-self.year
# p1=Person(name="Deniz",year=1995)
# p2=Person(name="Mehmet",year=2000)
#
# p1.address="Konya"
# p2.address="İstanbul"
#
# print(p1.name," ",p1.year," ",p1.address)
# print(p2.name," ",p2.year," ",p2.address)
#
# print(p1.calculateYear())
# print(p2.calculateYear())

class Movie:
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
    def __str__(self):
        return f"{self.title} by {self.director}"
    def __len__(self):
        return self.duration
    def __del__(self):
        print("Film objesi silindi")
m=Movie("Film Adı","Yönetmen",120)
print(m.title," ",m.director," ",m.duration)
print(len(m))
print(m)
del m