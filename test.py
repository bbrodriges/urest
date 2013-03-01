from urest import uREST
urest = uREST()

# testing GET
get_response = urest.get('http://google.com/')
print('GET', get_response)

# testing POST
post_response = urest.post('http://google.com/')
print('POST', post_response)
