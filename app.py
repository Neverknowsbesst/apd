def simula_apd(transiciones, aceptarPorFinal, estadoInicial, estadoFinal, palabra):
    estado = estadoInicial
    palabra = palabra.strip()
    stack = ["R"]
    i = 0

    while i <= len(palabra):
        if i < len(palabra):
            simbolo = palabra[i]
        else:
            simbolo = 'ε'
        simbolo_en_stack = stack[-1]

        transicion = (estado, simbolo, simbolo_en_stack)

        if transicion in transiciones:
            nuevo_estado, escribir_en_stack = transiciones[transicion]
            estado = nuevo_estado

            if escribir_en_stack == 'ε' and stack[-1] != 'R':
                stack.pop()
            else:
                for simbolo_transicion in reversed(escribir_en_stack):
                    stack.append(simbolo_transicion)

            if simbolo != 'ε':
                i += 1

        else:
            break
    if aceptarPorFinal:
        return estado == estadoFinal
    else:
        return stack == ['R']


transiciones = {
    ('q0', 'a', 'R'): ('q1', 'AR'),
    ('q1', 'b', 'A'): ('q1', 'ε'),
    ('q1', 'ε', 'R'): ('qf', 'ε')}
print(simula_apd(transiciones, True, 'q0', 'qf', 'ab')
)
transiciones = {
    ('q0', 'a', 'R'): ('q1', 'AR'),
    ('q1', 'b', 'A'): ('q1', 'ε'),
    ('q1', 'ε', 'R'): ('qf', 'ε')}
print(simula_apd(transiciones, True, 'q0', 'qf', 'aa')
)