# 1° questão (Resultado soma)

indice = 13
soma = 0
K = 0

while K < indice:
    K = K + 1
    soma = soma + K
    
print(soma) # soma = 91 

# 2° questão (Fibonacci)

def fibonacci_sequence(n):
    fib_seq = [0, 1]
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def is_in_fibonacci(n):
    fib_seq = fibonacci_sequence(n)
    return n in fib_seq

def main():
    try:
        num = int(input("Digite um número inteiro: "))
        
        if is_in_fibonacci(num):
            print(f"{num} está incluso na sequência de Fibonacci.")
        else:
            print(f"{num} não está incluso na sequência de Fibonacci.")
            
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
        
main()
        
# 3° questão (lógicas)

"""
Respostas
a) 9 (soma-se 2 ao último número)
b) 128 (multiplica-se por 2 o último número)
c) 49 (o número a ser somado aumenta de 2 em 2, começando por 1)
d) 100 (o número a ser somado aumenta de 8 em 8, começando por 8)
e) 13 (Soma-se os dois digitos anteriores para adquirir o próximo semelhante a sequência de fibonacci)
f) 200 (números que começam com a letra D)
"""

# 4° questão (lâmpadas)

"""
Resposta:
A solução clássica para esse problema seria ligar o primeiro interruptor e deixá-lo ligado por alguns minutos,
depois desligá-lo e ligar o segundo interruptor e então entrar na sala. Dessa forma, a luz que estiver ligada está
conectada ao segundo interruptor a que estiver desligada e quente ao toque está conectada ao primeiro interruptor
e a que estiver desligada e fria ao toque está conectada ao terceiro interruptor.
"""

# 5° questão (string invertida)

# Utilizando fatiamento de strings em Python podemos resolver desta maneira:

string = input(" Digite uma string qualquer: ")

string_invertida = string[::-1]

print(f"A string invertida é: {string_invertida}")