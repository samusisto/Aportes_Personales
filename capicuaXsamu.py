# PARA IMPRIMIR CAPICUAS DE 5 DÍGITOS DE MANERA SIMPLE
# @samusisto - UNRN, Ingeniería en computación
# respondiendo al desafío del profe de prog I


def prueba():

    for i in range(10):
        for j in range(10):
            for k in range(10):
                print(f"{k}{j}{i}{j}{k}")

if __name__ == "__main__":
    prueba()