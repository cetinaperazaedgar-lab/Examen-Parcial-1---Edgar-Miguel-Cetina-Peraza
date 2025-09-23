def D_B_E(n):
    if n == 0:
        return ""
    return D_B_E(n // 2) + str(n % 2)

def D_B (num, precision=15):
    entero = int(num)
    decimal = num - entero
    
    bin_entero = D_B_E(entero)
    if bin_entero == "":
        bin_entero = "0"
    
    bin_decimal = ""
    while decimal > 0 and len(bin_decimal) < precision:
        decimal *= 2
        bit = int(decimal)
        bin_decimal += str(bit)
        decimal -= bit
    
    return bin_entero + ("." + bin_decimal if bin_decimal else "")
print("="*30)
print("Conversor de decimal a binario")
num = float(input("\nIntroduce un número: "))
print("Equivalente en binario:", D_B(num))
print("="*30)