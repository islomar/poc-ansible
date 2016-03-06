
import os
import random

import docker

# Extract from
# https://github.com/aebm/docker-image-cleaner

API_VERSION = 'auto'
HTTP_TIMEOUT = 5


def _build_docker_client():
   if _is_osx_platform():
       return _macosx_docker_client()


def _macosx_docker_client():
   from docker.utils import kwargs_from_env
   kwargs = kwargs_from_env()
   # Read http://docker-py.readthedocs.org/en/latest/boot2docker/
   kwargs['tls'].assert_hostname = False

   kwargs['version'] = API_VERSION
   kwargs['timeout'] = HTTP_TIMEOUT
   return docker.Client(**kwargs)


def _is_osx_platform():
   from sys import platform as _platform
   return "darwin" in _platform


client = _build_docker_client()

from pprint import pprint
pprint(client.version())
# print "-"*15
# pprint(client.containers())

#--------------
DATACENTERS = ('mad01', 'par02', 'ber03')
SERVICES = ('frontend', 'backend', 'stats')

# Generate all containers
for i in range(20):
   ct = client.create_container(
       image='frolvlad/alpine-python2',
       command="sleep 8h",
       detach=True,
       name='instance{:02d}'.format(i + 1),
       labels={
           'datacenter': random.choice(DATACENTERS),
           'service': random.choice(SERVICES),
       }
   )
client.start(container=ct['Id'])

# # Delete all containers
# for ct in client.containers(all=True):
#     if not ct['Names'][0].startswith('/instance'):
#         continue
#
#     client.remove_container(ct['Id'], force=True)