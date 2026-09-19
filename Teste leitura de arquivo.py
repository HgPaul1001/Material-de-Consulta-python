arquivo = open("texto_leitura.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# com a declaração with
with open("texto_leitura.txt", "r") as arquivo:
		texto = arquivo.read()
		print(texto)