# pyblogger


pyblogger/
├── pyblogger/
│   ├── __init__.py
│   ├── site_generator.py
│   ├── parser.py
│   ├── template_engine.py
│   └── utils.py
├── examples/
│   └── meu_blog/
│       ├── content/
│       ├── templates/
│       └── static/
├── setup.py
└── README.md
#  O que essa lib faz 

✅ Leitura dos arquivos .md com front matter
Usar PyYAML + Markdown.

✅ Motor de template
Usar Jinja2 pra renderizar páginas com base em templates.

✅ Geração dos arquivos HTML na pasta output/
✅ Index de posts (como uma home ou listagem)
✅ Copiar arquivos estáticos (CSS, imagens)
