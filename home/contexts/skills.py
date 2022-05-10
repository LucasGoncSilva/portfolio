class Skill:
    def __init__(self, name: str, title: str) -> None:
        self.name = name
        self.title = title
        self.description = None
        self.doc = None

    def get_name(self) -> str:
        return self.name

    def get_title(self) -> str:
        return self.title

    def get_description(self) -> str:
        return self.description

    def get_doc(self) -> str:
        return self.doc


html = Skill('html', 'HyperText Markup Language')
html.description = 'Linguagem responsável pela estrutura da página, utiliza tags para limitar cada elemento da estrutura, bem como qual informação é um parágrafo, um título, uma tabela ou ainda qual informação as SEO possuem acesso.'
html.doc = 'https://www.w3.org/html/'


css = Skill('css', 'Cascading Style Sheets')
css.description = 'Linguagem responsável pela parte visual da página, utiliza "folhas em cascata" para determinar o estilo de cada elemento, desde o tamanho de cada item até o tempo de duração de animações. Basicamente, sua função é deixar a página visualmente agradável, conforme o estilo e a mensagem que deseja-se passar.'
css.doc = 'https://www.w3.org/Style/CSS/Overview.en.html'


sass = Skill('sass', 'Syntactically Awesome Style Sheets')
sass.description = '"CSS com superpoderes" é o slogan do SASS, e não é por acaso. Este pré-processador, também chamado como superset do CSS, processa/compila código de estilização baseado no Cascading Style Sheets no próprio, de maneira que navegadores consigam entendem. Variáveis, condicionais, loops, estes são os superpoderes que SASS entrega ao CSS'
sass.doc = 'https://sass-lang.com/'


js = Skill('js', 'JavaScript')
js.description = 'Se em uma página (comparando a um edifício) o HTML corresponde ao fundamento e a estrutura, e o CSS corresponde ao acabamento e estética, o JS - JavaScript - se refere a tudo que as pessoas podem interagir neste edifício, como acender e apagar lâmpadas.'
js.doc = 'https://www.javascript.com/'


bootstrap = Skill('bootstrap', 'Bootstrap')
bootstrap.description = 'Um dos frameworks web de código aberto para front-end, atuando com HTML, CSS e JS, surge como solução para construção ágil e facilitada de layouts responsivos (adaptáveis) para a web. Largamente utilizado por diversas gigantes do mercado, esta ferramenta pode até não te apresentar o ouro, mas pode certamente facilitar o caminho até ele.'
bootstrap.doc = 'https://getbootstrap.com/'


py = Skill('py', 'Python')
py.description = 'Uma linguagem multiproposital e multiparadigma, Python é uma linguagem crescente no mercado por sua facilidade no aprendizado e aplicação, além de ser aplicável em quase todos os lugares.'
py.doc = 'https://www.python.org/'


django = Skill('django', 'Django')
django.description = 'No top 2 frameworks web da linguagem Python, o Django apresenta a arquitetura MVC (Model-View-Controller) para a construção de ferramentas, soluções e sistemas, com robustez e segurança. Gigantes como Instagram, Spotify e Youtube foram construídas utilizando esta rocha, chamada Django'
django.doc = 'https://www.djangoproject.com/'


sqlite = Skill('sqlite', 'SQLite')
sqlite.description = 'Um gerenciador de bancos de dados simples, de fácil utilização que trabalha localmente, o SQLite é indicado para projetos que exijam médio-baixo tráfego de informações. Tal abordagem o torna amplamente utilizando em aplicações android, web com baixo tráfego de informações, e ainda, programas executáveis (.exe).'
sqlite.doc = 'https://www.sqlite.org/index.html'


ink = Skill('ink', 'Inkscape')
ink.description = 'Um software livre para criação de desenhos vetoriais, o Inkscape trabalha com o formato de arquivos ".svg", formato nativo da web. Nele é possível criar e editar ícones e logos, implementando-os como elementos adicionais ou de destaque nas páginas.'
ink.doc = 'https://inkscape.org/'


skill_cards = [html, css, sass, js, bootstrap, py, django, sqlite, ink]