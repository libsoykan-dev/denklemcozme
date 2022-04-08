    # Reel Sayılarda Tanımlı olan İkinci Dereceden Bir Bilinmeyenli Denklemlerin çözümü için oluşturulmuş bir Python programıdır.
    # Copyright (C) 2022 libsoykan-dev

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.


import math

print("Reel Sayılarda Tanımlı İkinci Derece Denklem Çözme Aracı v2.0")

print("Denkleminizin ax^2 + bx + c = 0 şeklinde olduğunu varsaydım...")

# Kişiye katsayılar sorulur

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print("Katsayılar toplamı: " + str(a + b + c)) # Katsayılar toplamı hesaplanarak yazdırılır

diskriminat = (b * b) - (4 * a * c) # Diskriminat (Δ) değeri hesaplanır

print("Diskriminat: " + str(diskriminat)) # Diskriminat değeri yazdırılır

if diskriminat < 0: # İmajiner sayılar kümesi tanımsız

    print("Bu denklem beni aşar. İmajiner sayılar tanımlı değil.")
    exit()
else: # Reel sayılarda tanımlı ise devam et

    cozumkumi1 = -1 * b + math.sqrt(diskriminat) # x1'in bölüneni hesaplanır

    cozumkumi2 = -1 * b - math.sqrt(diskriminat) # x2'nin bölüneni hesaplanır

    cozumkum2 = 2 * a # Bölen sayı hesaplanır

    cozumkumx1 = cozumkumi1 / cozumkum2 # x1 değeri hesaplanır

    cozumkumx2 = cozumkumi2 / cozumkum2 # x2 değeri hesaplanır

    bicim = input("Hacı denklemi çözdüm. Hangi biçimde yazayım?"
                      "\n1. Anlayacağım şekilde yaz (-b ± √Δ / 2a gibi)"
                      "\n2. Nasıl biliyorsan öyle yaz (0.31543234 gibi)"
                      "\n>") # Denklemi yazdırmak için kullanılacak biçim sorulur

    if bicim == "1": # Biçimi 1. öncüldeki şekilde yazdır

        print("x1 = (" + str(-1 * b) + " + " + "√" + str(diskriminat) + ")" + " / " + str(cozumkum2)) # x1

        print("x1 = (" + str(-1 * b) + " - " + "√" + str(diskriminat) + ")" + " / " + str(cozumkum2)) # x2

    elif bicim == "2": # Biçimi 2. öncüldeki şekilde yazdır

        print("x1 = " + str(cozumkumx1))

        print("x2 = " + str(cozumkumx2))

    else: # Biçim girdisi hatalı ise

        print("Adam gibi bir biçim söylesen olmaz mı? Ben nasıl biliyorsam öyle yazarım...") # :)

        print("x1 = " + str(cozumkumx1)) # x1

        print("x2 = " + str(cozumkumx2)) # x2

