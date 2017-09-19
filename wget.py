import urllib.request
import urllib.response
import MySQLdb


#CONEXAO COM BANCO DE DADOS
con = MySQLdb.connect(host="localhost", user="root", passwd="", db="test")
con.select_db('test')
cursor = con.cursor()

#EXECUTANDO QUERY
cursor.execute('SELECT * FROM URL WHERE STT = 0')
#SE A QUERY RETORNOU VALORES
if int(cursor.rowcount) > 0:
   i=0
   noar = []
   foradoar = []
   #LAÇO PARA PEGAR INFORMAÇÕES 
   for row in cursor.fetchall():
      #TENTANDO ENCONTRAR A URL
      try:
         url = row[1]
         domain = urllib.parse.urlsplit(url)[1].split(':')[0]
         f = urllib.request.urlopen(row[1])
   
         #AQUI DESCOBRIMOS SE HOUVE REDIRECT OU NAO
         if domain in (f.geturl()):
            print('mesmo dominio')
            print(f.geturl())
         else:
            print('dominios diferentes')
            print(f.geturl())
         #PEGAMOS O CONTEUDO DA PAGINA
         body = f.read()

         #TESTAMOS OS TERMOS PRA VER SE A PÁGINA É NOSSA
         
         if b"termo1" in body:
            noar.append(row[0])
        #TESTAMOS OS TERMOS PRA VER SE A PÁGINA É NOSSA
         if b"termo2" in body:
            noar.append(row[0])
           #SE A URL NÃO EXISTIR         
      except:
            foradoar.append(row[0])
   
#SE NÃO RETORNOU   
else:
    print("sem linhas")

i=0
while i < len(noar):
   cursor.execute("UPDATE `URL` SET `DT_INI` = '2017-09-18' WHERE `ID_URL` = "+ str(noar[i]))
   con.commit()
   i = i+1

i=0
while i < len(foradoar):
   cursor.execute("UPDATE `URL` SET `DT_FIM` = '2017-09-18' WHERE `ID_URL` = "+ str(foradoar[i]))
   con.commit()
   i=i+1

 

    
    

