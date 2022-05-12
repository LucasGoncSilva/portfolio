class Project:
    def __init__(self, name: str, title: str) -> None:
        self.name = name
        self.title = title
        self.description = None
        self.github = None
        self.project_link = None

    def get_name(self) -> str:
        return self.name

    def get_title(self) -> str:
        return self.title

    def get_description(self) -> str:
        return self.description

    def get_github(self) -> str:
        return f'https://github.com/LucasGoncSilva/{self.github}'

    def get_project_link(self) -> str:
        return self.project_link


lg = Project('lg', 'Lucas Gonc')
lg.description = 'Nada mais, nada menos que este próprio website - meu portfólio. Construído do zero e utilizando Django - um Framework Python com arquitetura MVC - como fundamento, este site apresenta parte daquilo que sou capaz de fazer.'
lg.github = 'lucasgonc'
lg.project_link = 'https://lucasgonc.herokuapp.com/'


task_list = Project('task_list', 'Gerenciador de Tarefas')
task_list.description = 'Uma lista pessoal de tarefas que armazena as informações no local storage, dispensando o uso de base de dados e possibilitando o acesso a cada item da lista sempre que necessário. Uma vez que não existe base de dados, não há como acessar uma mesma lista em diferentes aparelhos através de login.'
task_list.github = 'task_list'
task_list.project_link = 'https://personaltasklist.vercel.app/'


passgen = Project('pass_gen', 'Gerador de Senhas')
passgen.description = 'Desenvolvido em JavaScript e utilizando a framework Electron para a geração da interface gráfica, este gerador de senhas possibilita que o usuário escolha a quantidade de caracteres que deseja que a senha contenha, juntamente aos tipos de caracteres (minúsculas, maiúsculas, números e/ou símbolos.'
passgen.github = 'password_generator'
passgen.project_link = 'https://gerarsenhas.vercel.app/'


clock = Project('clock', 'Relógio Digital')
clock.description = 'Uma aplicação simples que informa o horário em tempo real com menos de um segundo de variação em relação ao horário oficial, o Digital Clock representa exatamente o que seu nome indica. Utiliza tecnologia web com Electron como framework para desktop app.'
clock.github = 'digital_clock'
clock.project_link = 'https://simpledigitalclock.vercel.app/'


encoder = Project('encoder', 'Encoder')
encoder.description = 'Encoder (codificador em inglês, no contexto de criptografia) é um programa, dispositivo ou equipamento capaz de criptografar informações utilizando uma chave escolhida pelo usuário. Somente será revelada a verdadeira mensagem utilizando exatamente a mesma chave utilizada para gerar o texto codificado, caso contrário, a mensagem revelada será diferente de modo a não haver ligação com a mensagem original, nem mesmo sendo revelada mensagem alguma.'
encoder.github = 'encoder'
encoder.project_link = 'https://codificador.vercel.app/'


cypher = Project('cypher', 'Cypher')
cypher.description = 'Baseado na "Cifra de César" com algumas modificações pessoais, este programa com interface gráfica possibilita a tradução ida e volta entre um texto/mensagem normal e cifrado. A matemática por trás da tradução é simples o suficiente para que seja possivel traduzir mensagens sem a necessidade de um programa, utilizando apenas a própria mente. Com base nisso, o Cypher foi desenvolvido para facilitar e acelerar a transcrição de textos longos para troca de informações.'
cypher.github = 'cypher'
cypher.project_link = 'https://textcypher.vercel.app'


project_cards = [lg, task_list, passgen, clock, encoder, cypher]