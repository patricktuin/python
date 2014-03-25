
import re

input_file = open('sso2.txt', 'r')
output_file = open('output.txt', 'w')

counter = 0
all_line = input_file.readlines()
for each_line in all_line:
	timeStamp1 = re.search("[[A-Za-z0-9_+_:_/_ ]*]", each_line)
	timeStamp2 = re.search("&timestamp=[^&]+", each_line)
	username = re.search('username=[^&]+', each_line)
	counter += 1
	username = username.group()
	username_re = re.compile("username=", re.MULTILINE)
	username = username_re.sub('', str(username))
	print (str(counter) + " " + username)
	output_file.write (str(counter) + " " + username + "\n")

#input_file.close
#output_file.close


