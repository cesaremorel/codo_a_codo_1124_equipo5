def myfunction(array_numbers):
    
    #Se eliminan duplicados
    score_mod = []
    for item in array_numbers:
        if item not in score_mod:
            score_mod.append(item)
    
    #Se ordena de mayor a menor
    ordered_list = sorted(score_mod, reverse = True)

    #Se llama al segundo elemento de la lista ordenada
    return ordered_list[1]
