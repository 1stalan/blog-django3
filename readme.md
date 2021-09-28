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

Configurando Nginx
Criar arquivo uwsgi_params no path do projeto

vim uwsgi_params

---- file content -----

uwsgi_param  QUERY_STRING       $query_string;
uwsgi_param  REQUEST_METHOD     $request_method;
uwsgi_param  CONTENT_TYPE       $content_type;
uwsgi_param  CONTENT_LENGTH     $content_length;

uwsgi_param  REQUEST_URI        $request_uri;
uwsgi_param  PATH_INFO          $document_uri;
uwsgi_param  DOCUMENT_ROOT      $document_root;
uwsgi_param  SERVER_PROTOCOL    $server_protocol;
uwsgi_param  REQUEST_SCHEME     $scheme;
uwsgi_param  HTTPS              $https if_not_empty;

uwsgi_param  REMOTE_ADDR        $remote_addr;
uwsgi_param  REMOTE_PORT        $remote_port;
uwsgi_param  SERVER_PORT        $server_port;
uwsgi_param  SERVER_NAME        $server_name;

Criar arquivo de configuração NGINX em /etc/nginx/sites-available

upstream django {
    server unix:///home/nd_alans/coursedjango3/blog/mysite.sock; 
}

server {
    listen      80;
    server_name example.com;
    charset     utf-8;

    client_max_body_size 75M; 

    location /media  {
        alias /home/nd_alans/coursedjango3/blog/media; 
    }

    location /static {
        alias /home/nd_alans/coursedjango3/blog/static;
    }

    location / {
        uwsgi_pass  django;
        include     /home/nd_alans/coursedjango3/blog/uwsgi_params; 
    }
}

Criar link simbólico em sites-enabled sudo ln -s /etc/nginx/sites-available/django


Criando .ini file

[uwsgi]
chdir           = /home/nd_alans/coursedjango3/blog/
module          = django_vps.wsgi
home            = /home/nd_alans/venv
master          = true
processes       = 10
socket          = /home/nd_alans/coursedjango3/blog/mysite.sock
vacuum          = true
chmod-socket    = 666

Configurando uWSGI modo Emperor 

sudo mkdir /etc/uwsgi
sudo mkdir /etc/uwsgi/vassals
sudo ln -s /home/nd_alans/coursedjango3/blog/curso_django.ini /etc/uwsgi/vassals/


Configurando systemctl to start on boot

cd /etc/systemd/system/

sudo vim djangovps.service

[Service]
ExecStart=/home/nd_alans/venv/bin/uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data
RuntimeDirectory=uwsgi
Restart=always
KillSignal=SIGQUIT
Type=notify
StandardError=syslog
NotifyAccess=all
User=nd_alans

[Install]
WantedBy=multi-user.target

Mudando as permissões do arquivo 

======

sudo chmod 664 /etc/systemd/system/djangovps.service

sudo systemctl daemon-reload

sudo systemctl enable djangovps.service

sudo systemctl start djangovps.service

sudo systemctl status djangovps.service

journalctl -u djangovps.service