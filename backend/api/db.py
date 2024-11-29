import mysql.connector
mydb = mysql.connector.connect(
    host="database", 
    user="root",
    passwd="messageboard",
    port="3306"
)

my_cursor = mydb.cursor()
my_cursor.execute("USE messageboard;")
print("connected", flush=True)
def insert_message(identity, message):
    query = f"INSERT INTO messages(identity, message) VALUES (\"{identity}\", \"{message}\");"
    my_cursor.execute(query)
    mydb.commit()

def select_message(search_query):
    query = f"SELECT * FROM messages WHERE messages.message LIKE \'%{search_query}%\';"
    my_cursor.execute(query)
    data = {}
    for result in my_cursor:
        data[result[0]] = result[1] 
    return data
    
