class Account:
    all = []
    def __init__(self, name:str, email: str, password: str):
        self.name=name
        self.email = email
        self.password = password

        Account.all.append(self)

    def __repr__(self):
        return f"{self.name}('{self.email}', '{self.password}')"


spotify = Account("spotify","andres@outlook.es", "contraseña")
netflix = Account("netflix","anrnet@outlook.es", "peliculasyseries")
amazon = Account("amazon","andrescompras@outlook.es", "smszona")
youtube = Account("youtube","andresvids@outlook.es", "viraltrending")
facebook = Account("facebook","andressocial@outlook.es", "contraseñaface")
instagram = Account("instagram","andresocial@outlook.es", "contraseñainsta")

print(Account.all)

