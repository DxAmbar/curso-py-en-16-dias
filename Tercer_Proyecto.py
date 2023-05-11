frase_ingresada = input("Introduce una frase: ")
letras = []
letras.append(input("Introduce una letra: ").lower())
letras.append(input("Introduce una segunda letra: ").lower())
letras.append(input("Introduce una tercera letra: ").lower())
print("\n")
print(f"Tu frase es: '{frase_ingresada}'")

# cuántas veces aparece cada letra ingresada, lower case

frase = frase_ingresada.lower()

primera_letra = frase.count(letras[0])
segunda_letra = frase.count(letras[1])
tercera_letra = frase.count(letras[2])
print("\n")
print(f"""La letra '{letras[0]}' aparece {primera_letra} veces en tu frase.
La letra '{letras[1]}' aparece {segunda_letra} veces en tu frase.
La letra '{letras[2]}' aparece {tercera_letra} veces en tu frase.""")

# cuántas palabras hay en la frase

print("\n")
palabras = frase.split()
print(f"Hay {len(palabras)} palabras en tu frase.")


# informar primera y última letra

print("\n")
print("La primera letra de tu frase es " + frase[0] + " y la última es " + frase[-1])

# invertir el orden de la frase

fragmento = frase_ingresada[::-1]

print("\n")
print("Tu frase al revés se leería: " + fragmento)

# ver si "Python" está en la frase

python = "python" in frase
dic = {True:"Si.", False:"No."}

print("\n")
print(f"¿Está Python en tu frase? {dic[python]}")