#!/usr/bin/python3
# Milo Miles
# Automating User Additions
# Program Creation: 11/6
# Program Last Updated: 11/6


#Importing the Operation System and other pieces needed to run the program
import os
import re
import sys

def main():
    for line in sys.stdin:

        #Checks to see if the line is commented out, if so it skips the line
        match = re.match("^#",line)

        #Splitting the line that was fed in into the five categories
        fields = line.strip().split(':')

        #If there are less than 5 fields input from the file it skips the user and moves on to the next user
        if match or len(fields) != 5:
            continue

        username = fields[0] #Sets the variables to prepare for the system call
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])
        groups = fields[4].split(',')
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        #print(cmd)
        os.system(cmd) #System call to add user
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        #print (cmd)
        os.system(cmd)

        for group in groups:
            #Looks and assignes the added user to whatever groups were imput
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
