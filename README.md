# open-rpc-transformer
Transform OpenRPC Spec to OpenApi Format


## Requirements

```
pip install requests
````

## Usage

To generate spec files.

```
python -m src.main
```

Spec files will be output to `/specs`.


To add a new chain to generate the spec for a new chain,
go to `src/params/relay_chains.py`, add a new `Params`
object for that chain:

```python
NewChainParams = Params(
    send_address="" #hex string of a account,
    contract_address="" #hex string of a smart contract,
    block_hash="" #hex string of a block hash,
    call_data="" #hex string of data passed to eth_call, sent to contract_address, from send_address,
    transaction_hash="" #hex string of transaction,
    topic="" #hex string of topic used in eth_getLogs,
)
```

and then add it to the `param_map` dictionary at the bottom of the module, with
the key representing what the output spec file will be saved as.


