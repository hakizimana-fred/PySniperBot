from web3.auto import Web3
import logging
import asyncio

logging.basicConfig(level=logging.INFO)


class MempoolTxns:
    def __init__(self, infura_url: str) -> None:
        self.web3 = Web3(Web3.WebsocketProvider(infura_url))
        if not self.web3.is_connected():
            raise ValueError("Connection to Ethereum node Failed")
        else:
            logging.info("Successfully connected to Ethereum node")

    def handle_event(self, event):
        try:
            transaction = self.web3.to_json(event).strip('')
            print(transaction)
        except Exception as e:
            print(f"Something went wrong: {e}")

    async def log_loop(self, event_filter, poll_interval):
        while True:
            for event in event_filter.get_new_entries():
                self.handle_event(event)
                await asyncio.sleep(poll_interval)

    def filter_pending_transactions(self):
        txt_filter = self.web3.eth.filter('pending')
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(
                asyncio.gather(
                    self.log_loop(txt_filter, 2)
                )
            )
        finally:
            loop.close()
