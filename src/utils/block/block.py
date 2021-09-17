from typing import Dict


class Block:
    def __init__(self, namespace: str, chain_identifiers: Dict, action: str, identity_rating: int, metadata: Dict):
        self.namespace = namespace
        self.chain_identifiers = chain_identifiers
        self.action = action
        self.identity_rating = identity_rating
        self.metadata = metadata

    def generate_hash(self, previous_hash: str):
        pass

    def generate_token(self, previous_hash: str):
        pass
