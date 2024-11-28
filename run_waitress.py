from waitress import serve
from online_shop.wsgi import application

if __name__ == '__main__':
    try:
        print("Starting the server...")
        serve(application, host='0.0.0.0', port=8000)
    except Exception as e:
        print(f"An error occurred: {e}")
