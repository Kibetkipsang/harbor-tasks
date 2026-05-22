from auth import generate_token, verify_token

token = generate_token("alice")

print(verify_token(token))