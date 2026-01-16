# Lab Submission Template
# Week 1 Lab Practice: Introduction to Git and GitHub
- **Name**: Avery Yong
- **Student ID**: 059789115
- **Due Date**: Jan 18, 2026
---
## Table of Contents
1. [Introduction](#introduction)
2. [VM Configuration Details](#vm-configuration-details)
3. [Command Outputs](#command-outputs)
4. [Screenshots](#screenshots)
5. [Experience and Challenges](#experience-and-challenges)
---
## Introduction
Provide a brief overview of the lab. Summarize its objective and key tasks you performed.
---
## VM Configuration Details
Describe the virtual machine setup. Include details like:
- **VM Name**: `ControlNode`
- **RAM**: `4 GB`
- **Disk Space**: `25 GB`
- **CPU Cores**: `2`
- **Network Adapter**: `NAT`
---
## Code Block Deliverables
### Deliverable 1:
```bash
# Command executed
lsb_release -a
```
**Output**:
```bash
Distributor ID:	Ubuntu
Description:	Ubuntu 24.04.3 LTS
Release:	24.04
Codename:	noble
```
### Deliverable 2: 
```bash
# Command executed
uname -a
```
**Output**:
```bash
Linux ayong2-undefined 6.8.0-90-generic #91-Ubuntu SMP PREEMPT_DYNAMIC Tue Nov 18 14:14:30 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
```
### Deliverable 5:
```bash
# Command executed
git config --list
```
**Output**:
```bash
user.name=SenCoAyon
user.email=cloudyboi0@hotmail.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
remote.origin.url=git@github.com:SenCoAyon/SRT205_Labs.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.master.remote=origin
branch.master.merge=refs/heads/master
```
### Deliverable 6: 
```bash
# Command executed
git log
```
**Output**:
```bash
commit 81138689ce1482a372108c0f347a961d0b44ccab
Author: SenCoAyon <cloudyboi0@hotmail.com>
Date:   Fri Jan 16 21:09:28 2026 +0000

    Is this right?

commit 7757f91652e7381a8b29e932ca5088442cec1910
Author: SenCoAyon <cloudyboi0@hotmail.com>
Date:   Fri Jan 16 15:09:38 2026 -0500

    test

```


Repeat this structure for all the commands you executed during the lab.
---
## Screenshots Deliverables
### Deliverable 3: GitHub Dashboard
![My GitHub Dashboard](/Lab01/Dashboard.png)
### Deliverable 4: SRT205-Labs Repo Collab Page?
![Empty Collaborator Page due to Seneca Issues](/Lab01/Collaboration.png)
### Deliverable 7: Branches
![Branches](/Lab01/Branches.png)
---
## Experience and Challenges
### Reflection on Completing the Lab
- **What did you learn?**: Just a quick recap of some commands and some git commands.
- **Challenges Faced**: Destroyed a VM because I messed up branches on my git. I'm still very confused as to why my git wasn't finding the ~/.ssh/id_rsa
- **How You Overcame Challenges**: Google is helpful, and most of the wrong git commands give feedback that often work. 

