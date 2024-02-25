import http.client
import json

#template creds - these won't work though!
username = "myuser"
password = "mypassword"

def test_connection():
    connection = http.client.HTTPSConnection('zhwwmaomc.net', timeout=2)
    print(connection)

    connection.request("GET", "/")
    response = connection.getresponse()
    print("Status: {} and reason: {}".format(response.status, response.reason))

    connection.close()

    return response.status

# this login should not work
def test_failure():
    connection = http.client.HTTPSConnection('zhwwmaomc.net', timeout=2)
    print(connection)
    headers = {'Content-type': 'application/json'}

    message = {'username': username, 'password': password}
    json_data = json.dumps(message)

    connection.request('POST', '/post', json_data, headers)

    response = connection.getresponse()
    print(response.read().decode())

    connection.close()

    return response.status

# this login should work
def test_login():
    connection = http.client.HTTPSConnection('zhwwmaomc.net', timeout=2)
    print(connection)
    headers = {'Content-type': 'application/json'}

    creds = get_credentials()

    message = {'username': creds[0], 'password': creds[1]}
    json_data = json.dumps(message)

    connection.request('POST', '/post', json_data, headers)

    response = connection.getresponse()
    print(response.read().decode())

    connection.close()

    return response.status

# add some data to website
def test_put():
    connection = http.client.HTTPSConnection('zhwwmaomc.net', timeout=2)
    print(connection)
    headers = {'Content-type': 'application/json'}

    message = {'data': "This is some test data"}
    json_data = json.dumps(message)

    connection.request('PUT', '/put', json_data, headers)

    response = connection.getresponse()
    print(response.read().decode())

    connection.close()

    return response.status

# calculate credentials for login that will actually work
def get_credentials():
    special = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')'}
    un = "test" + "user" + str(50)
    pw = "Password" + "1" + special[0]
    return [un, pw]