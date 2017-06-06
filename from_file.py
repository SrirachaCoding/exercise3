from sys import argv

script, filename, *args = argv

txt = open(filename)
#txt = open('sample.txt', 'r')

print(*args, args[0])

print ("here's your file %r:" %filename)
txt_out = txt.read()
print (txt_out)

if args[0] == '-m':
	print("Do you want to make a copy? (yes)")
	if (input() == 'yes'):
		index = filename.find('.')
		# CAUTION! WILL OVERWRITE FILE IF IT ALREADY EXISTS
		# future version can attempt to open it first. If fails, create. 
		#Else, add number and try again.
		new_filename = filename[:index] + '_copy'+ filename[index:]
		txt2 = open(new_filename, 'w+')
		print(txt2.write(txt_out))
		txt.close()
		txt2.close()

	else:
		print("no problem!")

