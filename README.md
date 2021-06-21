# Logs Analysis

[Udacity Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044)

## Table of Contents

- [Description](#description)
- [Requirement](#requirement)
- [Repository data](#repository-data)
- [Install](#install)
  - [Using Vagrant virtual machine](#using-vagrant-virtual-machine)
- [Updates post mentor review](#updates-post-mentor-review)

## Description

This Project is created as part of Udacity Full Stack Web Developer Nanodegree. The project creates a reporting tool that prints out reports based on the data in an existing database. As prerequisite, a newspaper site database is provided which contains newspaper articles, authors and the web server log for the site.
This reporting tool is a Python program that uses Structured Query Language (SQL) to perform queries on database.

## Requirement

The requirement is to report the results for below queries :- 
1. What are the most popular three articles of all time? Which articles have been accessed the most?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Repository data
The repository contains below main files :-
- _[logs_analysis.py](logs_analysis.py)_ - Python Program.
- _[logs_analysis.txt](output/logs_analysis.txt)_ - Resulting output text file.
- _[README.md](README.md)_ - Project Documentation.

## Install
As a prerequisite, installation steps are provided by udacity.

### Using Vagrant virtual machine

- #### Install VirtualBox and Vagrant
  Install VirtualBox from virtualbox.org to run a virtual machine. Install Vagrant to configure the VM.
  I have used VirtualBox-6.0.14 version with Vagrant-2.2.6 version.

- #### VM configuration
  Follow the Vagrant virtual machine configuration from [Udacity virtual machine configuration](https://github.com/udacity/fullstack-nanodegree-vm) to start and ssh into virtual   machine.
  
- #### Run the python program
  Place the logs_analysis.py file inside FSND-Virtual-Machine/vagrant/tool folder in your machine.
  ```sh
  ❯ cd /FSND-Virtual-Machine/vagrant
  Run vagrant up and ssh commands to log into machine
  ❯ vagrant up
  ❯ vagrant ssh
  ❯ vagrant@vagrant:~$ cd /vagrant/tool
  Install psycopg2 library to run with python3
  ❯ sudo apt-get install python3-psycopg2
  ❯ vagrant@vagrant:/vagrant/tool$ python3 logs_analysis.py
  Or run below cmd
  ❯ vagrant@vagrant:/vagrant/tool$ python logs_analysis.py
  ```
  
## Updates post mentor review
- str.format is replaced with f-strings in print function. f-strings are supported from python 3.6 version.
  To run the python file log_analysis.py make sure to install python-3.6. The configurations mentioned above provides python-3.5/python-2.7 by default.
  
  ```sh
  ❯ vagrant@vagrant:~$ cd /vagrant/tool
  Install psycopg2 library to run with python3.6
  ❯ vagrant@vagrant:/vagrant/tool$ pip install psycopg2-binary
  ❯ vagrant@vagrant:/vagrant/tool$ python3.6 logs_analysis.py
  ```
