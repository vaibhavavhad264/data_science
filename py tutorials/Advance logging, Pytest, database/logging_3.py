import logging as lg

lg.basicConfig(
    filename =  'web_app.log',
    level = lg.INFO,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def login(username):
    lg.info(f'User {username} is logged in.')

def process_data(data):
    try:
        if data == "bad_data":
            raise ValueError("Invalid data")
        lg.info(f"Data processed : {data}")
    except ValueError as e:
        lg.error(f"Error processing data : {e}", exc_info = True)

def logout(username):
    lg.info(f"User {username} logged out.")

if __name__ == "__main__":
    username = "admin"
    login(username)
    process_data("bad_data")
    logout(username)
