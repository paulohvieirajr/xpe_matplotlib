import matplotlib.pyplot as plt

# Dados ficticios de preços de ações ao longo de 5 dias
setores = ['Tecnologia', 'Saúde', 'Financeiro', 'Indústria']
ano_2019 = [15, 25, 10, 20]
ano_2020 = [20, 20, 15, 25]
ano_2021 = [25, 15, 20, 15]

plt.figure(figsize=(10, 6))

plt.bar(setores, ano_2019, label='2019')
plt.bar(setores, ano_2020, label='2020', bottom=ano_2019)
plt.bar(setores, ano_2021, label='2021', bottom=[a + b for a, b in zip(ano_2019, ano_2020)])

plt.xlabel('Setores')
plt.ylabel('Contribuição para o Total (%)')
plt.title('Comparação de Setores para a Carteira de INvestimentos')
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.show()

