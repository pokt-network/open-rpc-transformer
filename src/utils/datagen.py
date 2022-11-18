from web3 import Web3

PROVIDER_URL = "https://eth-mainnet.gateway.pokt.network/v1/lb/c2371aeb367681b4d6febd87"
TOKEN_CONTRACT_ADDRESS = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

params = {
    "send_address": "",
    "contract_address": "",
    "block_hash": "",
    "call_data": "",
    "transaction_hash": "",
    "topic": "",
}

params.update({"contract_address": TOKEN_CONTRACT_ADDRESS})

# Reduced ERC-20 ABI, only Transfer event
ABI = """[
        {
            "anonymous": false,
            "inputs": [
                {
                    "indexed": true,
                    "name": "from",
                    "type": "address"
                },
                {
                    "indexed": true,
                    "name": "to",
                    "type": "address"
                },
                {
                    "indexed": false,
                    "name": "value",
                    "type": "uint256"
                }
            ],
            "name": "Transfer",
            "type": "event"
        }
    ]
"""

w3 = Web3(Web3.HTTPProvider(PROVIDER_URL))

latest_block = w3.eth.get_block("latest")
print(latest_block.number)

# event_filter = w3.eth.filter({"address": TOKEN_CONTRACT_ADDRESS})

# myfilter = tokenContract.eventFilter('Transfer', {'fromBlock': latest_block.number - 10,'toBlock': 'latest'});
# eventlist = myfilter.get_all_entries()

contract = w3.eth.contract(
    address=Web3.toChecksumAddress(TOKEN_CONTRACT_ADDRESS), abi=ABI
)
events = contract.events.Transfer.getLogs(fromBlock=latest_block.number - 2)

print("==============")

print("Event: ")
print(events[0])

print("==============")

txnHash = events[0]["transactionHash"].hex()
print("Txn Hash")
print(txnHash)
params.update({"transaction_hash": txnHash})

print("==============")

txn = w3.eth.get_transaction(txnHash)
print("Txn Details")
print(txn)

print("==============")

call_data = txn["input"]
print("Input Call Data")
print(call_data)
params.update({"call_data": call_data})

print("==============")

receipt = w3.eth.get_transaction_receipt(txnHash)
print("Txn Receipt")
print(receipt)

print("==============")

blockHash = receipt["blockHash"].hex()
print("Block Hash")
print(blockHash)
params.update({"block_hash": blockHash})

print("==============")

to = receipt["to"]
print("To Address")
print(to)
params.update({"send_address": to})

print("==============")

topic = receipt["logs"][0]["topics"][0].hex()
print("Topic")
print(topic)
params.update({"topic": topic})

print("==============")

print("Final")
print(params)

if __name__ == "__main__":
    print("CLI")
