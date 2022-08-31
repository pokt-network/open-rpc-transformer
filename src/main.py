import os
import requests
import json


class OrsTransformer:
    def __init__(self, orsPath):
        self.spec = requests.get(orsPath).json()
        self.transform = {}

    def toOas(self):
        self.transform["openapi"] = "3.1.0"
        self.transform["info"] = self.spec["info"]
        self.transform["components"] = self.spec["components"]

        self.transform["paths"] = {}

        for index, method in enumerate(self.spec["methods"]):

            req_schema = {
                "title": "{}Request".format(method["name"]),
                "type": "object",
                "required": ["jsonrpc", "method", "params", "id"],
                "properties": {
                    "jsonrpc": {
                        "title": "jsonrpc version",
                        "type": "string",
                        "enum": ["2.0"],
                    },
                    "method": {
                        "title": "RPC Method Name",
                        "type": "string",
                        "enum": [method["name"]],
                    },
                    "params": {
                        "title": "Needed RPC Params",
                        "type": "array",
                        "prefixItems": [
                            {
                                k: (v if k != "title" else param["name"])
                                for k, v in param["schema"].items()
                            }
                            for param in method["params"]
                        ],
                        "minItems": len(
                            [p for p in method["params"] if p.get("required")]
                        ),
                        "maxItems": len(method["params"]),
                    },
                    "id": {"title": "RPC Request ID", "type": "integer"},
                },
            }
            self.transform["paths"]["/" + method["name"]] = {
                "post": {
                    "summary": method["summary"],
                    "operationId": method["name"],
                    "responses": {
                        "200": {
                            "description": method["result"]["name"],
                            "content": {
                                "application/json": {
                                    "schema": method["result"]["schema"]
                                    # "schema": {}
                                }
                            },
                        }
                    },
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": req_schema,
                            }
                        },
                        "description": "",
                    },
                }
            }

    def saveSpec(self, name):
        BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
        with open(name + ".json", "w") as sf:
            sf.write(json.dumps(self.transform, indent=2))


ors = OrsTransformer(
    "https://raw.githubusercontent.com/pokt-foundation/open-rpc-transformer/master/ors/ethereum_mainnet.json"
)
ors.toOas()
ors.saveSpec("ethereum_mainnet")

# print(ors.transform)
