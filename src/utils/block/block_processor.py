from src.utils.block import Block
from src.utils.persistent_storage import factory as persistent_storage


class BlockProcessor:
    def __init__(self):
        pass

    def discover_chain(self, block: Block):
        persistent_storage().read_action_by_chain_identifiers(block.chain_identifiers)

    def write(self):
        pass

    def create_block(self):
        pass

    def get_previous_block(self):
        pass
