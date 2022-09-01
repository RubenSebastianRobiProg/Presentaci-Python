usuarios={"Pedro":1234}
print ("Bienvenid@s al sistema de entradas. Recuerda que el máximo de miembros permitidos son  4.")
while len(usuarios) != 4:
    print ("Introduce si eres 'Nuevo usuario' o 'Acceder'.") 
    inici = input ("Qué quieres hacer: ")
    if inici == "Nuevo usuario":
        nombre = input ( "Nombre: ")
        contraseña = input ("Contraseña: ")
        usuarios [nombre] = contraseña
        print ("Ya se han registrado " ,len (usuarios), "usuarios.")
        print (usuarios.keys())
    elif inici == "Acceder":
        nombreacc = input ( "Nombre: ")
        contraseñaacc = input ("Contraseña: ")
        print (usuarios.get (nombreacc))
        if usuarios.get (nombreacc) == contraseñaacc:
            print ("Puedes acceder al sistema")
        else:
            print ("Acceso denegado.")
        
        
        

    
