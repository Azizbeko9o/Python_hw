######    HOMEWORK-8
# class Hayvon:
#     def __init__(self, nomi, yoshi):
#         self.nomi = nomi
#         self.yoshi = yoshi
#         self.bolalar = [] 
#     def ovoz_chiqar(self):
#         print("Bu hayvon qandaydir ovoz chiqaryapti.")
#     def bola_qosh(self, bola):
#         self.bolalar.append(bola)
#         print(f"{self.nomi} ga {bola.nomi} ismli bola qo'shildi.")
#     def bolalarni_korish(self):
#         print(f"{self.nomi}ning bolalari:")
#         for bola in self.bolalar:
#             print(f"- {bola.nomi}, {bola.yoshi} yoshda")
# class It(Hayvon):
#     def ovoz_chiqar(self):
#         print("Vovv vovv!")
# class Mushuk(Hayvon):
#     def ovoz_chiqar(self):
#         print("Miyov miyov!")
# class Qush(Hayvon):
#     def ovoz_chiqar(self):
#         print("Chirilladi!")
# ona_it = It("Rex", 5)
# bola_it = It("Rox", 3)
# ona_mushuk = Mushuk("Mushka", 4)
# bola_mushuk = Mushuk("Mishka", 2)
# ona_qush = Qush("Chumchuq", 3)
# bola_qush = Qush("Chum", 1)
# ona_it.bola_qosh(bola_it)
# ona_mushuk.bola_qosh(bola_mushuk)
# ona_qush.bola_qosh(bola_qush)
# ona_it.ovoz_chiqar()
# ona_it.bolalarni_korish()
# ona_mushuk.ovoz_chiqar()
# ona_mushuk.bolalarni_korish()
# ona_qush.ovoz_chiqar()
# ona_qush.bolalarni_korish()
#########################################
# class Hayvon:
#     def __init__(self, nomi, yoshi, rangi):
#         self.nomi = nomi
#         self.yoshi = yoshi
#         self.rangi = rangi
#     def ovqatlanish(self):
#         print(f"{self.nomi} ovqatlanmoqda.")
#     def uxlash(self):
#         print(f"{self.nomi} uxlayapti.")
#     def yurish(self):
#         print(f"{self.nomi} yurib ketdi.")
# class It(Hayvon):
#     def __init__(self, nomi, yoshi, rangi, zot):
#         super().__init__(nomi, yoshi, rangi)
#         self.zot = zot
#     def yugurish(self):
#         print(f"{self.nomi} tez yuguryapti!")
# class Mushuk(Hayvon):
#     def __init__(self, nomi, yoshi, rangi, sevimli_ovqat):
#         super().__init__(nomi, yoshi, rangi)
#         self.sevimli_ovqat = sevimli_ovqat
#     def sakrash(self):
#         print(f"{self.nomi} derazaga sakradi.")
# class Qush(Hayvon):
#     def __init__(self, nomi, yoshi, rangi, qanot_uzunligi):
#         super().__init__(nomi, yoshi, rangi)
#         self.qanot_uzunligi = qanot_uzunligi
#     def uchish(self):
#         print(f"{self.nomi} osmonga uchib chiqdi!")
# print("--- Hayvonlar xatti-harakatlari ---")
# it = It("Rex", 4, "qora", "Ovcharka")
# it.yurish()
# it.yugurish()
# it.ovqatlanish()
# it.uxlash()
# print()
# mushuk = Mushuk("Mashqa", 2, "oq", "sut")
# mushuk.yurish()
# mushuk.sakrash()
# mushuk.ovqatlanish()
# mushuk.uxlash()
# print()
# qush = Qush("Chumchuq", 1, "sariq", 25)
# qush.yurish()
# qush.uchish()
# qush.ovqatlanish()
# qush.uxlash()
#########################################
# class Hayvon:
#     def __init__(self, nomi, yoshi, rangi):
#         self.nomi = nomi
#         self.yoshi = yoshi
#         self.rangi = rangi
#     def haqida(self):
#         print(f"Nomi: {self.nomi}, Yoshi: {self.yoshi}, Rangi: {self.rangi}")

