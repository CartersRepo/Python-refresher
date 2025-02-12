user = {"username": "jose", "access_level": "guest"}

def get_admin_password():
    return "1234"

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            f"User {user["username"]} does not have admin access."
        
    return secure_function

#print(get_admin_password())
get_admin_password = make_secure(get_admin_password)
print(get_admin_password())