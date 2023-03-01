
def revert_str(str_in: str) -> str:
    str_out = ''
    for index in range(-1, -len(str_in)-1, -1):
        str_out += str_in[index]
    return str_out


string_input = input("Escreva algo para inverter os caracteres: ")

print(revert_str(string_input))
