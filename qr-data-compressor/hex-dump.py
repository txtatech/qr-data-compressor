import base64

# Assume base64_str is your base64 string
base64_str = "SGVsbG8gd29ybGQh"  # This is "Hello world!" in base64

# Decode the base64 string back into bytes
byte_data = base64.b64decode(base64_str)

# Convert the bytes to a hex string
hex_str = byte_data.hex()

print(hex_str)