#     def ovqatlanish(self):
#         print(f"{self.nomi} ovqatlanmoqda.")
# class It(Hayvon):
#     def yugurish(self):
#         print(f"{self.nomi} yuguryapti.")
# class Mushuk(Hayvon):
#     def uxlash(self):
#         print(f"{self.nomi} uxlmoqda.")
# class Qush(Hayvon):
#     def uchish(self):
#         print(f"{self.nomi} uchmoqda.")
# it = It("Rex", 3, "qora")
# mushuk = Mushuk("Mashqa", 2, "oq")
# qush = Qush("Chumchiq", 1, "sariq")
# print("--- It ---")
# it.haqida()
# it.ovqatlanish()
# it.yugurish()
# print("\n--- Mushuk ---")
# mushuk.haqida()
# mushuk.ovqatlanish()
# mushuk.uxlash()
# print("\n--- Qush ---")
# qush.haqida()
# qush.ovqatlanish()
# qush.uchish()
#########################################
# class Hisob:
#     def __init__(self, hisob_raqami, ism, balans):
#         self.hisob_raqami = hisob_raqami
#         self.ism = ism
#         self.balans = balans
#     def hisob_haqida(self):
#         print(f"Hisob raqami: {self.hisob_raqami}")
#         print(f"Mijoz ismi: {self.ism}")
#         print(f"Balans: {self.balans} so'm")
# a1 = Hisob("123456", "Azizbek Ne'matov", 15000000)
# a1.hisob_haqida()
#########################################
# import pickle 
# class Hisob:
#     def __init__(self, hisob_raqami, ism, balans):
#         self.hisob_raqami = hisob_raqami
#         self.ism = ism
#         self.balans = balans

#     def hisob_haqida(self):
#         print(f"Hisob raqami: {self.hisob_raqami}")
#         print(f"Mijoz ismi: {self.ism}")
#         print(f"Balans: {self.balans} so'm")
# class Bank:
#     def __init__(self):
#         self.accounts = {}
#         self.next_account_number = 1001 
#     def create_account(self, ism, boshlangich_balans):
#         raqam = str(self.next_account_number)
#         yangi_hisob = Hisob(raqam, ism, boshlangich_balans)
#         self.accounts[raqam] = yangi_hisob
#         self.next_account_number += 1
#         print(f"Hisob yaratildi! Raqam: {raqam}")
#     def view_account(self, hisob_raqami):
#         if hisob_raqami in self.accounts:
#             self.accounts[hisob_raqami].hisob_haqida()
#         else:
#             print("Bunday hisob mavjud emas.")

#     def deposit(self, hisob_raqami, summa):
#         if hisob_raqami in self.accounts:
#             self.accounts[hisob_raqami].balans += summa
#             print(f"{summa} so'm qo'shildi. Yangi balans: {self.accounts[hisob_raqami].balans} so'm")
#         else:
#             print("Hisob topilmadi.")

#     def withdraw(self, hisob_raqami, summa):
#         if hisob_raqami in self.accounts:
#             if self.accounts[hisob_raqami].balans >= summa:
#                 self.accounts[hisob_raqami].balans -= summa
#                 print(f"{summa} so'm yechildi. Yangi balans: {self.accounts[hisob_raqami].balans} so'm")
#             else:
#                 print("Balansda yetarli mablag' yo'q.")
#         else:
#             print("Hisob topilmadi.")

#     def save_to_file(self):
#         with open("hisoblar.pkl", "wb") as f:
#             pickle.dump((self.accounts, self.next_account_number), f)
#         print("Ma'lumotlar faylga saqlandi.")

