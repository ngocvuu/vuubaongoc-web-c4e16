from models.service import Service
import mlab


mlab.connect()
# Find id
services = Service.objects.get(id = "5ac0947b932f1b05975ec33d")
# Delete id
services_del = services.delete()
