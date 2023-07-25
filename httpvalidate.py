import requests
import time
import socket

# All the test functions
def long_header_test(url):
    header_value = 'a' * 10000
    headers = {'X-Custom-Header': header_value}
    response = requests.get(url, headers=headers)
    print(response.status_code)

def long_request_test(url):
    params = {'param': 'a' * 10000}
    response = requests.get(url, params=params)
    print(response.status_code)

def transfer_encoding_test(url):
    headers = {'Transfer-Encoding': 'chunked', 'Content-Length': '100'}
    response = requests.get(url, headers=headers)
    print(response.status_code)

def double_url_encoding_test(url):
    url = url + "%2520"  # Double URL encoded space
    response = requests.get(url)
    print(response.status_code)

def extremely_long_http_request(url):
    params = {'param': 'a' * 60000}
    response = requests.get(url, params=params)
    print(response.status_code)

def extremely_long_parameter(url):
    params = {'param': 'a' * 60000}
    response = requests.get(url, params=params)
    print(response.status_code)

def http_websocket_violation_test(url):
    headers = {'Connection': 'Upgrade', 'Upgrade': 'websocket'}
    response = requests.get(url, headers=headers)
    print(response.status_code)

def illegal_byte_code_char_in_header_name_test(url):
    headers = {'\x00Custom-Header': 'value'}
    response = requests.get(url, headers=headers)
    print(response.status_code)

def illegal_byte_code_char_in_header_value_test(url):
    headers = {'Custom-Header': '\x00value'}
    response = requests.get(url, headers=headers)
    print(response.status_code)
def illegal_byte_code_char_in_method_test(url):
    try:
        response = requests.request('\x00GET', url)
        print(response.status_code)
    except Exception as e:
        print(f"Illegal Byte Code Character in Method Test Exception: {e}")

def illegal_byte_code_char_in_param_name_test(url):
    params = {'\x00param': 'value'}
    response = requests.get(url, params=params)
    print(response.status_code)

def illegal_byte_code_char_in_param_value_test(url):
    params = {'param': '\x00value'}
    response = requests.get(url, params=params)
    print(response.status_code)

def illegal_byte_code_char_in_query_string_test(url):
    url = url + '?query=\x00value'
    response = requests.get(url)
    print(response.status_code)

def illegal_byte_code_char_in_url_test(url):
    url = url + '\x00'  # append NULL byte to URL
    response = requests.get(url)
    print(response.status_code)

#def illegal_chunk_size_test(url):
    # this test may need a raw socket connection and may be server specific
#    pass

def illegal_content_length_test(url):
    headers = {'Content-Length': 'abc'}  # Not an integer
    response = requests.get(url, headers=headers)
    print(response.status_code)

def illegal_content_type_test(url):
    headers = {'Content-Type': '\x00'}  # NULL byte in content type
    response = requests.get(url, headers=headers)
    print(response.status_code)

#def illegal_http_version_test(url):
    # this test may need a raw socket connection to change the HTTP version
#    pass

def illegal_host_name_test(url):
    url = url.replace("http://", "http://\x00")  # Insert NULL byte into host
    response = requests.get(url)
    print(response.status_code)

def illegal_parameter_encoding_test(url):
    params = {'param': 'value\x00'}  # Null byte in parameter value
    response = requests.get(url, params=params)
    print(response.status_code)

#def illegal_response_code_test(url):
  # this test requires a custom server that can return illegal response codes
 #   pass

def illegal_url_path_encoding_test(url):
    url = url + "/%AF%AF"  # Invalid percent encoding
    response = requests.get(url)
    print(response.status_code)

def illegal_content_encoding_test(url):
    headers = {'Content-Encoding': '\x00'}  # NULL byte in content encoding
    response = requests.get(url, headers=headers)
    print(response.status_code)

def malformed_http_header_line_test(url):
    headers = {'X-Custom-Header': 'value\r\nX-Malformed-Header: value'}
    response = requests.get(url, headers=headers)
    print(response.status_code)

def malformed_json_message_test(url):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data='{"malformed json"}')
    print(response.status_code)

def malformed_soap_message_test(url):
    headers = {'Content-Type': 'application/soap+xml'}
    response = requests.post(url, headers=headers, data='<soap:malformed/>')
    print(response.status_code)

def malformed_url_test(url):
    url = url + '%'  # Append malformed percent encoding
    response = requests.get(url)
    print(response.status_code)

def null_char_in_header_name_test(url):
    headers = {'X-Custom\x00Header': 'value'}  # NULL byte in header name
    response = requests.get(url, headers=headers)
    print(response.status_code)

def null_char_in_header_value_test(url):
    headers = {'X-Custom-Header': '\x00value'}  # NULL byte in header value
    response = requests.get(url, headers=headers)
    print(response.status_code)

def null_char_in_param_name_test(url):
    params = {'\x00param': 'value'}
    response = requests.get(url, params=params)
    print(response.status_code)

