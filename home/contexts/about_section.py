from datetime import datetime


date = datetime.now()
month = date.month
year = date.year

if year == 2022 and month < 7: period = 'primeiro'
elif year == 2022 and month >= 7: period = 'segundo'
elif year == 2023 and month < 7: period = 'terceiro'
elif year == 2023 and month >= 7: period = 'quarto'
elif year == 2024 and month < 7: period = 'quinto'
elif year == 2024 and month >= 7: period = 'sexto'
elif year == 2025 and month < 7: period = 'sétimo'
elif year == 2025 and month >= 7: period = 'oitavo'

p1 = f'Com 18 anos de idade adentrei o universo da programação, em abril de 2021, sempre estudando de maneira consistente e sólida. Inicialmente como autodidata, utilizando recursos como Youtube, StackOverFlow e alguns cursos; atualmente estou cursando Ciência da Computação no {period} semestre.'
p2 = 'Busco sempre estar somando àquilo em que me envolvo, buscando, também, compreender minha posição e o porque de cada tarefa, a fim de realizá-las da melhor forma possível. Destaco, como pontos fortes, meu trabalho em equipe, dedicação e capacidade de liderar grupos e equipes.'
p3 = 'A título de curiosidade, devo dizer que tenhos planos de, a médio/longo prazo, entrar para a área de Pentesting e Web Hacking; talvez iniciando como um hobbie, mas tendo chances de utilizar esses conceitos profisionalmente. Uma reflexão: se eu hackear um sistema que eu mesmo criei, sou um bom hacker ou um desenvolvedor duvidoso?'

about_paragraphs = [p1, p2, p3]