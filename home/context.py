class Skill:
    def __init__(self, name: str, title: str, url: str, description: str) -> None:
        self.name = name
        self.title = title
        self.url = url
        self.description = description


html: Skill = Skill('html', 'HTML', 'https://www.w3.org/html/', 'Linguagem responsável pela estrutura da página, utiliza tags para limitar cada elemento da estrutura, bem como qual informação é um parágrafo, um título, uma tabela ou ainda qual informação as SEO possuem acesso.')
css: Skill = Skill('css', 'CSS', 'https://www.w3.org/Style/CSS/Overview.en.html', 'Linguagem responsável pela parte visual da página, utiliza "folhas em cascata" para determinar o estilo de cada elemento, desde o tamanho de cada item até o tempo de duração de animações. Basicamente, sua função é deixar a página visualmente agradável, conforme o estilo e a mensagem que deseja-se passar.')
sass: Skill = Skill('sass', 'Saas', 'https://sass-lang.com/', '"CSS com superpoderes" é o slogan do SASS, e não é por acaso. Este pré-processador, também chamado como superset do CSS, processa/compila código de estilização baseado no Cascading Style Sheets no próprio, de maneira que navegadores consigam entendem. Variáveis, condicionais, loops, estes são os superpoderes que SASS entrega ao CSS')
js: Skill = Skill('js', 'JavaScript', 'https://www.javascript.com/', 'Se em uma página (comparando a um edifício) o HTML corresponde ao fundamento e a estrutura, e o CSS corresponde ao acabamento e estética, o JS - JavaScript - se refere a tudo que as pessoas podem interagir neste edifício, como acender e apagar lâmpadas.')
bootstrap: Skill = Skill('bootstrap', 'Bootstrap', 'https://getbootstrap.com/', 'Um dos frameworks web de código aberto para front-end, atuando com HTML, CSS e JS, surge como solução para construção ágil e facilitada de layouts responsivos (adaptáveis) para a web. Largamente utilizado por diversas gigantes do mercado, esta ferramenta pode até não te apresentar o ouro, mas pode certamente facilitar o caminho até ele.')
py: Skill = Skill('py', 'Python', 'https://www.python.org/', 'Uma linguagem multiproposital e multiparadigma, Python é uma linguagem crescente no mercado por sua facilidade no aprendizado e aplicação, além de ser aplicável em quase todos os lugares.')
django: Skill = Skill('django', 'Django', 'https://www.djangoproject.com/', 'No top 2 frameworks web da linguagem Python, o Django apresenta a arquitetura MVC (Model-View-Controller) para a construção de ferramentas, soluções e sistemas, com robustez e segurança. Gigantes como Instagram, Spotify e Youtube foram construídas utilizando esta rocha, chamada Django')
sqlite: Skill = Skill('sqlite', 'SQLite', 'https://www.sqlite.org/index.html', 'Um gerenciador de bancos de dados simples, de fácil utilização que trabalha localmente, o SQLite é indicado para projetos que exijam médio-baixo tráfego de informações. Tal abordagem o torna amplamente utilizando em aplicações android, web com baixo tráfego de informações, e ainda, programas executáveis (.exe).')
ink: Skill = Skill('ink', 'Inkscape', 'https://inkscape.org/', 'Um software livre para criação de desenhos vetoriais, o Inkscape trabalha com o formato de arquivos ".svg", formato nativo da web. Nele é possível criar e editar ícones e logos, implementando-os como elementos adicionais ou de destaque nas páginas.')

skill_cards: list[Skill] = [html, css, sass, js, bootstrap, py, django, sqlite, ink]


class Project:
    def __init__(self, name: str, description: str, url: str) -> None:
        self.name = name
        self.description = description
        self.url = url


secret_guardian: Project = Project('SecretGuardian', 'Gerenciador de Senhas online com criptografia de banco em Django e Sass.', '#')
project_automation: Project = Project('Projeto Automação', 'Automação de testes de nível corporativo em browser e API com Selenium e Zeep.', '#')
app: Project = Project('Casarão', 'App institucional do Casarão em React Native e Tailwind CSS com Expo Go.', '#')

project_cards: list[Project] = [secret_guardian, project_automation, app]
