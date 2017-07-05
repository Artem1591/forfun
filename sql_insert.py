import mysql.connector
from mysql.connector import errorcode

query_dict = {
    "insert" : "INSERT INTO `database`.`table1`(`name`) VALUES ('{0}');",
}

def commonInsert(query):
    try:
        cnx = mysql.connector.connect(user='root', password='ma',
                                      host='127.0.0.1',
                                      database='database')
        cursor = cnx.cursor()

        cursor.execute(query)

        cnx.commit()

        cursor.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()

def insert(id, name):
    return commonInsert(query_dict["insert"].format(name))

#print insert(3, 'Vazgen')

