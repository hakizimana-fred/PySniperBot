from web3.auto import Web3
import logging

logging.basicConfig(level=logging.INFO)


class MempoolTxns:
    def __init__(self, infura_url: str) -> None:
        self.web3 = Web3(Web3.WebsocketProvider(infura_url))
        if not self.web3.is_connected():
            raise ValueError("Connection to Ethereum node Failed")
        else:
            logging.info("Successfully connected to Ethereum node")

    def filter_pending_transactions(self):
        return self.web3.eth.filter('pending')
