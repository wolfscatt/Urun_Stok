#-------------------------------------------- Sözlük Veri Türünü Kullanarak Stok Oluşturan Program --------------------------------------------

urunler = {}

def urun_ekle():
  # global id,kategori,isim,renk,adet,alis,satis
  id = input("Eklemek istediğiniz ürünün id numarasını giriniz(6 haneli olmalıdır ve ilk 3 hanesi kategoriyi temsil edecektir.\n(Telefon için 101, bilgisayar için 201, beyaz eşya için 301 ve ev aletleri için 401 ile başlamalıdır.)): ")
  while True:
    if len(id) != 6:
      print("id numarası 6 haneli olmalıdır!")
      id = input("Eklemek istediğiniz ürünün id numarasını giriniz(6 haneli olmalıdır ve ilk 3 hanesi kategoriyi temsil edecektir.\n(Telefon için 101, bilgisayar için 201, beyaz eşya için 301 ve ev aletleri için 401 ile başlamalıdır.)): ")
    try:
      id = int(id)
    except:
      print("Girdiğiniz id sadece rakam içermelidir")
      id = input("Eklemek istediğiniz ürünün id numarasını giriniz(6 haneli olmalıdır ve ilk 3 hanesi kategoriyi temsil edecektir.\n(Telefon için 101, bilgisayar için 201, beyaz eşya için 301 ve ev aletleri için 401 ile başlamalıdır.)): ")   
    else :
      break

  kategori = input("Eklemek istediğiniz ürünün kategorisini giriniz('Telefon, Bilgisayar, Beyaz Eşya, Ev Aletleri'): ")
  while True: 
    id = str(id) 
    while kategori == 'Telefon' or kategori == 'telefon':
      if id[0:3] != '101':
        print("Telefon kategorisi için id değeri 101 ile başlamalıdır!")
        id = input("Eklemek istediğiniz ürünün id numarasını giriniz(6 haneli olmalıdır ve ilk 3 hanesi kategoriyi temsil edecektir.\n(Telefon için 101, bilgisayar için 201, beyaz eşya için 301 ve ev aletleri için 401 ile başlamalıdır.)): ")   
        kategori = input("Eklemek istediğiniz ürünün kategorisini giriniz('Telefon, Bilgisayar, Beyaz Eşya, Ev Aletleri'): ")
      else:
        break
    while kategori == 'Bilgisayar' or kategori == 'bilgisayar':
      if id[0:3] != '201':
        print("Bilgisayar kategorisi için id değeri 201 ile başlamalıdır!")
        id = input("Eklemek istediğiniz ürünün id numarasını giriniz(6 haneli olmalıdır ve ilk 3 hanesi kategoriyi temsil edecektir.\n(Telefon için 101, bilgisayar için 201, beyaz eşya için 301 ve ev aletleri için 401 ile başlamalıdır.)): ")   
        kategori = input("Eklemek istediğiniz ürünün kategorisini giriniz('Telefon, Bilgisayar, Beyaz Eşya, Ev Aletleri'): ")
      else:
       break
    while kategori == 'Beyaz Eşya' or kategori == 'beyaz eşya':
      if id[0:3] != '301':
        print("Beyaz Eşya kategorisi için id değeri 301 ile başlamalıdır!")
        id = input("Eklemek istediğiniz ürünün id numarasını giriniz(6 haneli olmalıdır ve ilk 3 hanesi kategoriyi temsil edecektir.\n(Telefon için 101, bilgisayar için 201, beyaz eşya için 301 ve ev aletleri için 401 ile başlamalıdır.)): ")   
        kategori = input("Eklemek istediğiniz ürünün kategorisini giriniz('Telefon, Bilgisayar, Beyaz Eşya, Ev Aletleri'): ")
      else:
        break
    while kategori == 'Ev Aletleri' or kategori == 'ev aletleri':
      if id[0:3] != '401':
        print("Ev Aletleri kategorisi için id değeri 401 ile başlamalıdır!")
        id = input("Eklemek istediğiniz ürünün id numarasını giriniz(6 haneli olmalıdır ve ilk 3 hanesi kategoriyi temsil edecektir.\n(Telefon için 101, bilgisayar için 201, beyaz eşya için 301 ve ev aletleri için 401 ile başlamalıdır.)): ")   
        kategori = input("Eklemek istediğiniz ürünün kategorisini giriniz('Telefon, Bilgisayar, Beyaz Eşya, Ev Aletleri'): ")
      else:
        break
    break

  isim = input("Eklemek istediğiniz ürünün ismini giriniz: ")
  renk = input("Eklemek istediğiniz ürünün rengini giriniz: ")
  adet = input("Eklemek istediğiniz ürünün adedini giriniz: ")
  alis = input("Eklemek istediğiniz ürünün alış fiyatını giriniz: ")

  while True: 
    try:
      alis = int(alis)
    except:
      print("Girdiğiniz alış fiyatı sadece rakam içermelidir")
      alis = input("Eklemek istediğiniz ürünün alış fiyatını giriniz: ")
    break
  satis = input("Eklemek istediğiniz ürünün satis fiyatını giriniz: ")

  while True:
    try:
      satis = int(satis)
    except:
      print("Girdiğiniz satış fiyatı sadece rakam içermelidir")
      satis = input("Eklemek istediğiniz ürünün satis fiyatını giriniz: ")
    break
  urunler.update({id:{kategori:{'Adet':adet, 'Alış Fiyatı':alis, 'Renk':renk, 'Satış Fiyatı':satis, 'İsim':isim}}})

