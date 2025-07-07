import mysql.connector
from config import MYSQL_CONFIG

def get_connection():       #create and return data base connection from config
    return mysql.connector.connect(**MYSQL_CONFIG)

def query_db(query,args=(), one=False): #Reading the data 
    conn=get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, args)
    result = cursor.fetchall()
    conn.close()
    return result [0] if one and result else result 

def execute_db(query, args=()): #Executes the query (edit)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    conn.close()
