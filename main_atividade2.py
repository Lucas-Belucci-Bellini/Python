
def main():
	data = input().strip().split()
	if len(data) >= 2:
		a, b = int(data[0]), int(data[1])
	else:
		a = int(data[0]) if data else int(input())
		b = int(input())

	
	if a == 0:
		
		ok = (b == 0)
	else:
		ok = (b % a == 0)

	print("SIM" if ok else "NAO")


if __name__ == '__main__':
	main()
