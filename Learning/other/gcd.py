v1 = input("a:")

v2 = input("b:")

print(v1)

a = 1
print(a+int(v1))

v1 = int(v1)
v2 = int(v2)
vmax = max(v1,v2)
vmin = min(v1,v2)



while True:
	vmax -= vmin
	print('vmax %s   vmin %s' % (vmax,vmin))
	if vmax == 0:
		print('best %d' % vmin)
		break
	if vmax<vmin:
		# temp = vmin
		# vmin = vmax
		# vmax = temp
		vmax,vmin = vmin,vmax