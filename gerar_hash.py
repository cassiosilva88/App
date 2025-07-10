import streamlit_authenticator as stauth

# Substitua pelos seus valores
usernames = ['cassio', 'maria']
senhas = ['12345', 'senha123']

hashes = stauth.Hasher(senhas).generate()

for user, hashed in zip(usernames, hashes):
    print(f"{user}: {hashed}")
