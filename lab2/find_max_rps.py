import subprocess
import time

def test_rps(url, concurrency=1):
    cmd = f"ab -n {concurrency*10} -c {concurrency} {url}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    for line in result.stdout.split('\n'):
        if 'Requests per second' in line:
            rps = float(line.split()[3])
            return rps
    return 0

def find_max_rps(url, start_concurrency=1):
    concurrency = start_concurrency
    while True:
        print(f"Testing concurrency: {concurrency}")
        rps = test_rps(url, concurrency)
        print(f"RPS: {rps:.2f}")
        
        concurrency = int(concurrency * 1.1)
        max_concurrency = 500
	if concurrency > max_concurrency:
    		break
        
        time.sleep(1)

if __name__ == "__main__":
    print("Testing nginx public location:")
    find_max_rps("http://localhost:8080/public/test.jpg")
    
    print("\nTesting nginx gunicorn location:")
    find_max_rps("http://localhost:8080/gunicorn")
    
    print("\nTesting direct WSGI:")
    find_max_rps("http://localhost:8000/")
