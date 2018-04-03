from models.customers import Customers
import mlab

mlab.connect()

all_customers = Customers.objects()
