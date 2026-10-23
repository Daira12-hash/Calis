#""---------------------------------------------------
#hands on - Asistente Financiero 
#eres un estudiante universitario que recibe una cantidad limitada de dinero para cubrir sus gastos de la semana
#crear un programa que defina:
# cuanto dinero tienes disponible al inicio de la sema
#registre tres gastos principales (transporte, comida, material escolar)
#calcule cuanto gastaste en total
#determinar cuanto dinero te queda
#muestre una recomendación dependiendo tu situación financiera
#---------------------------------------------------------""
#inicio de semana 
presupuesto_semanal=600
print(presupuesto_semanal)

#Traslado de ida y vuelya
gasto_transporte= 66

#Desayunos, comidas, etc
gasto_comida=300

#copias, utiles, etc.
gasto_material_escuela=100


gasto_total= gasto_transporte + gasto_comida + gasto_material_escuela
print(gasto_total)

balance_final= presupuesto_semanal - gasto_total
if balance_final > 100:
    print("Vas bien, sigue asi, te quedan" + str (balance_final) + "libres")
    
else:
    print("Cuida tus finanzas chiquis: Guarda un poco")