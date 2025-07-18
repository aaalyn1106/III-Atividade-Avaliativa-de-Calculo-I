import math

def criar_funcao(expressao):
    """Cria uma função a partir de uma expressão string usando eval()."""
    ambiente = {
        'x': None,
        'math': math,
        'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
        'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
        'sinh': math.sinh, 'cosh': math.cosh, 'tanh': math.tanh,
        'exp': math.exp, 'log': math.log, 'log10': math.log10,
        'sqrt': math.sqrt, 'abs': abs,
        'pi': math.pi, 'e': math.e
    }
    return lambda x: eval(expressao, ambiente, {'x': x})

def derivada(f, x0, h=1e-5, metodo='central'):
    """Calcula a derivada numérica usando diferenças finitas."""
    if metodo == 'progressiva':
        return (f(x0 + h) - f(x0)) / h
    elif metodo == 'regressiva':
        return (f(x0) - f(x0 - h)) / h
    elif metodo == 'central':
        return (f(x0 + h) - f(x0 - h)) / (2 * h)
    else:
        raise ValueError("Método inválido. Escolha entre 'progressiva', 'regressiva' ou 'central'.")

def integral(f, a, b, n=1000, metodo='esquerda'):
    """Calcula a integral numérica usando Soma de Riemann."""
    if n <= 0:
        raise ValueError("O número de subintervalos 'n' deve ser positivo.")
    dx = (b - a) / n
    soma = 0.0
    
    if metodo == 'esquerda':
        pontos = [a + i * dx for i in range(n)]
    elif metodo == 'direita':
        pontos = [a + (i + 1) * dx for i in range(n)]
    elif metodo == 'centro':
        pontos = [a + (i + 0.5) * dx for i in range(n)]
    else:
        raise ValueError("Método inválido. Escolha entre 'esquerda', 'direita' ou 'centro'.")
    
    for x_i in pontos:
        soma += f(x_i) * dx
    return soma

def main():
    print("="*60)
    print("CALCULADORA NUMÉRICA - DERIVADAS E INTEGRAIS")
    print("="*60)
    print("\nINSTRUÇÕES PARA INSERIR FUNÇÕES:")
    print("1. Use 'x' como variável independente")
    print("2. Operadores matemáticos:")
    print("   + : adição       - : subtração")
    print("   * : multiplicação / : divisão")
    print("   ** : potenciação (ex: x**2 para x ao quadrado)")
    print("3. Funções disponíveis:")
    print("   sqrt(x) : raiz quadrada    abs(x) : valor absoluto")
    print("   sin(x), cos(x), tan(x) : trigonométricas (radianos)")
    print("   exp(x) : exponencial (e^x)   log(x) : logaritmo natural")
    print("   log10(x) : logaritmo base 10")
    print("4. Constantes: pi (3.14159...)  e (2.71828...)")
    print("\nEXEMPLOS DE FORMATAÇÃO:")
    print("   x**2 + 3*x - 5")
    print("   sin(x)*cos(x)")
    print("   2**x + abs(x-4)")
    print("   sqrt(1 + x**2)")
    print("   exp(-x**2/2)/sqrt(2*pi)")
    print("="*60)
    
    expressao = input("\nDigite a função f(x): ")
    try:
        f = criar_funcao(expressao)
        # Teste para verificar se a função é válida
        teste = f(1.0)
        print("Função validada com sucesso!")
    except Exception as e:
        print(f"ERRO NA FUNÇÃO: {e}")
        print("Verifique a formatação e sintaxe da expressão")
        return

    operacao = input("Deseja calcular (D)erivada ou (I)ntegral? ").strip().upper()
    
    if operacao == 'D':
        print("\nMÉTODOS DE DERIVAÇÃO NUMÉRICA:")
        print("  progressiva : (f(x+h) - f(x)) / h")
        print("  regressiva  : (f(x) - f(x-h)) / h")
        print("  central     : (f(x+h) - f(x-h)) / (2h) [MAIS PRECISO]")
        
        x0 = float(input("\nPonto para calcular a derivada (x0): "))
        h = float(input("Tamanho do passo (h) [Enter para 0.00001]: ") or 1e-5)
        metodo = input("Método [Enter para central]: ").lower() or 'central'
        
        try:
            resultado = derivada(f, x0, h, metodo)
            print(f"\nRESULTADO: f'({x0}) ≈ {resultado:.8f}")
        except Exception as e:
            print(f"Erro no cálculo: {e}")
    
    elif operacao == 'I':
        print("\nMÉTODOS DE INTEGRAÇÃO (SOMA DE RIEMANN):")
        print("  esquerda : usa ponto esquerdo de cada subintervalo")
        print("  direita  : usa ponto direito de cada subintervalo")
        print("  centro   : usa ponto médio de cada subintervalo [MAIS PRECISO]")
        
        a = float(input("\nLimite inferior de integração: "))
        b = float(input("Limite superior de integração: "))
        n = int(input("Número de subintervalos (n) [Enter para 1000]: ") or 1000)
        metodo = input("Método [Enter para centro]: ").lower() or 'centro'
        
        try:
            resultado = integral(f, a, b, n, metodo)
            print(f"\nRESULTADO: ∫f(x)dx de {a} a {b} ≈ {resultado:.8f}")
        except Exception as e:
            print(f"Erro no cálculo: {e}")
    
    else:
        print("Operação inválida!")

if __name__ == "__main__":
    main()