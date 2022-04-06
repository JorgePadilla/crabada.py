from typing import Literal, NewType, TypedDict, List
from eth_typing import Address
from web3.types import Wei

Tus = NewType("Tus", float)

"""
Task assigned to a team
"""
TeamTask = Literal["loot", "mine"]


class ConfigTeam(TypedDict):
    id: int
    userAddress: Address
    battlePoints: int
    task: TeamTask
    lootStrategies: List[str]
    reinforceStrategies: List[str]
    reinforcementToPick: int


class ConfigUser(TypedDict):
    address: Address
    privateKey: str
    reinforcementMaxPriceInTus: Tus
    reinforcementMaxPriceInTusWei: Wei
    reinforcementMaxGasInGwei: float
    teams: List[ConfigTeam]


class ConfigContract(TypedDict):
    address: Address
    abi: str
