from dotenv import load_dotenv
import flask_file
import os


load_dotenv()

if __name__ == "__main__":
    try:
        app = flask_file.create_app()
        #app.run( host="172.20.11.47",port=3000 ,debug=True)
        print("env cehck",os.getenv('CERT_FILE'),os.getenv('CERT_KEY') )
        if os.getenv("Env") == "Local":
            app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
        if os.getenv("Env") == "Dev":
            print('devv')
            app.run(host=os.getenv('HOST'), port=os.getenv(
            'PORT'),certfile=os.getenv('CERT_FILE'), keyfile=os.getenv('CERT_KEY'))
    except Exception as e:
        print("Error: Unable to start the application.")
        print(e)