def urun_cikar():
  cikar = input("Çıkarmak İstediğiniz ürünün id numarasını giriniz: ")
  liste = list(urunler.keys())
  for i in liste:
    if cikar == i:
      urunler.pop(cikar)

def urun_bilgi_guncelle():
  guncelle = input("Güncellemek İstediğiniz ürünün id numarasını giriniz: ")
  liste = list(urunler.keys())
  for i in liste:
    if guncelle == i:
      id = input("Güncellemek İstediğiniz ürünün yeni id numarasını giriniz: ")
      kategori = input("Güncellemek istediğiniz kategori bilgisini giriniz('Telefon, Bilgisayar, Beyaz Eşya, Ev Aletleri'): ")
      isim = input("Güncellemek istediğiniz isim bilgisini giriniz: ")
      renk = input("Güncellemek istediğiniz renk bilgisini giriniz: ")
      adet = input("Güncellemek istediğiniz adet bilgisini giriniz: ")
      alis = input("Güncellemek istediğiniz alış fiyatını giriniz: ")
      satis = input("Güncellemek istediğiniz satis fiyatını giriniz: ")
    else:
      guncelle = input("Stokta bu id numarasına sahip bir ürün bulunamadı lütfen güncellemek istediğiniz ürünün id numarasını tekrar giriniz: ")
  urunler.update({id:{kategori:{'Adet':adet, 'Alış Fiyatı':alis, 'Renk':renk, 'Satış Fiyatı':satis, 'İsim':isim}}})

def stok_goruntule():
  try:
    print(urunler)
    # print(f"Stoktaki Ürünler:\n{urunler[id][kategori]['Adet']} adet {urunler[id][kategori]['İsim']} marka {kategori} bulunmaktadır.")
  except:
    print("Stokta Ürün Bulunamadı!")

def calistir():
  while True:
    urun = input("Ürün Eklemek için 1'e, çıkarmak için 2'ye, güncellemek için 3'e ve stoğu görüntülemek için 4'e çıkmak için 5'e basınız: ") 
    while not (urun == "1" or urun == "2" or urun == "3" or urun == "4" or urun == "5"):
        print("Lütfen sadece belirtilen rakamları giriniz!...")
        urun = input("Ürün Eklemek için 1'e, çıkarmak için 2'ye, güncellemek için 3'e ve stoğu görüntülemek için 4'e basınız: ") 
    if(urun == "1"):
      urun_ekle()
    elif urun == "2":
      urun_cikar()
    elif urun == "3":
      urun_bilgi_guncelle()
    elif urun == "4":
      stok_goruntule()
    elif urun == "5":
      break
       
calistir()