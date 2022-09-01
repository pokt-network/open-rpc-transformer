import os
import requests
import json

from .example_params import ParamEx


class OrsTransformer:
    def __init__(self, orsPath):
        self.spec = requests.get(orsPath).json()
        self.transform = {}

    def toOas(self):
        self.transform["openapi"] = "3.1.0"
        self.transform["info"] = self.spec["info"]
        self.transform["components"] = self.spec["components"]

        self.transform["paths"] = {}

        for method in self.spec["methods"]:
            req_ex = getattr(ParamEx, method["name"], ParamEx.empty).value
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
            resp_schema = {
                "title": "{}Response".format(method["name"]),
                "type": "object",
                "properties": {
                    "id": {"title": "RPC Request ID", "type": "integer"},
                    "jsonrpc": {
                        "title": "jsonrpc version",
                        "type": "string",
                        "enum": ["2.0"],
                    },
                    "result": method["result"]["schema"],
                },
            }
            self.transform["paths"]["/" + method["name"]] = {
                "post": {
                    "summary": method["name"],
                    "description": (
                        method["summary"] + "\n" + method.get("description", "")
                    ).strip(),
                    "operationId": method["name"],
                    "responses": {
                        "200": {
                            "description": method["result"]["name"],
                            "content": {"application/json": {"schema": resp_schema}},
                        }
                    },
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": req_schema,
                                "example": {
                                    "jsonrpc": "2.0",
                                    "method": method["name"],
                                    "params": req_ex,
                                    "id": 0,
                                },
                            }
                        },
                    },
                }
            }

    def saveSpec(self, name):
        with open(name + ".json", "w") as sf:
            sf.write(json.dumps(self.transform, indent=2))


ors = OrsTransformer(
    "https://raw.githubusercontent.com/pokt-foundation/open-rpc-transformer/master/ors/ethereum_mainnet.json"
)
ors.toOas()
ors.saveSpec("ethereum_mainnet")

# print(ors.transform)
