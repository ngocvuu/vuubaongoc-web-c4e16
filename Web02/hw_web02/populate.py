from models.customers import Customers
import mlab
from random import randint,choice
from faker import Faker

mlab.connect()

fake = Faker()


# Create documents
for i in range(50):
    print("Saving customers ", i+1, "........")
    new_customer = Customers( name = fake.name(),
                                gender = randint(0,1),
                                email = fake.company_email(),
                                phone = fake.phone_number(),
                                job = fake.job(),
                                company = fake.company(),
                                contacted = choice([True,False])
                                )
    new_customer.save()
