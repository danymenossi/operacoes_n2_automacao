#import cx_Oracle

#def conectar():
#    conn = cx_Oracle.connect("usuario/senha@endereco_do_banco")  # Substitua com as informações de conexão corretas
#    return conn

#def executar_consulta(conn, consulta):
#    cursor = conn.cursor()
#    cursor.execute(consulta)
#    resultado = cursor.fetchall()
#    cursor.close()
#    return resultado

#def fechar_conexao(conn):
#    conn.close()