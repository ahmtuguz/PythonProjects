import requests
import json

class Movie:
    def __init__(self):
        self.api_url="https://api.themoviedb.org/3/"
        self.api_key="e8a9d5f82d78ca210c8076d648685c12"

    def getTopRated(self):
        result=requests.get(f"{self.api_url}movie/top_rated?api_key={self.api_key}&language=en-US&page=1") 
        return result.json()
    def getSearchMovie(self,keyword):
        result=requests.get(f"{self.api_url}search/keyword?api_key={self.api_key}&query={keyword}&page=1") 
        return result.json()
        
xmovie=Movie()
ymovie=Movie()
while True:
    seçim=input("1- TopRated Movie\n2- Search Movie\n3- Exit\nSeçim:")
    if seçim=="3":
        break
    elif seçim=="1":
        movie=xmovie.getTopRated()
        for movies in movie["results"]:
         print(movies["title"])
    elif seçim=="2":
        x=input("aramak istenilen kelime: ")
        movie=ymovie.getSearchMovie(x)
        for movies in movie["results"]:
         print(movies["name"])     
         
  
