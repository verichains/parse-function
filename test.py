from eth_abi import decode_abi
from eth_abi.codec import ABICodec

# Define the ABI encoder and decoder
abi_codec = ABICodec()

# Define the types of the input parameters as a list
types = ['uint256', {'name': 'myStruct', 'type': 'tuple', 'components': [{'name': 'myString', 'type': 'string'}, {'name': 'myBool', 'type': 'bool'}]}, 'bool']

# Define the values of the input parameters as a tuple
values = (12345, ('hello world', True), True)

# Encode the values into a byte string using the encode_abi function
encoded_data = abi_codec.encode_abi(types, values)

# Decode the byte string using the decode_abi function
decoded_data = decode_abi(types, encoded_data)

# Print the decoded data
print(decoded_data)