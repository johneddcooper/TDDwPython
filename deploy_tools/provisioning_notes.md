Provisinoing a new site
======================

## Required packages:

* nginx
* Python 3.7
* pipenv
* Git

eg, on Ubuntu:    

	sudo add-apt-repository ppa:deadsnakes/ppa    
	sudo apt update    
	sudo apt install nginx git python3.7
	pip3 install pipenv

## Nginx Virtual Host Config

* see nginx.template.conf
* replace DOMAIN with, eg., staging.my-domain.com

## Systemd Service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com

## Folder structure:

Assume we have a user account at /home/username

/home/username
└── sites
    ├── DOMAIN1
    │    ├── .env
    │    ├── db.sqlite3    
    │    ├── manage.py etc    
    │    ├── static    
    │    ├── Pipfile    
    │    └── Pipfile.lock  
    └── DOMAIN2         
         ├── .env         
         ├── db.sqlite3         
         ├── etc
