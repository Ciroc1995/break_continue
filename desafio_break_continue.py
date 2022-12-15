# Solução 1
estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']
for estilo in estilos:
    if estilo == 'Rap':
        continue
    print(estilo)

# Solução 2
estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']
for estilo in estilos:
    if estilo == 'Rock':
        break
    print(estilo)

