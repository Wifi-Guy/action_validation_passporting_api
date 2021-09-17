from typing import Any, Dict

from src.utils.identities.base import Identity


class PersistentStorage:
    def __init__(self):
        pass

    def read_action_by_id(self, _id: str):
        raise NotImplementedError()

    def read_action_by_chain_identifiers(self, identifiers: Dict[str]):
        raise NotImplementedError()

    def read_action_by_chain_identifiers_and_action(self, identifiers: Dict[str], action: str):
        raise NotImplementedError()

    def write_action(self, key: str, val: Any):
        raise NotImplementedError()

    def read_namespace(self, _id: str):
        raise NotImplementedError()

    def write_namespace(self, namespace_name: str, identity_authority_id: str):
        raise NotImplementedError()

    def read_identities(self):
        raise NotImplementedError()

    def read_identities_in_namespace(self, namespace_id: str):
        raise NotImplementedError()

    def write_identity(self, identity: Identity):
        raise NotImplementedError()

    def delete_identity(self, identity: Identity):
        raise NotImplementedError()

    def delete_chain(self, chain_id: str):
        raise NotImplementedError()
