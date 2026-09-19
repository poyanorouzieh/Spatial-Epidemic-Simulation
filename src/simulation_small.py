import random
import copy 
import matplotlib.pyplot as plt
import matplotlib.colors as pltc
print("--------------------------------------------- ") 
p1= float(input("enter p1 :"))
p2= float(input('enter p2 :'))
pr= float(input('enter pr :'))
pd= float(input('enter pd :'))
pi= float(input('enter pi :'))
f = float(input('enter f  :'))
print("--------------------------------------------- ") 
Q={}
for i in range(1,11) :
    for j in range(1,11):
        Q[(i,j)]=['S', 0 ,0 ,0 ,0]
Test = int(input("enter how many sick cel do you want : "))
for _ in range(Test) :
    i = random.choice([1,2,3,4,5,6,7,8,9,10])
    j = random.choice([1,2,3,4,5,6,7,8,9,10])
    Q[(i,j)][0] = "I"
    Q[(i,j)][4] = 1
Qt = copy.deepcopy(Q)
Qf = copy.deepcopy(Q)
#مکان تمام نقاط تعریف شد 
def loc(fi,te):
    if fi >10 :
        fi = fi - 10
    if fi < 0 : 
        fi = 11 + fi
    if te < 0 :
        te = 11 + te
    if te >10 :
        te = te - 10
    if fi == 0 :
        fi = 10
    if te == 0 :
        te = 10
    return Q[(fi,te)][0] 
# تابع تشخیص وضعیت تمام نقاط تعریف شد 
def cor(fi,te) :
    k1 = 0 
    k2 = 0
    if loc(fi+1,te) == 'I' :
        k1 = k1 + 1
    if loc(fi-1,te) == 'I' :
        k1 = k1 + 1
    if loc(fi,te+1) == 'I' :
        k1 = k1 + 1
    if loc(fi,te-1) == 'I' :
        k1 = k1 + 1
    if loc(fi+1,te+1) == 'I' :
        k1 = k1 + 1
    if loc(fi-1,te-1) == 'I' :
        k1 = k1 + 1
    if loc(fi+1,te-1) == 'I' :
        k1 = k1 + 1
    if loc(fi-1,te+1) == 'I' :
        k1 = k1 + 1
    if loc(fi+2,te) == 'I' :
        k2 = k2 + 1
    if loc(fi-2,te) == 'I' :
        k2 = k2 + 1
    if loc(fi,te+2) == 'I' :
        k2 = k2 + 1
    if loc(fi,te-2) == 'I' :
        k2 = k2 + 1
    if loc(fi+2,te+2) == 'I' :
        k2 = k2 + 1
    if loc(fi-2,te-2) == 'I' :
        k2 = k2 + 1
    if loc(fi+2,te-2) == 'I' :
        k2 = k2 + 1
    if loc(fi-2,te+2) == 'I' :
        k2 = k2 + 1
    if loc(fi+1,te-2) == 'I' :
        k2 = k2 + 1
    if loc(fi-1,te-2) == 'I' :
        k2 = k2 + 1
    if loc(fi+2,te+1) == 'I' :
        k2 = k2 + 1
    if loc(fi-2,te+1) == 'I' :
        k2 = k2 + 1
    if loc(fi+2,te-1) == 'I' :
        k2 = k2 + 1
    if loc(fi-2,te-1) == 'I' :
        k2 = k2 + 1
    if loc(fi+1,te+2) == 'I' :
        k2 = k2 + 1
    if loc(fi-1,te+2) == 'I' :
        k2 = k2 + 1
    return [k1,k2]
# تابع شمارش k1 , k2 تعریف شد 
def cord(fi,te) :
    k3 = 0
    if loc(fi+1,te) == 'D' :
        k3 = k3 + 1
    if loc(fi-1,te) == 'D' :
        k3 = k3 + 1
    if loc(fi,te+1) == 'D' :
        k3 = k3 + 1
    if loc(fi,te-1) == 'D' :
        k3 = k3 + 1
    if loc(fi+1,te+1) == 'D' :
        k3 = k3 + 1
    if loc(fi-1,te-1) == 'D' :
        k3 = k3 + 1
    if loc(fi+1,te-1) == 'D' :
        k3 = k3 + 1
    if loc(fi-1,te+1) == 'D' :
        k3 = k3 + 1
    return k3
