from faker import Faker

fake = Faker()  

def get_fake_user(fakeCases = 5):

    cases = []
    usuarios_validos = ["standard_user", "locked_out_user", "problem_user"]
    contraseña_valida = "secret_sauce"

    for _ in range(fakeCases):
        if fake.boolean(chance_of_getting_true=40):
            user = fake.random_element(usuarios_validos)
            password = contraseña_valida
            login_bool = True
        else:
            user = fake.user_name()
            password = fake.password()
            login_bool = False
            
        cases.append((user, password, login_bool))

    return cases

