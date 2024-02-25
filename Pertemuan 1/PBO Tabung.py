print("menghitung luas dan volume tabung/silender")

#variable
r=int(input("masukan jari jari=" ))
t=int(input("masukan tinggi  =" ))

#rumus
phi= 22/7
volume = phi*r*r*t
luasp= 2*phi*r*(r+t)
luass=2*phi*r*t

#output
print("luas permukaan tabung adalah=",luasp)
print("luas selimut tabung adalah=",luass)
print("volume tabung adalah=",volume)