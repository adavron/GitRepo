Adding DHparameters to multiple IPmons

we set shell variable $pswd to users password so we dont enter user password each time

# pswd='abc123'

in 'txt' file we have IPaddr of hosts
and command which generates DHparam and appends to local.crt file goes into fabfile.py
if there are multiple hosts, its recommended to use  -P -z 1 option for parralell one host at the time execution.
since we are using for loop, we dont need this option.

for i in $(cat txt); do fab -H $i -u UserNameHere -p $pswd openssl; done

to run multiple commands:

for i in $(cat txt); do fab -H $i -u UserNameHere -p $pswd openssl hostname; done

