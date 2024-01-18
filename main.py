
def hallar_divisores(n):
	print(f"Los divisoressss de {n} son:", end=" ")
	for i in range(1, n + 1):
		if n % i == 0:
			print(i, end=" ")
	print()

def main():
	print("Programa para hallar los divisores de un numero")
	while True:
		entrada = int(input("por favor inserte un numero: "))
		hallar_divisores(entrada)

if __name__ == "__main__":
	main()