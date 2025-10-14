frutas= ["manzana", "banana", "cereza", "naranja"]
for fruta in frutas:
  print(fruta)
  
  for i in range(5):
    print(i)

for i in range(2, 6):
  print(i)

for i in range(2, 30, 3):
  print(i)

for h in range(1,5):
  print(f"<h1>SECCIONES {h}</h1>")

deportes= ["futbol", "basket", "tenis", "golf"]
for deporte in range(len(deportes)):
  print(deporte, deportes[deporte])

  prendas= ["pantalon", "camisa", "remera"]
for indice,prenda in enumerate (prendas):
  print(indice, prenda)

  for i,prenda in enumerate(prendas, start=1):
    print(i, prenda)

    names= ["Ana", "Luis", "Carlos"]
    edades= [28, 34, 29]
    for name, edad in zip(names, edades):
      print("name", name, "edad", edad)
      
sports= ["futbol", "basket", "tenis"]
horarios= ["10:00", "12:00",]
for sport, horario in zip(sports, horarios):
 print("sport", sport, "horario", horario)

 perfiles= {"nombre": "Ana", "edad": 28, "profesion": "instructor"}
for key, value in perfiles.items():
  print(key, value)