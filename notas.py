print("**********CALIFICACION DE TRABAJOS FINALES*******************")
print("********SOLO SE DEJARON 5 TRABAJOS**************")
List  = ["Marco Pisco", "Eduardo Gonzales", "Kevin Mendoza"]
print("********Alumno a evaluar********")
print(List[0])

contador = 0;
contador2 = 0;
nota = 2;

cantidad = int(input("Ingrese la cantidad de calificaciones que va a presentar: "))
while (cantidad > 5):
    print("ERRRO!!!!!!!!!!!!!!")
    print("SOLO SE DEJARON 5 TRABAJOS")
    cantidad = int(input("Ingrese la cantidad de calificaciones que va a presentar: "))
    
for i in range (1, cantidad + 1):
    nota = int(input(f"Ingrese la nota del trabajo {i}: "))
    while (nota > 20):
        
          print("ERROR!!!!!")
          print("VUELVA A INTRODUCIR LA NOTA")   
          nota = int(input(f"Ingrese la nota del trabajo {i}: "))   
                       
    if (nota > 10.5):
        print("Aprobado")
        contador = contador + 1
        
    else:
        print("Desaprobado")
        contador2 = contador2 + 1 
    
print(f"Ha aprobado en {contador} trabajos") 
print(f"Ha desaprobado en {contador2} trabajos")   
