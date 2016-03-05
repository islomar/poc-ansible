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
* Es mejor sacar las variables a otro sitio, no mezclarlo todo en el inventario.
* The things in brackets are group names.
* It is also possible to make groups of groups using the :children suffix. 
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

* You've been noticed about the Heartbleed Bug and you need to update openssl package in all of them:
`ansible all -a "apt-get update" -b`
`ansible all -a "apt-get install --only-upgrade libssl1.0.0" -b`
`ansible all -m shell -a "apt-get update && apt-get install --only-upgrade libssl1.0.0" -b`
`ansible all -m apt -a 'update_cache=yes name=openssl state=latest' --become`

* Use of shell:
`ansible app-servers -m shell -a "echo $TERM"

* Module for managing user accounts: http://docs.ansible.com/ansible/user_module.html
* In order to create a user for a role:
1. Create a file <groupName>.yml under group_vars folder so that is used when running each host, 
2. Run the **user* module:    `ansible all -m user -a "name=frontenduser" -become`
3. Estamos definiendo el estado que esperamos, NO una orden de creación/borrado/whatever. En este caso, decimos que esperamos que exista el usuario 'frontenduser': si no existe, lo crea, y si existe... no hace nada.
4. Cuando se ejecuta la primera vez, devuelve "changed=true", indicando que en esa ejecución ha creado el usuario. Si se vuelve a ejecutar, devolverá "changed=false", indicando que el usuario ya existía y por tanto no ha tenido que ejecutar nada.


##Task3
* **Modules** are used to control system resources
  * http://docs.ansible.com/ansible/modules.html
  * Ansible ships with a number of modules (called the ‘module library’) that can be executed directly on remote hosts or through Playbooks.
* **Play**: conjunto de hosts contra un conjunto de acciones (it maps tasks to roles).
* **Playbook** fichero con varias plays. Descriptions of the desired state of your systems.
  * http://docs.ansible.com/ansible/playbooks_intro.html


* Tasks
  * Ver task3-first-step.yml
  * hosts
  * vars:	se pueden definir variables de ejecución para esta play. También se puede poner una referencia a un fichero de variables
  * name: nombre descriptivo, simplemente para saber en qué punto se está en cada momento.
  * become: para poder ser súperusuario. Podría ir en otro sitio, por ejemplo arriba del fichero, bajo hosts, si queremos usarlo para todos los plays del playbook.
  * módulo a ejecutar. Permite variable **with_items**

`ansible frontend1 -m shell -a "git --version"`		>> git does NOT exist
`ansible-playbook task3-first-step.yml`				>> git gets installed (changed=1)
`ansible-playbook task3-first-step.yml`				>> nothing happens (changed=0)


`ansible frontends -m command -a "ls -la /var/www/html"`

`gather_facts: no`: http://docs.ansible.com/ansible/playbooks_variables.html#turning-off-facts
 * Por defecto, hace un `ansible <hostname> -m setup`, que pilla toda la información de la máquina. Si pones gather_facts:no, ya no lo hace.
 * Se suele poner **no** para que vaya más rápido. Si no lo pones, hace el gather data en el [setup]

`ansible-playbook task3-first-step.yml -t "updateapp" -e "boniclo:patata"`

Passing variables on the command line:
http://docs.ansible.com/ansible/playbooks_variables.html#passing-variables-on-the-command-line


##Roles
https://github.com/nestorsalceda/taller-ansible
Objetivo: separar todo un playbook completo en diversos roles

wget http://172.16.42.78:8000/debian-jessi64.box

El "---" al principio del playbook no es obligatorio.



##Modules seen
* -m ping
* -m command -a "date"		>> Only accepts ONE command
* -m shell -a "command1 && command2"
* -m apt -a "xxx"
* -m user -a "user=<username>"


##DUDAS
* Paso de variable en CLI: -e "boniclo:patata": ¿¿--extra-vars "key=value"??
* Usar
