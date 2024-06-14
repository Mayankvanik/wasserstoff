import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def connect_to_database():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_DATABASE')   
    )


def user_history(user1):
    try:
        mydb = connect_to_database()
        mycursor = mydb.cursor()

        sql =  f"""SELECT question,answer FROM(SELECT * FROM chatbot_demo_backend.new_table_openai WHERE user_id = "{user1}" ORDER BY idabsx DESC LIMIT 10) AS sub ORDER BY idabsx ASC"""# "SELECT question,answer FROM chatbot_demo_backend.new_table_openai where user_id = %s"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        
        # Check if the user exists and is a seller
        print('allll new',result)
        return  result #[0] 

    except Exception as e:
        print('Error checking user existence: ', e)
        return False
    
def user_new(user1,question,answer,charge):
    #return (answer)
    try:
        mydb = connect_to_database()
        mycursor = mydb.cursor()
        #print('mm\\mm')
        sql1 = "INSERT INTO chatbot_demo_backend.new_table_openai (user_id, question, answer ,charges) VALUES (%s, %s, %s, %s)" # "UPDATE practice.users SET amount = amount - %s WHERE user_id = %s"
        val1 = (user1,question,answer,charge)

        mycursor.execute(sql1, val1)
        mydb.commit()

        sql =  f"""SELECT question,answer FROM(SELECT * FROM chatbot_demo_backend.new_table_openai WHERE user_id = "{user1}" ORDER BY idabsx DESC LIMIT 10) AS sub ORDER BY idabsx ASC"""# "SELECT question,answer FROM ` chatbot-demo-backend`.user_bot where user_id = %s"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        
        # Check if the user exists and is a seller
        #print(result)
        return  result 
    
    except Exception as e:
        print('Error checking user existence: ', e)
        return False
    

    
