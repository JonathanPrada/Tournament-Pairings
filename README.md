# SWISS PAIRINGS LOGIC 

A Swiss style pairing tournament database using git gui, vm, python and postgresql.

## FILES

tournament.py - This file is used to provide access to your database via a library of functions which can add, delete or query data in your database to another python program (a client program).

tournament.sql - this file is used to set up your database schema (the table representation of the data structure).

tournament_test.sql - this is a client program which will test the functions written in the tournament.py module. It will pass in values and check functions in tournament.py successfully completed printing results.

## INSTALLATION

Download Vagrant and Virtual Box
Recommend download GIT Gui
Download or clone Github Repo
Make sure your command line has python, if not download python to your terminal

## CONFIGURATION

All tournament pairing scripts within a file housing Vagrant in the following structure:

/vagrant/tournament/tournament.py, tournament_test.py, tournament.sql.

## RUNNING

The scripts have been previously executed with GIT command line.

Using GIT Gui, CD into root directory of vagrant file:
cd /vagrant

Within the vagrant folder type:
'''
vagrant up
vagrant ssh
'''

CD to /vagrant/tournament folder:
'''
cd /vagrant/tournament
'''

Connect to postgresql:
'''
psql
'''

Execute the tournament database schema setup:
'''
\i tournament.sql;
\q
'''

Back on /vagrant/tournament, execute the tests:
'''
python tournament_test.py
'''

You will see a list of test results.
