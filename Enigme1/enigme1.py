import numpy

nomber_species = 0

with open("donnees.txt", 'r') as file:
    for line in file:
        fish = line.strip().lower() 
        chain = ""

        for letter in fish:
            if 'a' <= letter <= 'f':
                chain += letter
        
        if chain: 
            adn = 0
            for char in chain:
                adn ^= int(char, 16)
        
        if adn == 15:
            nomber_species += 1

print(f"Nombre d'espèces ayant un ADN numérique de 15 : {nomber_species}")