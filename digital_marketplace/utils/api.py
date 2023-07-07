import json
import requests

from digital_marketplace.utils.env_variable import get_env_variable

secret_key = get_env_variable("FLUTTERWAVE_SECRET_KEY")

def verify_user_transactions(id):
    
    url = f"https://api.flutterwave.com/v3/transactions/{id}/verify"
    
    headers = {
        'Authorization': f"Bearer {secret_key}",
        "Content-Type": "application/json"
    }

    try:
        r = requests.get(
            url,
            headers=headers,
            timeout=60
        )
    except Exception as e:
        raise e

    resp = json.loads(r.text)
    return resp