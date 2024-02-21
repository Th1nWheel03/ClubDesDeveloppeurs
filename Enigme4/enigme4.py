total_sauvegardes = 0
    
with open("donnees.txt", 'r') as file:
    for line in file:
            
        taille_files, capacite_disque = line.strip().split(';')
        taille_files = list(map(int, taille_files.split(',')))

        used = 0
        index = 0
        while index < len(taille_files) and used <= int(capacite_disque):
            used += taille_files[index]
            if used <= int(capacite_disque):
                total_sauvegardes += 1
            index += 1

print("Nombre total de sauvegardes possibles :", total_sauvegardes)