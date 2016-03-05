#Ansible workshop in ShuttleCloud

Ansible version 2.0.1.0

Twitter hashtag: #WorkshopsWeLove

https://www.eventbrite.com/e/ansible-workshop-tickets-21733881625?utm_source=eb_email&utm_medium=email&utm_campaign=reminder_attendees_48hour_email&utm_term=eventname

This one-day workshop is targeted to developers, sysadmins and devops that want to get a practical knowledge of Ansible and feel confident with it. We will go through most of the knowledge required to understand why Ansible is an easy-to-use configuration management and orchestration tool, you'll learn how to use it and see its practical applications in production environments.

The workshop is very hands on, all the examples and material will be available in github.

**Links**
http://docs.ansible.com/ansible/intro_getting_started.html

**Summary:**
* Introduction
* Inventory
* Modules, tasks, plays, playbooks
* Roles
* Ansible for delivery
* Ansible and cloud services
* Dynamic inventory.
* Callbacks for adding new behaviors when responding to events.
* Patterns to work with secrets (git-crypt vs. ansiblevault)

Requirements:
* https://github.com/penguinjournals/ansible-101-control-machine


##Tutores##
* David  is currently working on Ticketbis, but he’s been through media companies, engineering and custom development. These days he's focused on our product delivery. 
He loves eating, cooking and, above all, being on the couch with his wife and daughter.
* Maykel is Systems Engineer at ShuttleCloud. Made in Cuba. He'll play drums someday.
* Nestor is a passionate and upbeat software engineer, interested in open source and well crafted software. Stone at @codingstones and Senpai athttp://senpaidevs.com 


##Introduction
Ticketbis: they use Ansible only for deployments.
* Agentless
* Push based
* Python + SSH

* Ansible works by connecting to your nodes and pushing out small programs, called "Ansible Modules" to them.
* When speaking with remote machines, Ansible by default assumes you are using SSH keys. SSH keys are encouraged but password authentication can also be used where needed by supplying the option --ask-pass.

##Task1
* Edit (or create) /etc/ansible/hosts and put one or more remote systems in it. Your public SSH key should be located in authorized_keys on those systems:
* **ansible.cfg**: este fichero se lee en diferente orden de prioridad, según donde se encuentre. Environment variable, folder, /etc/ansible
  * **hostfile**: listado de las máquinas a gestionar.
  * **remote_user**: the user with which you will connect to the machines (you can change it through CLI)
  * **host_key_checking: False**: para saltarte el chequeo de SSH.

* Estructura general: `ansible <destination> <command>`
`$ ansible all -m ping -vvvv`
-m	módulo de Python (ping en este caso)

* **Show date:**
`$ ansible all -a "date"`

* **Show files under /root (http://docs.ansible.com/ansible/intro_getting_started.html):**
`$ ansible all -a "ls -la /root" --sudo` >> sudo is deprecated, use **--become-user**
`$ ansible all -a "ls -la /root" --become`
`$ ansible all -a "ls -la /root" -b`

`ansible all -a "/bin/echo hello"`

##Task2
###Inventory
http://docs.ansible.com/ansible/intro_inventory.html
Es mejor sacar las variables a otro sitio, no mezclarlo todo en el inventario.
The things in brackets are group names.
* **group_vars**: ficheros de variables de los grupos. El fichero bajo /group_vars/ tendrá el nombre de un grupo (u all), y las variables definidas dentro se asignan a él.
* **host_vars**: fichero de variables de los hosts. El fichero bajo /host_vars/ tendrá el nombre de un host, y las variables definidas dentro se asignan a él.

`
[webservers]
foo.example.com
bar.example.com
`

Host variables:
`
[atlanta]
host1 http_port=80 maxRequestsPerChild=808
host2 http_port=303 maxRequestsPerChild=909
`