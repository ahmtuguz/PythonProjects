#okulNo=4279
okulNo=int(input("Okul No Giriniz: "))

def my_random_number(okulNo):
    return (13*okulNo-11)%23

def my_iterations(okulNo):
    a=my_random_number(okulNo)

    for i in range(a):
        okulNo=((7*okulNo)-5)%47
    return a,okulNo

(m,n)=my_iterations(okulNo)

my_text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris laoreet venenatis varius.Nulla euismod, sapien et placerat dapibus, lacus sapien hendrerit nulla, vel dictum tellus justo sed urna.Curabitur finibus, erat vitae euismod rhoncus, lacus orci egestas nisi, ac convallis eros purus vel magna.Nullam a sollicitudin ligula. Fusce nec lacinia lacus. Quisque vel risus lorem. Phasellus fermentum nec mauris id finibus. Aliquam ligula eros, cursus eget ante at, eleifend hendrerit nibh. Praesent pulvinar placerat odio, ut feugiat nunc vehicula at. Vivamus porta magna sed lorem volutpat, vitae vulputate sapien pharetra. Ut volutpat elit id ex scelerisque, a congue purus feugiat."
my_text.lower()
alfabe={
    "o":18,
    "r":21,
    "e":6,
    "m":16,
    "i":11,
    "p":20,
    "s":22,
    "u":25,
    " ":0
}

print(my_text[m-1:n])
toplam=0

for i in range(0,len(my_text[m-1:n])):
    toplam+=alfabe[my_text[m-1]]
    m+=1

print("Kelime Toplamı: "+ str(toplam))