#     def load_from_file(self):
#         try:
#             with open("hisoblar.pkl", "rb") as f:
#                 self.accounts, self.next_account_number = pickle.load(f)
#             print("Ma'lumotlar fayldan yuklandi.")
#         except FileNotFoundError:
#             print("Fayl topilmadi. Yangi bank tizimi boshlanmoqda.")
# bank = Bank()
# bank.load_from_file()
# bank.create_account("Sanjar", 5000000)
# bank.create_account("Bobur", 750000)
# bank.deposit("1001", 250000)
# bank.withdraw("1002", 300000)
# bank.view_account("1001")
# bank.view_account("1002")
# bank.save_to_file()
#########################################
# import pickle
# class Hisob:
#     def __init__(self, raqam, ism, balans):
#         self.raqam = raqam
#         self.ism = ism
#         self.balans = balans
#     def malumot(self):
#         print(f"Hisob raqami: {self.raqam}")
#         print(f"Ism: {self.ism}")
#         print(f"Balans: {self.balans} so'm")
# class Bank:
#     def __init__(self):
#         self.accounts = {}
#         self.next_account_number = 1001
#         self.load_from_file()
#     def create_account(self, ism, boshlangich_balans):
#         raqam = str(self.next_account_number)
#         hisob = Hisob(raqam, ism, boshlangich_balans)
#         self.accounts[raqam] = hisob
#         self.next_account_number += 1
#         self.save_to_file()
#         print(f"Yangi hisob yaratildi. Raqam: {raqam}")
#     def view_account(self, raqam):
#         if raqam in self.accounts:
#             print("Hisob topildi:")
#             self.accounts[raqam].malumot()
#         else:
#             print("Xatolik: bu hisob raqami topilmadi.")
#     def save_to_file(self):
#         with open("hisoblar.pkl", "wb") as f:
#             pickle.dump((self.accounts, self.next_account_number), f)
#     def load_from_file(self):
#         try:
#             with open("hisoblar.pkl", "rb") as f:
#                 self.accounts, self.next_account_number = pickle.load(f)
#         except FileNotFoundError:
#             self.accounts = {}
#             self.next_account_number = 1001
# bank = Bank()
# while True:
#     print("\n--- Bank Dasturi ---")
#     print("1. Hisob yaratish")
#     print("2. Hisobni ko'rish")
#     print("3. Chiqish")
#     tanlov = input("Tanlovni kiriting (1-3): ")
#     if tanlov == "1":
#         ism = input("Ismingizni kiriting: ")
#         balans = int(input("Boshlang'ich balans: "))
#         bank.create_account(ism, balans)
#     elif tanlov == "2":
#         raqam = input("Hisob raqamingizni kiriting: ")
#         bank.view_account(raqam)
#     elif tanlov == "3":
#         print("Dastur yakunlandi.")
#         break
#     else:
#         print("Noto'g'ri tanlov. Qayta urinib ko'ring.")
#########################################
# hisoblar = {
#     "1001": {"ism": "Bobur", "balans": 500000},
#     "1002": {"ism": "Sanjar", "balans": 300000}
# }
# raqam = input("Hisob raqamingizni kiriting: ")
# if raqam in hisoblar:
#     try:
#         summa = int(input("Qo'shiladigan summani kiriting: "))
#         if summa > 0:
#             hisoblar[raqam]["balans"] += summa
#             print(f"{summa} so'm muvaffaqiyatli qo'shildi.")
#             print(f"Yangi balans: {hisoblar[raqam]['balans']} so'm")
#         else:
#             print("Xatolik: summa musbat bo'lishi kerak.")
#     except ValueError:
#         print("Xatolik: faqat raqam kiriting.")
# else:
#     print("Xatolik: bunday hisob raqami topilmadi.")
#########################################
# hisoblar = {
#     "1001": {"ism": "Bobur", "balans": 500000},
#     "1002": {"ism": "Sanjar", "balans": 300000}
# }
# raqam = input("Hisob raqamingizni kiriting: ")
# if raqam in hisoblar:
#     try:
#         summa = int(input("Yechiladigan summani kiriting: "))
#         if 0 < summa <= hisoblar[raqam]["balans"]:
#             hisoblar[raqam]["balans"] -= summa
#             print(f"{summa} so'm muvaffaqiyatli yechildi.")
#             print(f"Yangi balans: {hisoblar[raqam]['balans']} so'm")
#         else:
#             print("Xatolik: Balansda yetarli mablag' yo'q yoki noto'g'ri summa.")
#     except ValueError:
#         print("Xatolik: faqat raqam kiriting.")
# else:
#     print("Xatolik: bunday hisob raqami topilmadi.")
#########################################
import pickle
hisoblar = {
    "1001": {"ism": "Bobur", "balans": 500000},
    "1002": {"ism": "Sanjar", "balans": 300000}
}
def save_to_file():
    with open("accounts.txt", "wb") as f:
        pickle.dump(hisoblar, f)
    print("Hisoblar muvaffaqiyatli faylga saqlandi.")
def load_from_file():
    global hisoblar
    try:
        with open("accounts.txt", "rb") as f:
            hisoblar = pickle.load(f)
        print("Hisoblar fayldan muvaffaqiyatli yuklandi.")
    except FileNotFoundError:
        print("Fayl topilmadi, yangi hisoblar yaratish boshlanadi.")
load_from_file()
def create_account(raqam, ism, balans):
    hisoblar[raqam] = {"ism": ism, "balans": balans}
    save_to_file()
    print(f"Yangi hisob yaratildi. Raqamingiz: {raqam}")
def view_account(raqam):
    if raqam in hisoblar:
        print(f"Ism: {hisoblar[raqam]['ism']}")
        print(f"Balans: {hisoblar[raqam]['balans']} so'm")
    else:
        print("Xatolik: bunday hisob raqami topilmadi.")
def deposit(raqam, summa):
    if raqam in hisoblar:
        if summa > 0:
            hisoblar[raqam]["balans"] += summa
            save_to_file()
            print(f"{summa} so'm muvaffaqiyatli qo'shildi.")
            print(f"Yangi balans: {hisoblar[raqam]['balans']} so'm")
        else:
            print("Xatolik: summa musbat bo'lishi kerak.")
    else:
        print("Xatolik: hisob topilmadi.")
def withdraw(raqam, summa):
    if raqam in hisoblar:
        if 0 < summa <= hisoblar[raqam]["balans"]:
            hisoblar[raqam]["balans"] -= summa
            save_to_file()
            print(f"{summa} so'm muvaffaqiyatli yechildi.")
            print(f"Yangi balans: {hisoblar[raqam]['balans']} so'm")
        else:
            print("Xatolik: yetarli mablag' mavjud emas yoki noto'g'ri summa.")
    else:
        print("Xatolik: hisob topilmadi.")
view_account("1001")
view_account("1002")
deposit("1001", 100000)
withdraw("1002", 50000)
save_to_file()
