import traceback
try:
	with open('data2.txt','r+') as f:
		s = f.read()
		f.write('33333')
except Exception as e:

	print('11111111111')
	# traceback.print_exc()
	print('sdfsdfsdf %s' % e)