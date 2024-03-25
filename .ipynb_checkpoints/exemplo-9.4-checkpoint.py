import matplotlib.pyplot as plt

# Composição da carteira de investimentos (%)
setores = ['Tecnologia', 'Saúde', 'Financeiro', 'Indústria']
composicao = [30.36, 25, 20, 25]

# Plotar o gráfico de pizza
plt.pie(composicao, labels=setores, autopct='%1.1f%%', startangle=90)
# autopct='%1.1f%%'  >>  Formato de string que define como as % devem ser formatadas e exibidas no gráfico.
# Neste caso, "%1.1f%%" significa que as porcentagens serão exibidas com uma casa decimal.
# startangle=90  >> Define o ângulo inicial do gráfico de pizza. Neste caso, coloca 'Tecnologia' no topo do gráfico.
plt.axis('equal')   # Define a proporção de aspecto do gráfico como igual, desenha em forma de círculo, em vez de uma elipse.
# Outras opções 'auto' , 'off' , 'scaled' , 'tight'
plt.title('Composição da Carteira de Investimentos')  # Título do Gráfico
plt.show()  # Exibe o Gráfico
