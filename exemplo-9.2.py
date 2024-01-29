import matplotlib.pyplot as plt

# Dados ficticios de preços de ações ao longo de 5 dias
acoes = ['A', 'B']
precos_mes_anterior= [150, 130]
precos_mes_atual = [160, 140]

plt.bar(acoes, precos_mes_anterior, label='Mês Anterior', color='b', width=0.4)
plt.bar(acoes, precos_mes_atual, label='Mês Atual', color='g', width=0.4, bottom=precos_mes_anterior)
plt.xlabel('Ação')
plt.ylabel('Preço')
plt.title('Comparação de Preõs de Ações')
plt.legend()
plt.show()
