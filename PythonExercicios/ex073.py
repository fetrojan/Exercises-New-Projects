#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time do Juventude:

times = ('Corinthians', 'São Paulo', 'Santos', 'Palmeiras', 'Bragantino', 'América MG', 'Atlético MG', 'Athletico PR',
         'Internacional', 'Juventude', 'Fortaleza', 'Ceara', 'Botafogo', 'Flamengo', 'Fluminense', 'Avaí', 'Cuiaba',
         'Coritiba', 'Atletico GO', 'Goias')

print('#-'*40)
print(f'Classificação dos times: {times}')
print('#-'*40)
print(f'Os 5 primeiros times: {times[:5]}')
print('#-'*40)
print(f'Os quatro ultimos colocados: {times[16:]}')
print('#-'*40)
print(f'Times em ordem alfabética: {sorted(times)}')
print('#-'*40)
print(f'Posição do Juventude: {times.index("Juventude")+1}ª')