def null_char_in_param_value_test(url):
    params = {'param': '\x00value'}
    response = requests.get(url, params=params)
    print(response.status_code)

def post_request_missing_content_type_test(url):
    headers = {'Content-Length': '100'}
    response = requests.post(url, headers=headers, data='data')  # POST request with missing content type
    print(response.status_code)

def redundant_http_headers_test(url):
    headers = {'X-Custom-Header': 'value', 'X-Custom-Header': 'value2'}  # Redundant headers
    response = requests.get(url, headers=headers)
    print(response.status_code)

def slow_http_from_single_source_test(url):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((url, 80))
    request = "GET / HTTP/1.1\r\nHost: " + url + "\r\n\r\n"
    for letter in request:
        s.send(letter.encode())
        time.sleep(1)  # Sleep for 1 second
    s.close()

def too_many_cookies_in_a_request_test(url):
    cookies = {f"cookie{i}": "value" for i in range(101)}  # Generate 101 cookies, exceeds common limit
    response = requests.get(url, cookies=cookies)
    print(response.status_code)

def too_many_headers_per_request_test(url):
    headers = {}
    for i in range(101):  # HTTP standard limit is 100 headers
        headers[f"X-Custom-Header-{i}"] = "value"
    response = requests.get(url, headers=headers)
    print(response.status_code)

def too_many_url_parameters_test(url):
    params = {f"param{i}": "value" for i in range(101)}  # Exceed common limit of 100 parameters
    response = requests.get(url, params=params)
    print(response.status_code)

def url_is_above_root_directory_test(url):
    url = url + "/../"  # Attempt to access parent directory
    response = requests.get(url)
    print(response.status_code)

def unknown_http_request_method_test(url):
    try:
        response = requests.request('UNKNOWN', url)  # Attempt to use unknown HTTP method
        print(response.status_code)
    except Exception as e:
        print(f"Unknown HTTP Request Method Test Exception: {e}")

def main_menu():
    print("Web Server HTTP Validation Test Menu")
    print("Enter '00' to quit.")
    print("1. Long Header Test")
    print("2. Long Request Test")
    print("3. Transfer Encoding Test")
    print("4. Double URL Encoding Test")
    print("5. Extremely Long HTTP Request")
    print("6. Extremely Long Parameter")
    print("7. HTTP Websocket Violation Test")
    print("8. Illegal Byte Code Character in Header Name Test")
    print("9. Illegal Byte Code Character in Header Value Test")
    print("10. Illegal Byte Code Character in Method Test")
    print("11. Illegal Byte Code Character in Parameter Name Test")
    print("12. Illegal Byte Code Character in Parameter Value Test")
    print("13. Illegal Byte Code Character in Query String Test")
    print("14. Illegal Byte Code Character in URL Test")
    print("15. Illegal Content Length Test")
    print("16. Illegal Content Type Test")
    print("17. Illegal Host Name Test")
    print("18. Illegal Parameter Encoding Test")
    print("19. Illegal URL Path Encoding Test")
    print("20. Illegal Content Encoding Test")
    print("21. Malformed HTTP Header Line Test")
    print("22. Malformed JSON Message Test")
    print("23. Malformed SOAP Message Test")
    print("24. Malformed URL Test")

def url_prompt():
    url = input("Enter the URL to test: ")
    return url

def main():
    while True:
        main_menu()
        choice = input("Choose a test: ")
        if choice == '00':
            break
        else:
            url = url_prompt()
            if choice == '1':
                long_header_test(url)
            elif choice == '2':
                long_request_test(url)
            elif choice == '3':
                transfer_encoding_test(url)
            elif choice == '4':
                double_url_encoding_test(url)
            elif choice == '5':
                extremely_long_http_request(url)
            elif choice == '6':
                extremely_long_parameter(url)
            elif choice == '7':
                http_websocket_violation_test(url)
            elif choice == '8':
                illegal_byte_code_char_in_header_name_test(url)
            elif choice == '9':
                illegal_byte_code_char_in_header_value_test(url)
            elif choice == '10':
                illegal_byte_code_char_in_method_test(url)
            elif choice == '11':
                illegal_byte_code_char_in_param_name_test(url)
            elif choice == '12':
                illegal_byte_code_char_in_param_value_test(url)
            elif choice == '13':
                illegal_byte_code_char_in_query_string_test(url)
            elif choice == '14':
                illegal_byte_code_char_in_url_test(url)
            elif choice == '15':
                illegal_content_length_test(url)
            elif choice == '16':
                illegal_content_type_test(url)
            elif choice == '17':
                illegal_host_name_test(url)
            elif choice == '18':
                illegal_parameter_encoding_test(url)
            elif choice == '19':
                illegal_url_path_encoding_test(url)
            elif choice == '20':
                illegal_content_encoding_test(url)
            elif choice == '21':
                malformed_http_header_line_test(url)
            elif choice == '22':
                malformed_json_message_test(url)
            elif choice == '23':
                malformed_soap_message_test(url)
            elif choice == '24':
                malformed_url_test(url)
