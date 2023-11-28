from web3.auto import Web3


class MempoolTxns:
    def __init__(self, infura_url: str) -> None:
        self.web3 = Web3(Web3.WebsocketProvider(infura_url))
        if not self.web3.is_connected():
            raise ValueError("Connection to Ethereum node Failed")
        else:
            print("Successfully connected to Ethereum node")