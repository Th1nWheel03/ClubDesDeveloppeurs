valide = 0

with open("donnees.txt", 'r', encoding='utf-8') as file:
    for line in file:

        line = line.strip().split('=>')
        code = line[0].strip().split(': ')
        isbn = code[1]
        tab = list(map(str, isbn))
        multiple = 0
        total = 0
        tab_isbn = []

        for i in tab:
            if i == 'X':
                tab.remove(i)
                i = '10'
                tab.append(i)
                tab_isbn.append(int(i))
            else:
                tab_isbn.append(int(i))

        for f in tab_isbn:
            multiple+=1
            f*=multiple
            total+=f
            
        divisible_par_11 = total%11
            

        if divisible_par_11 == 0:
            valide+=1

print(f"Nombre de code ISBN valides est : {valide}")