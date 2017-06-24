
def main():
	a = [5,3,1,6]

	c = a[0:3];

	b = sorted(a)

	a.sort()
	print(a)
	print(b)
	print(c)

	d = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
	print(d)

	e = sorted(d)
	print(e)

	student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
	]

	f = sorted(student_tuples, key=lambda student: student[2])
	print(f)

if __name__ == '__main__':
	main()