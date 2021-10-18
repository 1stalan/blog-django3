
Link do projeto: [Python Garden](https://www.pythongarden.com.br/)

Criar Ambiente virtual

`python -m venv venv`

Ativar Ambiente virtual

`.\venv\Scripts\activate`

Instalando o django

`python -m pip install Django`

**Utilitario django-admin** 

Criar projeto

django-admin startproject "nome do projeto"

Iniciando o servidor de desenvolvimento

`python manage.py runserver`

`urls.py`

definição das urls em django, que atraves de uma expressão regular vai determinar uma função python que vai ser executada apos a url ser acessada

Criando tabelas no banco de dados

`python manage.py migrate`

Criando usuario de administração

`python manage.py createsuperuser`

Criando uma aplicação

`python manage.py startapp "nome da aplicação"`

