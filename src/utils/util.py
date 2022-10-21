import re

class Util:

    def __init__(self) -> None:
        pass

    def valida_cpf_caracter_igual(self, cpf):
        count = 0
        val_count_igual = 0
        caracter = ''
        for n in cpf:
            if count == 0:
                caracter = n
                count += 1
            else:
                if caracter == n:
                    count += 1
                    val_count_igual += 1
        if val_count_igual >= 10:
            return False
        else:
            return True

    def valida_cpf(self, cpf):
        # valida se tem letra
        if cpf:
            if type(cpf) == str:
                try:
                    cpf = int(cpf)
                    cpf = str(f"{cpf:011}")
                except Exception:
                    return False
            else:
                cpf = str(f"{cpf:011}")
        else:
            return False
        processo_cpf_igual = self.valida_cpf_caracter_igual(cpf)
        if processo_cpf_igual:
            sum = 0
            weight = 10
            for n in range(9):
                sum = sum + int(cpf[n]) * weight
                weight = weight - 1
            verifyingDigit = 11 - sum % 11
            firstVerifyingDigit = 0
            if verifyingDigit <= 9:
                firstVerifyingDigit = verifyingDigit
            sum = 0
            weight = 11
            for n in range(10):
                sum = sum + int(cpf[n]) * weight
                weight = weight - 1
            verifyingDigit = 11 - sum % 11
            secondVerifyingDigit = 0
            if verifyingDigit <= 9:
                secondVerifyingDigit = verifyingDigit
            if cpf[-2:] == "%s%s" % (firstVerifyingDigit, secondVerifyingDigit):
                return True
        else:
            return False