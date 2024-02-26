def degrees_to_time(degrees):
    hours = int(degrees / 30) % 12
    minutes = int((degrees % 30) * 2)
    return '{:02d}:{:02d}'.format(hours if hours != 0 else 12, minutes)

print(f"Pour un angle de 333.25, l'heure est : {degrees_to_time(333.25)} au format 12h HH:MM")