from brownie import config, MockV3Aggregator, network, accounts
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development"]["ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet_fork", "mainnet-fork-dev"]
DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        # if we are using one of the available development chains.
        return accounts[0]
    else:
        return accounts.add(
            config["wallets"]["from_key"]
        )  # else we pull an adress that we have hardcoded in some file


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()}
        )
    print("Mocks deployed!")
