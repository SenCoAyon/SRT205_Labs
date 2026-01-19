# Lab Submission Template
## Title: Lab02
- **Name**: Avery Yong
- **Student ID**: 059789115
- **Date**: January 19th, 2026
---
## Table of Contents
1. [Introduction](#introduction)
2. [VM Configuration Details](#vm-configuration-details)
3. [Command Outputs](#command-outputs)
4. [Experience and Challenges](#experience-and-challenges)
---
## Introduction
Working with ansible and setting it up.
---
## VM Configuration Details
Control Node
- **VM Name**: `ControlNode`
- **RAM**: `4 GB`
- **Disk Space**: `25 GB`
- **CPU Cores**: `2`
- **Network Adapter**: `NAT`
- **Network Adapter**: `Host-Only`
Managed Node 1
- **VM Name**: `ManagedNode01`
- **RAM**: `4 GB`
- **Disk Space**: `25 GB`
- **CPU Cores**: `2`
- **Network Adapter**: `Host-Only`

---
## Code Block Deliverables
### Deliverable 1: Check ansible version
```bash
# Command executed
ansible --version
```
**Output**:
```bash
ansible [core 2.16.3]
  config file = None
  configured module search path = ['/home/ayong2/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python3/dist-packages/ansible
  ansible collection location = /home/ayong2/.ansible/collections:/usr/share/ansible/collections
  executable location = /usr/bin/ansible
  python version = 3.12.3 (main, Jan  8 2026, 11:30:50) [GCC 13.3.0] (/usr/bin/python3)
  jinja version = 3.1.2
  libyaml = True

```
### Deliverable 2: Use setup.yml file to test and install curl
```bash
# Command executed
ansible-playbook -i hosts setup.yml -u ayong2 --become --ask-become-pass
```
**Output**:
```bash

PLAY [Test Ansible Playbook] ***************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Install curl] ************************************************************
ok: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```
### Deliverable 3: Check if ansible local is properly formatted and working
```bash
# Command executed
ansible -i hosts local -m ping
```
**Output**:
```bash
localhost | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}

```
### Deliverable 4: Check curl version
```bash
# Command executed
curl --version
```
**Output**:
```bash
curl 8.5.0 (x86_64-pc-linux-gnu) libcurl/8.5.0 OpenSSL/3.0.13 zlib/1.3 brotli/1.1.0 zstd/1.5.5 libidn2/2.3.7 libpsl/0.21.2 (+libidn2/2.3.7) libssh/0.10.6/openssl/zlib nghttp2/1.59.0 librtmp/2.3 OpenLDAP/2.6.7
Release-Date: 2023-12-06, security patched: 8.5.0-2ubuntu10.6
Protocols: dict file ftp ftps gopher gophers http https imap imaps ldap ldaps mqtt pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp
Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM PSL SPNEGO SSL threadsafe TLS-SRP UnixSockets zstd
```

### Deliverable 6: Test the Connection to ManagedNode01
```bash
# Command executed
ansible -i hosts remote -m ping
```bash
**Output**:
managed_node01 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```
---
## Experience and Challenges
### Reflection on Completing the Lab
- **What did you learn?** To copy the private key you can use ssh-copy-id, and that using sftp to send private keys does not work.
- **Challenges Faced**: The private key, of course.
- **How You Overcame Challenges**: I had to ask for help with how to copy the private keys, only to realize we only needed to have the publickey in authorized keys.
