import enum


class ParamEx(enum.Enum):
    empty = []
    eth_getBalance = ["0x407d73d8a49eeb85d32cf465507dd71d507100c1", "latest"]
    eth_getStorageAt = ["0x295a70b2de5e3953354a6a8344e616ed314d7251", "0x0", "latest"]
    eth_getTransactionCount = ["0x407d73d8a49eeb85d32cf465507dd71d507100c1", "latest"]
    eth_getBlockTransactionCountByHash = [
        "0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238"
    ]
    eth_getBlockTransactionCountByNumber = ["latest"]
    eth_getUncleCountByBlockHash = [
        "0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238"
    ]
    eth_getUncleCountByBlockNumber = ["latest"]
    eth_getCode = ["0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b", "latest"]
    eth_sendRawTransaction = [
        "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
    ]
    eth_call = [
        {"to": "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D", "data": "0x18160ddd"},
        "latest",
    ]
    eth_estimateGas = [
        {
            "to": "0x1c8F6A5F009E051CaB9C3851ca2DA2c936b2775A",
            "from": "0xA69babEF1cA67A37Ffaf7a485DfFF3382056e78C",
        },
        "latest",
    ]
    eth_getBlockByHash = [
        "0x43ce3845655d926e5a2ba97c80b26081fec496078e4974ce28564f62f1d91741",
        False,
    ]
    eth_getBlockByNumber = ["latest", False]
    eth_getTransactionByHash = [
        "0x88df016429689c079f3b2f6ad39fa052532c56795b733da78a91ebe6a713944b"
    ]
    eth_getTransactionByBlockHashAndIndex = [
        "0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331",
        "0x0",
    ]
    eth_getTransactionByBlockNumberAndIndex = ["latest", "0x0"]
    eth_getTransactionReceipt = [
        "0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238"
    ]
    eth_getUnlceByBlockHashAndIndex = [
        "0xc6ef2fc5426d6ad6fd9e2a26abeab0aa2411b7ab17f30a99d3cb96aed1d1055b",
        "0x0",
    ]
    eth_getUnlceByBlockNumberAndIndex = ["latest", "0x0"]
    eth_getLogs = [
        {
            "topics": [
                "0x000000000000000000000000a94f5374fce5edbc8e2a8697c15331677e6ebf0b",
            ],
        }
    ]
    web3_sha3 = ["0x68656c6c6f20776f726c64"]
