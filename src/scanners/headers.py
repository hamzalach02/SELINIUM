import requests

def security_headers_checker(url):
    response = requests.get(url)
    headers = response.headers
    missing_headers = []
    required_headers = ['Content-Security-Policy', 'X-Frame-Options', 'Strict-Transport-Security']
    for header in required_headers:
        if header not in headers:
            missing_headers.append(header)
    if missing_headers:
        print(f"Missing security headers: {', '.join(missing_headers)}")
