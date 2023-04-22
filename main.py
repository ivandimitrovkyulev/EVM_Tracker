from src.blockchain.evm import EvmContract
from src.variables import ankr_endpoints


chain = "polygon"
contract_address = "0x6Ef682F0223687c625E6c4a115F544a80c37dA33"
endpoint = ankr_endpoints.get(chain)

# Create EVM Contract instance to query
evm_contract = EvmContract(chain, contract_address, endpoint)

function = 'getTreasuryValue'

result = EvmContract.run_contract_function(evm_contract.contract, function, [])
print(result)
