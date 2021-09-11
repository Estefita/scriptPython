
words = "hola que tal"
lista = list() 
lista_repetidos = list()
for i, word in enumerate(words):    
    
    if word not in lista and " " not in word:
         lista_repetidos.append(f"{word}  --> {words.count(word)}")
    lista.append(word)         
for leter in lista_repetidos:
    print(leter)