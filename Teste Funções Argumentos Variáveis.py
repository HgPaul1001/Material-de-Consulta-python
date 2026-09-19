def calculo_media(*valores):
	soma = sum(valores)
	quantidade = len(valores)
	media = soma/quantidade
	return media
print(f"A média dos valores é: {calculo_media(20, 14, 49, 37, 1)}")