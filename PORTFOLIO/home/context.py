class Skill:
    def __init__(self, name: str, title: str, url: str, description: str) -> None:
        self.name = name
        self.title = title
        self.url = url
        self.description = description


html: Skill = Skill(
    'html',
    'HTML',
    'https://www.w3.org/html/',
    'Linguagem responsável pela estrutura da página, utiliza tags para limitar cada \
        elemento da estrutura, bem como qual informação é um parágrafo, um título, \
            uma tabela ou ainda qual informação as SEO possuem acesso.',
)
css: Skill = Skill(
    'css',
    'CSS',
    'https://www.w3.org/Style/CSS/Overview.en.html',
    'Linguagem responsável pela parte visual da página, utiliza "folhas em cascata" \
        para determinar o estilo de cada elemento, desde o tamanho de cada item até o \
            tempo de duração de animações. Basicamente, sua função é deixar a página \
                visualmente agradável, conforme o estilo e a mensagem que deseja-se passar.',
)
sass: Skill = Skill(
    'sass',
    'Saas',
    'https://sass-lang.com/',
    '"CSS com superpoderes" é o slogan do SASS, e não é por acaso. Este pré-processador, \
        também chamado como superset do CSS, processa/compila código de estilização baseado \
            no Cascading Style Sheets no próprio, de maneira que navegadores consigam entendem. \
                Variáveis, condicionais, loops, estes são os superpoderes que SASS entrega ao CSS',
)
js: Skill = Skill(
    'js',
    'JavaScript',
    'https://www.javascript.com/',
    'Se em uma página (comparando a um edifício) o HTML corresponde ao fundamento e a \
        estrutura, e o CSS corresponde ao acabamento e estética, o JS - JavaScript - se \
            refere a tudo que as pessoas podem interagir neste edifício, como acender e \
                apagar lâmpadas.',
)
bootstrap: Skill = Skill(
    'bootstrap',
    'Bootstrap',
    'https://getbootstrap.com/',
    'Um dos frameworks web de código aberto para front-end, atuando com HTML, CSS e \
        JS, surge como solução para construção ágil e facilitada de layouts responsivos \
            (adaptáveis) para a web. Largamente utilizado por diversas gigantes do mercado, \
                esta ferramenta pode até não te apresentar o ouro, mas pode certamente \
                    facilitar o caminho até ele.',
)
py: Skill = Skill(
    'py',
    'Python',
    'https://www.python.org/',
    'Uma linguagem multiproposital e multiparadigma, Python é uma linguagem crescente \
        no mercado por sua facilidade no aprendizado e aplicação, além de ser aplicável \
            em quase todos os lugares.',
)
django: Skill = Skill(
    'django',
    'Django',
    'https://www.djangoproject.com/',
    'No top 2 frameworks web da linguagem Python, o Django apresenta a arquitetura MVC \
        (Model-View-Controller) para a construção de ferramentas, soluções e sistemas, \
            com robustez e segurança. Gigantes como Instagram, Spotify e Youtube foram \
                construídas utilizando esta rocha, chamada Django',
)
postgres: Skill = Skill(
    'postgres',
    'PostgreSQL',
    'https://www.postgresql.org/',
    'O Mais Avançado Banco de Dados do Mundo, o Postgres, é um sistema de gerenciamento \
        de banco de dados relacional e objeto-relacional de código aberto. Ele é amplamente \
            utilizado por sua robustez, extensibilidade e conformidade com os padrões SQL. \
                Seus diferenciais incluem suporte avançado a transações ACID, extensões \
                    personalizadas e uma comunidade ativa de desenvolvimento.',
)
rust: Skill = Skill(
    'rust',
    'Rust',
    'https://www.rust-lang.org/pt-BR/',
    'Rust é uma linguagem de programação moderna, focada em segurança, desempenho e \
        concorrência. Projetada para evitar falhas de segmentação e condições de corrida, \
            ela combina a eficiência do C++ com garantias de segurança de memória. Rust \
                é popular por sua sintaxe expressiva, sistema de tipos avançado e a capacidade \
                    de gerenciar memória sem um coletor de lixo.',
)

skill_cards: list[Skill] = [html, css, sass, js, bootstrap, py, django, rust, postgres]


class Project:
    def __init__(self, name: str, description: str, url: str) -> None:
        self.name = name
        self.description = description
        self.url = url


swarden: Project = Project(
    'sWarden',
    'Gerenciador de Senhas online com criptografia de banco em Django e Sass.',
    'https://github.com/LucasGoncSilva/swarden/',
)
project_automation: Project = Project(
    'Projeto Automação',
    'Automação de testes de nível corporativo em browser e API com Selenium e Zeep.',
    '#',
)
vmap: Project = Project(
    'VMAP',
    'Ferramenta de controle e mapeamento de deploy em cenários reais em Django.\nCollab',
    'https://github.com/LucasGoncSilva/vmap/',
)

project_cards: list[Project] = [swarden, project_automation, vmap]
