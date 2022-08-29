import os
import requests
import json


class OrsTransformer:
    def __init__(self, orsPath):
        self.spec = requests.get(orsPath).json()
        self.transform = {}

    def toOas(self):
        self.transform["openapi"] = "3.0.0"
        self.transform["info"] = self.spec["info"]
        self.transform["components"] = self.spec["components"]

        self.transform["paths"] = {}

        for method in self.spec["methods"]:
            self.transform["paths"]["/" + method["name"]] = (
                {
                    "post": {
                        "operationId": method["name"],
                        "responses": {
                            "200": {
                                "description": method["result"]["name"],
                                "content": {
                                    "application/json": {
                                        "schema": method["result"]["schema"]
                                    }
                                },
                            }
                        },
                    }
                },
            )
            requestSchema = {
                "description": "{} Request".format(method["name"]),
                "required": True,
                "content": {"application/json": {"schema" : {"title" : "{}Request".format(method["name"]}}},
            }
            schemas = [param for param in method["params"]]


    def saveSpec(self, name):
        BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
        with open(name + ".json", "w") as f:
            json.dump(self.transform, f)


ors = OrsTransformer(
    "https://raw.githubusercontent.com/pokt-foundation/open-rpc-transformer/master/ors/ethereum_mainnet.json"
)
ors.toOas()
ors.saveSpec("ethereum_mainnet")

# print(ors.transform)
