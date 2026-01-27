## Lab 3 - Ansible Inventory Management
- **Name**: Avery Yong
- **Student ID**: 059789115
- **Date**: January 26, 2026
---
## Table of Contents
1. [Introduction](#introduction)
2. [VM Configuration Details](#vm-configuration-details)
3. [Command Outputs](#command-outputs)
4. [Screenshots](#screenshots)
5. [Experience and Challenges](#experience-and-challenges)
---
## Introduction
Learn about static and dynamic inventory files. 
Configure and manage SSH-based connectivity between nodes.
Use inventory files to organize and target managed nodes effectively.
Learned a few manners of using ansible as a remote tool
e.g
```bash
ansible-playbook -i static_inventory install_git.yml -K 
```
and
```bash
ansible -i static_inventory all -a "git --version"
```
for installing git and checking the versions

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
Managed Node 2
- **VM Name**: `ManagedNode02`
- **RAM**: `4 GB`
- **Disk Space**: `25 GB`
- **CPU Cores**: `2`
- **Network Adapter**: `Host-Only`

---
## Code Block Deliverables
### Deliverable 1: lsb_release -a
```bash
# Command executed
lsb_release -a
```
**Output on Node1**:
```bash
Distributor ID:	Ubuntu
Description:	Ubuntu 24.04.3 LTS
Release:	24.04
Codename:	noble
```

**Output on Node2**:
```bash
Distributor ID:	Ubuntu
Description:	Ubuntu 24.04.3 LTS
Release:	24.04
Codename:	noble

```

### Deliverable 2: Check if ssh is on the system
```bash
# Command executed
sudo systemctl status ssh
```
**Output**:
```bash
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/usr/lib/systemd/system/ssh.service; enabled; preset: enabled)
     Active: active (running) since Mon 2026-01-26 21:28:44 UTC; 4h 51min ago
TriggeredBy: ● ssh.socket
       Docs: man:sshd(8)
             man:sshd_config(5)
    Process: 830 ExecStartPre=/usr/sbin/sshd -t (code=exited, status=0/SUCCESS)
   Main PID: 850 (sshd)
      Tasks: 1 (limit: 4545)
     Memory: 2.3M (peak: 5.3M)
        CPU: 177ms
     CGroup: /system.slice/ssh.service
             └─850 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"

Jan 26 21:28:43 ControlNode systemd[1]: Starting ssh.service - OpenBSD Secure Shell server...
Jan 26 21:28:44 ControlNode sshd[850]: Server listening on 0.0.0.0 port 22.
Jan 26 21:28:44 ControlNode sshd[850]: Server listening on :: port 22.
Jan 26 21:28:44 ControlNode systemd[1]: Started ssh.service - OpenBSD Secure Shell server.
Jan 26 21:37:04 ControlNode sshd[1619]: Connection closed by authenticating user ayong2 192.168.25.1 port 33104 [preauth]
Jan 26 21:37:04 ControlNode sshd[1626]: Connection closed by authenticating user ayong2 192.168.25.1 port 33108 [preauth]
Jan 26 21:37:08 ControlNode sshd[1638]: Accepted password for ayong2 from 192.168.25.1 port 33122 ssh2
Jan 26 21:37:08 ControlNode sshd[1638]: pam_unix(sshd:session): session opened for user ayong2(uid=1000) by ayong2(uid=0)
Jan 26 21:37:08 ControlNode sshd[1638]: pam_unix(sshd:session): session closed for user ayong2
```
### Deliverable 3: Show static_inventory file
```bash
# Command executed
cat static_inventory
```
**Output**:
```bash
[web_servers]
managed_node01 ansible_host=192.168.25.2 ansible_user=ayong2 ansible_ssh_private_key_file=~/.ssh/id_rsa 
#ansible_password=ubuntu ansible_port=22 ansible_become=yes ansible_become_password=ubuntu	
# Don't store passwords, it's insecure, and possibly easily accessible. I only did it here to test (26-01-26)

[db_servers]
managed_node02 ansible_host=192.168.25.3 ansible_user=ayong2 ansible_ssh_private_key_file=~/.ssh/id_rsa

```
### Deliverable #4: Test connection of ManagedNode01
```bash
# Command executed
ansible -i static_inventory web_servers -m ping
```
**Output**:
```bash
managed_node01 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

### Deliverable #5: See how much free space is available on ManagedNode02
```bash
# Command executed
ansible -i dynamic_inventory.py db_servers -m command -a "free -h"
```
**Output**:
```bash
managed_node02 | CHANGED | rc=0 >>
               total        used        free      shared  buff/cache   available
Mem:           3.8Gi       490Mi       3.2Gi       1.5Mi       365Mi       3.3Gi
Swap:          2.2Gi          0B       2.2Gi
```

### Deliverable #6: Execute install_git.yml playbook
```bash
# Command executed
ansible-playbook -i static_inventory install_git.yml -K
```
**Output**:
```bash

PLAY [Install software on all servers] *****************************************

TASK [Gathering Facts] *********************************************************
ok: [managed_node01]
ok: [managed_node02]

TASK [Install git] *************************************************************
ok: [managed_node02]
ok: [managed_node01]

PLAY RECAP *********************************************************************
managed_node01             : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
managed_node02             : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```
---

## Experience and Challenges
### Reflection on Completing the Lab
- **What did you learn?** Provide a brief summary of your takeaways from this lab.
- **Challenges Faced**: Highlight any difficulties you encountered during the lab.
- **How You Overcame Challenges**: Describe the steps you took or solutions you implemented to resolve the challenges.
