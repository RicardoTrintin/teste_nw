import os

DATABASE = {
    "host": os.environ.get("HOST_DATABASE"),
    "port": os.environ.get("PORT_DATABASE"),
    "database": os.environ.get("DATABASE"),
    "user": os.environ.get("USER_DATABASE"),
    "password": os.environ.get("PASS_DATABASE"),
}