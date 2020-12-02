from bitcoin.rpc import RawProxy

p = RawProxy()

txid = raw_input("Iveskite transakcijos ID\n")


# First, retrieve the raw transaction in hex
raw_tx = p.getrawtransaction(txid)

# Decode the transaction hex into a JSON object
decoded_tx = p.decoderawtransaction(raw_tx)

OutputValue=0

# Retrieve each of the outputs from the transaction
for output in decoded_tx['vout']:
    OutputValue+=output['value']

inputValue = 0
for output in decoded_tx['vin']:
    call_tx = p.decoderawtransaction(p.getrawtransaction(output['txid']))
    for dtx_output in call_tx['vout']:
        inputValue += dtx_output['value']

TransactionFee = inputValue - OutputValue

print("Transaction Fee:")
print(TransactionFee)
