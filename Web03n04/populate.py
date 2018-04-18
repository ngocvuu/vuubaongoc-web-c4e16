from models.service import Service
import mlab
from random import randint, choice
from faker import Faker


mlab.connect()

fake = Faker()

# Create a document
for i in range(30):
    print("Saving service", i + 1, "........")
    new_service = Service(name=fake.name(),
                            yob=randint(1995,2000),
                            gender=randint(0,1),
                            height=randint(150,180),
                            phone=fake.phone_number(),
                            address=fake.address(),
                            status=choice([True,False]),
                            image= choice(["https://images.kienthuc.net.vn/zoomh/500/uploaded/bientapkienthuc/2016_12_09/Son9-12/NewFolder4/su-that-phia-sau-co-gai-viet-xinh-dep-van-nguoi-me.jpg","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_C9pBOkPDGENQ4pZ-BEgLCnvVTEoAHeFCzmcO7QqH58hmeYLY","https://kenh14cdn.com/thumb_w/660/2017/screen-shot-2017-06-20-at-11-39-57-pm-1497978081743.png"]),
                            description= choice(["ngoan hiền", "dễ thương", "vô tư", "ngây thơ"]),
                            measurements= [randint(80,100),randint(50,70),randint(80,100)],
                            )
    new_service.save()

# print(fake.address())
