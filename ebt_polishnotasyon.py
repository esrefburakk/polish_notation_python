__author__ = "Eşref Burak Tanrıseven"

#alttaki fonksiyonumuzda operatörlerimizi belirttik
def operator(operate):
    return ((operate == '+') | (operate == '-') | (operate == '*') | (operate == '/'))

#alttaki fonksiyonumuzda main(ana) kod bloğumuzdan gelen listede hangi operatörlerin seçildiğini anlamak için operatörlere göre return değerleri belirledik
def operator_sec(operate):
    if operate == '+':
        return 1
    elif operate == '-':
        return 2
    elif operate == '*':
        return 3
    elif operate == '/':
        return 4
    else:
        print("Girdiğiniz operatör doğru operatör değildir.")

#alttaki fonksiyonumuz islemYap fonksiyonudur yani seçilen operatörlere ve girilen sayılara göre işlemler yapılmaktadır.
def islemYap(operate,sayi1,sayi2):
    operatore = operator_sec(operate)
    if operatore == 1:
        return sayi1 + sayi2
    elif operatore == 2:
        return sayi1 - sayi2
    elif operatore == 3:
        return sayi1 * sayi2
    elif operatore == 4:
        return sayi1 / sayi2
    else:
        print("Seçdiğiniz operatörlere göre işlemler yapılamamıştır")
        
#2 adet liste sonuçları tutacağımız liste,genel listemiz,operatörlerin listesi,son operatörü tutacak olan bir değişken ve sonucu tutacak değişken yazılmıştır. 
liste1 = []
liste2 = []
genelListe = []
operatorListe = []
sonOperator = ''
sonuc = 0

#polish notasyonuna uygun olarak girilecek metni klavyeden istedik ve girilen değerleri ayrı ayrı eleman olarak tutsun diye split() fonksiyonu ile boşluklu olarak ayırdık.
notasyon = input("Polish notasyonuna göre işlem yapacağınız operatör ve sayıları giriniz: ")
genelListe = notasyon.split(" ")

#bir adet durum değeri aldık boolen olarak bu da bizim ileride operatörlerin olup olmadığına göre True False değeri döndürecek.Bu yüzden başlangıçta False değeri atadık.
durum = False

#son operatörü de yok olarak atadık.
sonOperator = ""

