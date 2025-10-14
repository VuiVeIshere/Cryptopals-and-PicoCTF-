import base64
import Crypto.Util.number as bytes_to_long
string="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
bytes_string=bytes.fromhex(string)
base64_string=base64.b64encode(bytes_string)
print(base64_string.decode())
