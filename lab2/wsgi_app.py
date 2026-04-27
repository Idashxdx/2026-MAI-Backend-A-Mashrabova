import random
import string
import time

def generate_password():
    length = random.randint(8, 16)
    
    digit = random.choice(string.digits)
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    special = random.choice('#[]().,!@&^%*')
    
    remaining_length = length - 4
    all_chars = string.digits + string.ascii_lowercase + string.ascii_uppercase + '#[]().,!@&^%*'
    remaining = [random.choice(all_chars) for _ in range(remaining_length)]
    
    password_list = [digit, lower, upper, special] + remaining
    random.shuffle(password_list)
    
    return ''.join(password_list)

def application(environ, start_response):
    time.sleep(0.05)
    
    password = generate_password()
    response = password + '\n'
    
    status = '200 OK'
    headers = [('Content-Type', 'text/plain; charset=utf-8')]
    
    start_response(status, headers)
    return [response.encode('utf-8')]