#bir adet for döngüsü oluşturduk ve bu döngüde i değerimiz genel listemizin içerisinde dolandı.
for i in genelListe:
    #bir adet if else kurduk buradaki if else imizin amacı genel listemizin içerisinde operatör değerleri var mı yok mu onu anlamak.
    if (operator(i) == True):
        #eğer var ise son operatör değerimizi değiştirip i yapıyor ve durum değişkenimizi de True ya çeviriyoruz.Ve son olarak da 1.listemize i elemanını sonuna eklemek için append() fonksiyonunu kullanıyoruz.
        durum = True
        sonOperator = i
        liste1.append(i)
    elif (operator(i) == False):
        #eğer yok ise demektir ki listenin içindeki bu değer sayısal bir değerdir.Bu yüzden operatör listesinin sonuna bu değeri integer olarak ekliyoruz.
        operatorListe.append(int(i))
        #ardından bir if else daha ekliyoruz bunun sebebi operatör listesinin içindeki elemanlarla işlem yapacağız bunun 
        #tespiti için.Uzunluk 2 mi diye bakıyoruz çünkü 2 farklı değer(sayı) ve 1 adet operatörümüz olacak üstteki 
        #islemYap fonksiyonumuzun içi 3 değer aldacak şekilde kurduğumuz için.
        if (len(operatorListe) == 2):
            #bir adet daha if else kuruyoruz bu sefer de durum değişkenine bakıyoruz yani yukarıda önceden operatör değerimiz bulundu mu diye
            if(durum == True):
                #eğer operatörümüz önceden bulunduysa islemYap() fonksiyonumuzu devreye sokuyoruz ve liste1 e eklediğimiz değerleri uygun olarak 
                #islemYap() fonksiyonumuzu gönderiyoruz ve bunun sonucunu bir sonuc değişkenine atıyoruz.
                #ardından liste1 ile işimizi bitti ve sonucu bulduğumuz için liste1 in uzunluktan 1 önceki elemanına kadar siliyoruz ve operatör sadece elimizde kalıyor 
                #ve operatorListe sinin de 0 dan 2.elemanlarına kadar olan elemanları siliyoruz siliyoruz ve
                #2.listemiz yani sonuçları toplayacağımız listemize sonucumuzu append() fonksiyonu ile ekliyoruz.
                #ve ardından durum değerimizi False yapıyoruz ki tekrar bu işlemlere girdiğinde herhangi bir sorun ile karşılaşmayalım
                uzunluk1 = len(liste1)
                sonuc = islemYap(liste1[uzunluk1-1],operatorListe[0],operatorListe[1])
                del operatorListe[0:]
                del liste1[uzunluk1-1]
                liste2.append(sonuc)
                durum = False
            else:
                #eğer durumumuz false ile yani önceden herhangi bir operatör bulunmadı ise liste2 mize yani sonuç listemize 
                #direkt olarak operatorlistemizdeki 1. ve 2. elemanları ekliyoruz.
                liste2.append(operatorListe[0])
                liste2.append(operatorListe[1])
        else:
            #eğer operatorListe mizin uzunluk değeri 2 den farklı bir değer ise bir if kuruyoruz ve bu ifte i değerimizi genel listemizin sonuna alıyoruz.
            #ve ardından liste2 yani sonuç listemize direk bu i değerini ekliyoruz.
            if (i == genelListe[-1]):
                liste2.append(int(i))
                
uzunluk2 = len(liste1) #liste1 imizin uzunluk değerini buluyoruz çünkü aşağıda kuracağımız for döngüsünde işlemlerimizi
#liste1 imizin uzunluğuna kadar yapmamız gerekiyor.

for i in range(uzunluk2):
    #i değerimiz liste1 in uzunluk değerine kadar sayısal olarak artıyor ve o kadar döngü işlemi yapıyoruz.
    #önceki for döngümüzde liste2 yani sonuç listemize elemanlar eklemiştik ve liste1 imizde de operatör değerlerimiz bulunuyor idi
    #islemYap fonksiyonumuza tekrardan başvuruyoruz çünkü liste2 nin içinde önceki for döngüsünden kalan sonuc değerlerimiz mevcut
    #aynı şekilde islemYap fonksiyonumuzda ilk olarak liste 1 imizin son değerine gidiyoruz çünkü önceki fordan da biliyoruz ki liste1'in
    #son değeri operatör değerimiz(+ - * /) ve ardından sonuc elemanlarımız liste 2 de olduğu için liste2deki 1. ve 2.elemanlarımızı islemYap fonksiyonuna yolluyoruz.
    #ve sonucu sonuc değişkenine atıyoruz.Ardından liste2 nin 0 ve 2.eleman indislerine kadar olar elemanalrı siliyoruz.Bu sayede geride kalan 
    #sonuc elemanlarımız var ise onlar liste2[0] ve liste2[1] değerlerine geliyorlar.Ardından liste2 nin 0. elemanına sonuc değişkenimizi ekliyoruz
    #ve liste1 in son elemanına kadar olan değerleri siliyoruz ve elimizde var ise geriye operatör değerimiz kalıyor
    sonuc = islemYap(liste1[len(liste1)-1],liste2[0],liste2[1])
    del liste2[0:2]
    liste2.insert(0,sonuc)
    del liste1[len(liste1)-1]
#ve son olarak sonuc değerimiz liste2 nin 0. indisteki elemanına denk düşeceği için liste2 nin 0. elemanını sonucumuz olarak yazdırıyoruz.
print("Sonucunuz: ",liste2[0])

