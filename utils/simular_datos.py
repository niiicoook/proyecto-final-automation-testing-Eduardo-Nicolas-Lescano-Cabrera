from faker import Faker

fake = Faker()  

def get_fake_user(fakeCases = 5):

    cases = []

    for _ in range(fakeCases):
        user = fake.user_name()
        password = fake.password(length=12)
        login_bool = fake.boolean(chance_of_getting_true=40)
        cases.append((user, password, login_bool))

    return cases

