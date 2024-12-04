class Project:
    def __init__(self, name: str, description: str, url: str) -> None:
        self.name = name
        self.description = description
        self.url = url


swarden: Project = Project(
    'sWarden',
    'Online password manager with database encryption in Django and Sass.',
    'https://github.com/LucasGoncSilva/swarden/',
)
project_automation: Project = Project(
    'Projeto Automação',
    'Automation of enterprise-level browser and API tests with Selenium and Zeep.',
    'https://github.com/LucasGoncSilva/projeto_automacao/',
)
vmap: Project = Project(
    'VMAP',
    'Tool for controlling and mapping deployments in real scenarios with Django. \
        Collab.',
    'https://github.com/LucasGoncSilva/vmap/',
)
bookery: Project = Project(
    'Bookery',
    'Desktop management system and book API for libraries with Axum and Tauri.',
    'https://github.com/LucasGoncSilva/bookery/',
)
mosheh: Project = Project(
    'Mosheh',
    'Mosheh, a tool for creating docs for projects, from Python to Python.',
    'https://github.com/LucasGoncSilva/mosheh/',
)
soon: Project = Project(
    'Soon',
    'Project in the theoretical planning phase, evaluating opportunities. \
        More information soon.',
    '#',
)

project_cards: list[Project] = [swarden, project_automation, bookery, vmap, mosheh]

project_cards += [soon] * (6 - len(project_cards))


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
    'Language responsible for the structure of the page, it uses tags to limit each \
        element of the structure, as well as which information is a paragraph, \
            a title, a table or even which information the SEO has access to.',
)
css: Skill = Skill(
    'css',
    'CSS',
    'https://www.w3.org/Style/CSS/Overview.en.html',
    'It uses “cascading sheets” to determine the style of each element, from the \
        size of each item to the duration of animations. Basically, its function \
            is to make the page visually pleasing, according to the style and message \
                you want to convey.',
)
sass: Skill = Skill(
    'sass',
    'Saas',
    'https://sass-lang.com/',
    '"CSS with superpowers" is the slogan of SASS, and it\'s no coincidence. This \
        preprocessor, also called a CSS superset, processes/compiles styling code \
            based on Cascading Style Sheets into itself, in a way that browsers can \
                understand. Variables, conditionals, loops, these are the superpowers \
                    that SASS gives CSS',
)
js: Skill = Skill(
    'js',
    'JavaScript',
    'https://www.javascript.com/',
    'If on a page (comparing it to a building) HTML corresponds to the foundation and \
        structure, and CSS corresponds to the finish and aesthetics, JS - JavaScript - \
            refers to everything that people can interact with in this building, such \
                as turning light bulbs on and off.',
)
bootstrap: Skill = Skill(
    'bootstrap',
    'Bootstrap',
    'https://getbootstrap.com/',
    'One of the open source web frameworks for the front-end, working with HTML, CSS \
        and JS, it has emerged as a solution for the agile and easy construction of \
            responsive (adaptable) layouts for the web. Widely used by several giants \
                in the market, this tool may not present you with gold, but it can \
                    certainly make the path to it easier.',
)
py: Skill = Skill(
    'py',
    'Python',
    'https://www.python.org/',
    'A multi-purpose and multi-paradigm language, Python is a growing language on \
        the market due to its ease of learning and application, as well as being \
            applicable almost everywhere.',
)
django: Skill = Skill(
    'django',
    'Django',
    'https://www.djangoproject.com/',
    'Among the top web frameworks in the Python language, Django presents the MVC \
        (Model-View-Controller) architecture for building tools, solutions and systems \
            with robustness and security. Giants such as Instagram, Spotify and \
                Youtube were built using this rock, called Django.',
)
postgres: Skill = Skill(
    'postgres',
    'PostgreSQL',
    'https://www.postgresql.org/',
    "The World's Most Advanced Database, Postgres, is an open source relational and \
        object-relational database management system. It is widely used for its \
            robustness, extensibility and compliance with SQL standards. Its \
                distinguishing features include advanced support for ACID \
                    transactions, customized extensions and an active development \
                        community.",
)
rust: Skill = Skill(
    'rust',
    'Rust',
    'https://www.rust-lang.org/pt-BR/',
    'Rust is a modern programming language focused on security, performance and \
        concurrency. Designed to avoid segmentation faults and race conditions, \
            it combines the efficiency of C++ with memory safety guarantees. Rust \
                  is popular for its expressive syntax, advanced type system and \
                    the ability to manage memory without a garbage collector.',
)

skill_cards: list[Skill] = [html, css, sass, js, bootstrap, py, django, rust, postgres]
