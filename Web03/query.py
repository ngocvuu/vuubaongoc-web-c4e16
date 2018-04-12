from models.service import Service
import mlab

mlab.connect()

all_services = Service.objects()
#
# print(all_services[10].name)
# id_to_find = "5ac08c1e932f1b04f700d6af"

# kieu_anh = Service.objects.get(id = id_to_find)
# kieu_anh = Service.objects.with_id()
# print(kieu_anh.phone)

# del_all_ser = all_services.delete()
all_customers = Customer.objects()

all_orders = Order.objects()
