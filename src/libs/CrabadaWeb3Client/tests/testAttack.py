from typing import cast

from hexbytes import HexBytes
from src.libs.Web3Client.exceptions import Web3ClientException
from src.libs.Web3Client.helpers.debug import printTxInfo
from src.helpers.general import fourthOrNone, secondOrNone, thirdOrNone
from src.common.config import nodeUri, users
from src.libs.CrabadaWeb3Client.CrabadaWeb3Client import CrabadaWeb3Client
from sys import argv
from web3.exceptions import ContractLogicError

# VARS
client = CrabadaWeb3Client(nodeUri=nodeUri, privateKey=users[0]["privateKey"])

teamId = users[0]["teams"][0]["id"]
mineId = int(secondOrNone(argv) or 0)
expiredTime = int(thirdOrNone(argv) or 0)
certificate = HexBytes(fourthOrNone(argv))

if not (mineId and expiredTime and certificate):
    print("Specify 3 non-zero arguments: mineId, expiredTime and certificate")
    exit(1)

# TEST FUNCTIONS
def test() -> None:
    txHash = client.attack(mineId, teamId, expiredTime, certificate)
    printTxInfo(client, txHash)


# EXECUTE
try:
    test()
except ContractLogicError as e:
    print(">>> CONTRACT EXCEPTION!")
    print(e)
except Web3ClientException as e:
    print(">>> CLIENT EXCEPTION!")
    print(e)