#تعداد افراد مرده در فاصله 1
def ran(fi,te) :
    n = Q[(fi,te)][1]
    r = Q[(fi,te)][2]
    z = Q[(fi,te)][3]
    if loc(fi,te) == "S" :
        Pt = (f**n)*(1-((1-p1)**(cor(fi,te)[0]))*((1-p2)**(cor(fi,te)[1])))
        Qt[(fi,te)][0] = random.choices(["S","I"] , weights=[1-Pt , Pt ])[0]
        if Qt[(fi,te)][0] == "S" :
            Qt[(fi,te)][4] = 0
        if Qt[(fi,te)][0] == "I" :
            Qt[(fi,te)][4] = 1
    elif loc(fi,te) == "I" :
        Qt[(fi,te)][0] = random.choices(["I","R","D"] , weights=[pi,pr,pd])[0]
        if  Qt[(fi,te)][0] == "R" :
            n = n + 1
            z = z + 2
            Qt[(fi,te)][4] = 2
        if Qt[(fi,te)][0] == "D" :
            r = r + 1 
            Qt[(fi,te)][4] = 3
    elif loc(fi,te) == "R":
        if z == 0 :
            Qt[(fi,te)][0] = "S"
            Qt[(fi,te)][4]= 0 
        elif z != 0 :
            z = z-1
    elif loc(fi,te) == "D":
        if r == 0 and ((8 - cord(fi,te) - cor(fi,te)[0]) >= 3): 
            Qt[(fi,te)][0]="S"
            Qt[(fi,te)][4]= 0
        elif r != 0 :
            r = r -1 
    Qt[(fi,te)][1] = n
    Qt[(fi,te)][2] = r 
    Qt[(fi,te)][3] = z
# تشخیصص حالت بعدی فرد متناسب با بقیه 
while True :   
    x = int(input("""
                        1- showing systen in T
                        2- Showing the time of disease eradication or extinction
                        3- show plot at T
                        4- exit
                        enter a number  : """))
    if x == 1 :
        day = 0
        while True :
            print("--------------------------------------------- ") 
            T = int(input("enter T (-1 = exit): "))
            day = day + T
            if T == -1 :
                print("--------------------------------------------- ") 
                break
            for i in range(T) :
                for i in range(1,11) :
                    for j in range(1,11):
                        ran(i,j)
                Q = copy.deepcopy(Qt)
            for i in range(1,11) :
                for j in range(1,11):
                    print(Q[(i,j)][0],end="")
                print("")
            print(f"day {day}")
    if x == 2 :
        print("--------------------------------------------- ")
        Navrage = 0
        N = int(input("enter Number of times tested :"))
        for _ in range(N) :
            T = 0
            Q = copy.deepcopy(Qf)
            while True : 
                count = 0
                for i in range(1,11) :
                    for j in range(1,11):
                        ran(i,j)
                        if loc(i,j) == "I" :
                            count = count + 1
                Q = copy.deepcopy(Qt)
                if count != 0 :
                    T = T + 1
                if count == 0 :
                    break
            Navrage = Navrage + T
            print(f"disease eradicated at day {T}")
        print("--------------------------------------------- ")
        print(f"The disease is usually eradicated within {Navrage/N} days.")
        print("--------------------------------------------- ") 
    if x == 3 :
        while True :
            day = 0
            print("--------------------------------------------- ") 
            T = int(input("enter T (enter -1 to exit ): "))
            if T == -1 :
                print("--------------------------------------------- ")
                break 
            day = day + T
            for i in range(T) :
                for i in range(1,11) :
                    for j in range(1,11):
                        ran(i,j)
                Q = copy.deepcopy(Qt)
            color = pltc.ListedColormap(["green","red","blue","black"])
            Qplot = [[0]*10 for _ in range(1,11)]
            for i in range(1,11) :
                for j in range(1,11):
                    Qplot[j-1][i-1] = Q[(i,j)][4]
            plt.figure(figsize=(10,10))
            plt.pcolormesh(Qplot, cmap=color, edgecolor='black', linewidth=1)
            plt.gca().set_aspect('equal')
            plt.show()
    if x == 4 : 
        print("so long")
        break