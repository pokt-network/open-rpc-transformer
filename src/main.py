
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

        self.transform["paths"] = {}

        for method in self.spec["methods"]:
            self.transform["paths"]["/"+method["name"]] = {
                "post": {
                    "responses": {            
                        "200": {
                            "description": "Default response",
                            "content": {}
                        }},
                    "requestBody": {
                    "required": False,
                    "content": {
                        },
                    
                    }
                }
            }

    def saveSpec(self, name):
        BASE_DIR = os.path.join( os.path.dirname( __file__ ), '..' )
        json.dump( self.transform, open( name +".json", 'w' ) )

        

ors = OrsTransformer("https://raw.githubusercontent.com/pokt-foundation/open-rpc-transformer/master/ors/ethereum_mainnet.json")
ors.toOas()
ors.saveSpec("ethereum_mainnet")

#print(ors.transform)