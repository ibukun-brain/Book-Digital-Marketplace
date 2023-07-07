import hashlib
from digital_marketplace.utils.env_variable import get_env_variable

secretKey = get_env_variable('FLUTTERWAVE_SECRET_KEY')
publicKey = get_env_variable('FLUTTERWAVE_PUBLIC_KEY')

data = {
    # enter your request payload here
}

def shaEncryption(input):
    encoded_bytes = input.encode()
    sha256 = hashlib.sha256()
    sha256.update(encoded_bytes)
    encryptedString = sha256.hexdigest()
    return encryptedString

# hashedSecretKey = shaEncryption(secretKey)
# StringToBeHashed = str(data["amount"]) + data["currency"] + data["customer"]["email"] + data["tx_ref"] + hashedSecretKey
# payload_hash = shaEncryption(StringToBeHashed)
# print(payload_hash)