print("Hello World! This is my first Python Program. ")
print("""Welcome to Python Programming!,
    This is a multi-line string example.""")                    
print('This is also a multi-line string example.')

print("""I am signing up for Colab's 100 days of Python challenge!
        I will make sure to spend some time every day coding along, for a minimum of 10 minutes a day.
        I'll be using Google Colab, an amazing online notebook so I can do this from my phone wherever I happend to be. No excuses for not coding from the middle of a field!""")

print("Masukkan nama kamu: ")
nama = input()
print("Hai " + nama + "! Selamat Belajar Python!")

print("Halo apa kabar? ")
kabar = input()
print("Kabar saya " + kabar + ", terima kasih sudah bertanya! ")

x = 5
print(type(x)) #Bakal tampil <class 'int'>
nama = "Rizqi"
print(type(nama))
angka = 10
print(type(angka))
print("Berapa usiamu: ")
age = input()
print("Usia kamu adalah: " + age)
print(type(age))

buah = ["apel", "jeruk", "mangga"]
print(buah)
course = ["Python", "Java", "C++"]
print(course)

nilai = [90, 85, 92]
nilai.remove(85)
print(nilai)

buah = {"apel", "jeruk", "mangga"}
print(buah)
nilai = {90, 92, 85, 100}
print(nilai)
nilai.add(95)
print(nilai)

def greeting(name):
    print("Hello, " + name + " Welcome to python programming!")

greeting("Rizqi")

def my_function():
    print("Ini adalah fungsi pertama saya!")

def comb(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return comb(n-1, k-1) + comb(n-1, k)

def greet(name):
    print("Hai!, " + name + " Selamat datang di dunia pemrograman python!")

greet("Rizqi")

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")