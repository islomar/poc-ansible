# ansible-101-control-machine

## *nix (Mac, Linux...)

### Step 1.
Install [Virtualbox](https://www.virtualbox.org/wiki/Downloads)

We'll use it for creating and destroying virtual machines on your computer easily.

### Step 2.
Install [Vagrant](https://www.vagrantup.com/downloads.html)

The machines we'll use during the workshop will be created and managed using vagrant.

### Step 3.
Install [Ansible](http://docs.ansible.com/ansible/intro_installation.html) (pip install ansible should do the job)

### Verification.

- Clone/download the [workshop repository](https://github.com/penguinjournals/ansible-101)
- From inside task1 folder run `vagrant up` (you'll need internet in this step)
- When the machine has started up run `ansible all -m ping`, you should get this:
```
task1 | success >> {
    "changed": false,
    "ping": "pong"
}
``` 
If you get some error like:

`task1 | FAILED => private_key_file (./insecure_private_key) is group-readable or world-readable and thus insecure - you will probably get an SSH failure`

or like this:

```
task1 | UNREACHABLE! => {
    "changed": false,
    "msg": "ERROR! SSH Error: data could not be sent to the remote host. Make sure this host can be reached over ssh",
    "unreachable": true
}
```

Run:

`chmod 400 insecure_private_key`

## Windows

### Step 1.
Install [Virtualbox](https://www.virtualbox.org/wiki/Downloads)

We'll use it for creating and destroying virtual machines on your computer easily.

### Step 2.
Install [Vagrant](http://www.vagrantup.com/downloads)

The machines we'll use during the workshop will be created and managed using vagrant.

### Step 3.
Clone/download this repository to your computer

### Step 4.
Run `vagrant up` from the root folder of the repository

Now you can connect to the machine using `vagrant ssh`

### Verification.

- Clone/download the [workshop repository](https://github.com/penguinjournals/ansible-101)
- From inside task1 folder run "vagrant up" (you'll need internet in this step)
- From inside the vagrant-control-machine (remember the `vagrant ssh` on Step 4) type:

```
cd vagrant
git clone https://github.com/penguinjournals/ansible-101
cd task1
ansible all -m ping
```

You should get something like:
```
task1 | success >> {
    "changed": false,
    "ping": "pong"
}
```
If you get some error like:

`task1 | FAILED => private_key_file (./insecure_private_key) is group-readable or world-readable and thus insecure - you will probably get an SSH failure`

Run:

`chmod 400 insecure_private_key`

If you have any problem contact me at twitter [@penguinjournals](http://penguinjournals.com/penguinjournals) or via email at dgonzalezdiez [at] gmail [dot] com.
