from typing import Union


class Params:
    def __init__(
        self,
        send_address: str,
        contract_address: str,
        block_hash: str,
        call_data: str,
        transaction_hash: str,
        topic: str,
    ):
        self.send_address = send_address
        self.contract_address = contract_address
        self.block_hash = block_hash
        self.call_data = call_data
        self.transaction_hash = transaction_hash
        self.topic = topic

    @property
    def empty(self) -> list:
        return []

    @property
    def eth_getBalance(self) -> list[str]:
        return [self.contract_address, "latest"]

    @property
    def eth_getStorageAt(self) -> list[str]:
        return [self.contract_address, "0x0", "latest"]

    @property
    def eth_getTransactionCount(self) -> list[str]:
        return [self.contract_address, "latest"]

    @property
    def eth_getBlockTransactionCountByHash(self) -> list[str]:
        return [self.block_hash]

    @property
    def eth_getBlockTransactionCountByNumber(self) -> list[str]:
        return ["latest"]

    @property
    def eth_getUncleCountByBlockHash(self) -> list[str]:
        return [self.block_hash]

    @property
    def eth_getCode(self) -> list[str]:
        return [self.contract_address, "latest"]

    @property
    def eth_sendRawTransaction(self) -> list[str]:
        return [
            "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
        ]

    @property
    def eth_call(self) -> list[Union[dict[str, str], str]]:
        return [{"to": self.contract_address, "data": self.call_data}, "latest"]

    @property
    def eth_estimateGas(self) -> list[Union[dict[str, str], str]]:
        return [{"to": self.contract_address, "from": self.send_address}, "latest"]

    @property
    def eth_getBlockByHash(self) -> list[Union[str, bool]]:
        return [self.block_hash, False]

    @property
    def eth_getBlockByNumber(self) -> list[Union[str, bool]]:
        return ["latest", False]

    @property
    def eth_getTransactionByHash(self) -> list[str]:
        return [self.transaction_hash]

    @property
    def eth_getTransactionByBlockHashAndIndex(self) -> list[str]:
        return [self.block_hash, "0x0"]

    @property
    def eth_getTransactionByBlockNumberAndIndex(self) -> list[str]:
        return ["latest", "0x0"]

    @property
    def eth_getTransactionReceipt(self) -> list[str]:
        return [self.transaction_hash]

    @property
    def eth_getUncleByBlockHashAndIndex(self) -> list[str]:
        return [self.block_hash, "0x0"]

    @property
    def eth_getUncleByBlockNumberAndIndex(self) -> list[str]:
        return ["latest", "0x0"]

    @property
    def eth_getLogs(self) -> list[dict[str, list[str]]]:
        return [{"topics": [self.topic]}]
