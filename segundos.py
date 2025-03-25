#saiba quantos segundos é equivalente em minutos, horas e segundos
#pede ao usuario os segundos que quer consultar
segundos_inp = int(input("Olá, bem vindo ao programa, insira os segundos desejados: "))
#a variavel horas recebe os segundos coletados divido por quantos segundos tem uma hora
horas = segundos_inp // 3600
#pegos os mesmos segundos e tiro o resto da divisão entre os segundos inseridos e 3600
segundos_restantes = segundos_inp % 3600
#a variavel minutos recebe segundos restantes divido pela quantidade de segundos que tem em um minuto
minutos = segundos_restantes // 60
#tira o resto da divisão entre os segundos restante e 60
segundos_restantes_final = segundos_restantes % 60
#mostra o resultado final do codigo
print("horas = ", horas, "|minutos ", minutos, "|segundos = ", segundos_restantes_final)
