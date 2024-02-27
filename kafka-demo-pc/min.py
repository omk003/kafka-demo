import json
from kafka import KafkaProducer
from faker import Faker
from pizzaproducer import PizzaProvider
fake = Faker()
fake.add_provider(PizzaProvider)


folderName = "./"

producer = KafkaProducer(
    bootstrap_servers = "XXXXXXXXXXXXXXX",
    security_protocol = "SSL",
    ssl_cafile = folderName+ "ca.pem",
    ssl_certfile = folderName+"service.cert",
    ssl_keyfile = folderName+"service.key",
    value_serializer = lambda v: json.dumps(v).encode('ascii'),
    key_serializer = lambda v: json.dumps(v).encode('ascii')
)
for i in range(1000):
    producer.send(
        "test_topic",
        key={"key": 1},
        value = {"message": fake.name(),
                 "address": fake.address(),
                 "phone_number": fake.phone_number(),
                 "order": fake.pizza_name()}
    )
    producer.flush()

# producer.send(
#         "test_topic",
#         key={"key": 1},
#         value = {"message": "hello"}
# )
