import mysql.connector as sql

def get_connection(db):
    try:
        cnx = sql.connect(host='localhost', user='root', password='***', database=db)
        print('ok')
        return cnx
    except Exception as e:
        print(e)

def get_data_list(connection: sql.MySQLConnection, 
                   query_text:str,reset=True):
    try:
        cur_con = connection
        if reset:
            cur_con.reset_session()
        cursor = cur_con.cursor()
        query = query_text
        cursor.execute(query)
        res = cursor.fetchall() 
        cols = cursor.column_names
        cursor.close()
        cur_con.close()
        return (res, cols)
    
    except Exception as e:
        print(e)