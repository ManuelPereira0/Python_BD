import pymysql.cursors

#Abrir uma conexão

con = pymysql.connect(host='ip host',user='root', database='dados', password='senha', cursorclass=pymysql.cursors.DictCursor)

#Preparar um cursos com o método .cursor()

with con.cursor() as c:
#Criar um consulta  
    #sql1 = "insert into cadastro values (2,'Fernando','Fone','2023/01/20', 100,1)"
    sql = "select * from cadastro"
    c.execute(sql)
    resultados = c.fetchall()

    print("Total rows are:  ", len(resultados))
    print("Printing each row")

    for resultado in resultados:
        print('\n')
        print(resultado.get("cliente"))
        print(resultado.get("produto"))
        print('\n')
    c.close()   