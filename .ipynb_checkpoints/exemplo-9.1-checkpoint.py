import matplotlib.pyplot as plt

# Dados ficticios de preços de ações ao longo de 5 dias
dias = [1, 2, 3, 4, 5]
precos = [100, 120, 115, 130, 125]


plt.plot(dias, precos, marker='o', linestyle='-', color='b')
plt.xlabel('Dia')
plt.ylabel('Preço')
plt.title('Evolução do Preço das Ações')
plt.grid(True)
plt.show()
