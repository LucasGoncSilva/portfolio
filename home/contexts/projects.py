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


lg = Project('portfolio', 'Lucas Gonc')
lg.description = 'Nada mais, nada menos que este próprio website - meu portfólio. Construído do zero e utilizando Django - um Framework Python com arquitetura MVC - como fundamento, este site apresenta parte daquilo que sou capaz de fazer.'
lg.github = 'portfolio'
lg.project_link = 'https://lucasgonc.herokuapp.com'


lipsum = Project('lipsum', 'Lipsum')
lipsum.description = 'Gerenciador de senhas online, simples e intuitivo, capaz de armazenar diversos serviços, usuários e senhas, sempre utilizando criptografia. Desta forma, nem mesmo administradores do sistema são capazes de decifrar o que clientes inserem.'
lipsum.github = 'lipsum'
lipsum.project_link = 'https://lipsum.herokuapp.com'


task_list = Project('task_list', 'Gerenciador de Tarefas')
task_list.description = 'Uma lista pessoal de tarefas que armazena as informações no local storage, dispensando o uso de base de dados e possibilitando o acesso a cada item da lista sempre que necessário. Uma vez que não existe base de dados, não há como acessar uma mesma lista em diferentes aparelhos através de login.'
task_list.github = 'task_list'
task_list.project_link = 'https://personaltasklist.vercel.app'


project_cards = [lg, lipsum, task_list]