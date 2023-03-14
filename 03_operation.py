set_a={"col","mex","bol"}
set_b={"pe", "bol"}

set_c=set_a.union(set_b)
print(set_c)
print(set_a|set_b)    # el simbolo " | " funciona como la unión de conjuntos 
print(set_a & set_b)    # el simbolo " & "  funciona como la intersección entre conjuntos
print (set_a-set_b)   # el simbolo " - " es la diferencia entre los conjuntos
print (set_a ^ set_b)  # el simbolo " ^ " es la diferencia simetrica