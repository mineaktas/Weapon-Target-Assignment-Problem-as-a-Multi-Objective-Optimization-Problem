import random
import math
# Problemde 2 site var; 1.siteda 5 silah 4 hedef  -  2.siteda 4 silah 3 hedef. Önce açı hesabı ile TSP süreleri hesaplanarak amaç fonksiyonu yazdırıldı. Sonra PK ve FlightDuration için amaç fonk yzdırıldı.
#başlangıç noktası x:25 y:5 bitiş noktası x:25 y:10 olarak girilir (namlunun noktaları).
def generate_random_lines(num, start_point):
    lines = []
    for _ in range(num):
        end_x = random.randint(0, 50)  # Rastgele bitiş noktasının x koordinatı (-10 ile 10 arasında)
        end_y = random.randint(start_y, 50)  # Rastgele bitiş noktasının y koordinatı (-10 ile 10 arasında)
        lines.append((start_point, (end_x, end_y)))
    lines.insert(0,namlu)
    return lines

# Başlangıç noktasını kullanıcıdan al
start_x= int(input("Başlangıç noktasının X koordinatını girin: "))
start_y= int(input("Başlangıç noktasının Y koordinatını girin: "))
finish_x= int(input("Bitiş noktasının X koordinatını girin: "))
finish_y= int(input("Bitiş noktasının Y koordinatını girin: "))
namlu=((start_x,start_y),(finish_x,finish_y))
start_point = (start_x, start_y)


# hedefler oluştur
adet = int(input("Oluşturulacak hedef sayısını girin: "))
lines = generate_random_lines(adet, start_point)
#iki hedef arasındaki açıyı hesapla
def calculate_angle(p1, p2):
    # İki noktanın açıyı tanımlayan vektörü
    v = (p2[0] - p1[0], p2[1] - p1[1])

    angle = math.atan2(abs(v[1]), abs(v[0]))
    if p2[0] < p1[0]:
        return 90 - math.degrees(angle)
    if p2[0] > p1[0]:
        return 90 - math.degrees(angle)
    if p2[0]== p1[0]:
        return 0
    if (p1[0]< start_point[0] and p2[0]>start_point[0]) or (p2[0]< start_point[0] and p1[0]>start_point[0]):
        return 180-math.degrees(angle)

list=[]
for n in lines[1:]:
    list.append(n[1])
list.insert(0,namlu[0])

angleMat=[]
for i in list:
    satir=[]
    for j in list:
        satir.append(calculate_angle(i,j))
    angleMat.append(satir)


for i in list:
    angle1 = calculate_angle(list[0], i)
    for j in list:
        angle2 = calculate_angle(list[0], j)
        angle=angle1+angle2
        if i[0]==j[0] and i[1]==j[1]:
            angle=0
        if (i[0]<start_point[0] and j[0]<start_point[0]) or (i[0]>start_point[0] and j[0]>start_point[0]):
            angle=abs(angle1-angle2)


omega = int(input("Açısal hızı girin (radyan/sn): "))
angleMatDur=[]
for i in angleMat:
    strc=[]
    for j in i:
        time =j/omega
        strc.append(round(time,2))
    angleMatDur.append(strc)

def print_matrix(angelMatDur):
    for row in angelMatDur:
        for element in row:
            print(f"{element:.2f}", end="\t")
        print()

print_matrix(angleMatDur)


TSP="Min ="
a = 0
for i in angleMatDur:
    b=0
    for j in i:
        TSP +=str(round(j,3))+"*w"+str(a)+str(b)+"+"
        b +=1
    a += 1
print("TSP İÇİN",TSP)


def generate_random_coordinates(num_points):
    coordinates = []
    for _ in range(num_points):
        x = random.randint(0, 10000)
        y = random.randint(0, 10000)
        z = random.randint(0, 10000)
        coordinates.append((x, y, z))
    return coordinates

def generate_random_speed():
    return random.randint(300, 2000)

def calculate_distance(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distance

#olasılık ürettirme
def generate_random_probability(weapon_count):
    probabilities = []
    for _ in range(weapon_count):
        p = random.uniform(0, 1)
        probabilities.append(round(p,2))
    return probabilities

# Bölgeleri ve silah sayılarını oluşturma
num_regions = int(input("Bölge sayısını girin: "))
region_weapon_counts = []
targets = []

for i in range(num_regions):
    num_points = int(input(f"Bölge {i+1} için hedef sayısını girin: "))
    target = generate_random_coordinates(num_points)
    targets.append(target)
    weapon_count = int(input(f"Bölge {i+1} için silah sayısını girin: "))
    region_weapon_counts.append(weapon_count)

# Hedef sayısını ve konumları oluşturma
points = generate_random_coordinates(num_points)
point_speeds = [generate_random_speed() for _ in range(num_points)]

# Her bölge için silah hızlarını ve mesafeleri hesaplama
time_matrix = []
for region_index, target in enumerate(targets):
    weapon_speeds = [generate_random_speed() for _ in range(region_weapon_counts[region_index])]
    region_times = []

    for weapon_index, coordinate in enumerate(target):
        distances = []
        for point in points:
            distance = calculate_distance(coordinate, point)
            distances.append(distance)

        weapon_times = []
        for point_index, distance in enumerate(distances):
            if weapon_index < len(weapon_speeds) and point_index < len(point_speeds):
                total_speed = weapon_speeds[weapon_index] + point_speeds[point_index]
                if total_speed != 0:
                    time = distance / total_speed
                else:
                    time = float('inf')
                weapon_times.append(round(time,2))
        region_times.append(weapon_times)

    time_matrix.append(region_times)


# Matrisi yazdırma
for region_index, region_times in enumerate(time_matrix):
    print(f"Bölge {region_index + 1} için süre matrisi:")
    for weapon_index, weapon_times in enumerate(region_times):
        for point_index, time in enumerate(weapon_times):
            print(f"{time:.2f}", end="\t")
        print()

#amaç fonksiyonu yazdırma
flightduration="min="
a=1  #en sona bölge
for i in time_matrix:
    b=1 #ortaya hedef
    for j in i:
        c=1 #en başa
        for w in j:
            flightduration+= str(w)+"*y"+str(b)+str(c)+str(a)+"+"
            c+=1
        b+=1
    a+=1
print("FLIGHTDURATION için ",flightduration)


numofweapon=0
for i in region_weapon_counts:
    numofweapon+=i

pb=generate_random_probability(numofweapon)
print("pb",pb)

#amaç fonksiyonu yazdırma
pk="max="
a=1  #en sona bölge
for i in time_matrix:
    b=1 #ortaya hedef
    for w in pb:
        c = 1  # en başa
        for j in i:
            pk+= str(w)+"*y"+str(b)+str(c)+str(a)+"+"
            c+=1
        b+=1
    a+=1
print("PK için ",pk)

#hedeflere ait doğruları ve namluyu çizdir
import matplotlib.pyplot as plt

def plot_lines(lines):
    # Koordinat sistemi figürünü oluştur
    plt.figure()

    # Doğruları çiz
    for line in lines:
        p1, p2 = line
        x_coords = [p1[0], p2[0]]
        y_coords = [p1[1], p2[1]]
        plt.plot(x_coords, y_coords, color='red')


    # Eksenleri ayarla
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # Grafik penceresini göster
    plt.show()

# Doğruları çiz
plot_lines(lines)