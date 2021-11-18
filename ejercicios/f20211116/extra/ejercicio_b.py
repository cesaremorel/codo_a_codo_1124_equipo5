def myfunction(company_name):
    company_name = company_name.lower()
    caracteres = []
    apariciones = []
    for i in company_name:
        if (i != " " and i not in caracteres):
            caracteres.append(i)
            apariciones.append(company_name.count(i))

    longitud = min(len(caracteres),3)
    for i in range(longitud):
        ubicacion = apariciones.index(max(apariciones))
        print (caracteres[ubicacion],apariciones[ubicacion])
        caracteres.pop(ubicacion)
        apariciones.pop(ubicacion)