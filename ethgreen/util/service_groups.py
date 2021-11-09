from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "ethgreen_harvester ethgreen_timelord_launcher ethgreen_timelord ethgreen_farmer ethgreen_full_node ethgreen_wallet".split(),
    "node": "ethgreen_full_node".split(),
    "harvester": "ethgreen_harvester".split(),
    "farmer": "ethgreen_harvester ethgreen_farmer ethgreen_full_node ethgreen_wallet".split(),
    "farmer-no-wallet": "ethgreen_harvester ethgreen_farmer ethgreen_full_node".split(),
    "farmer-only": "ethgreen_farmer".split(),
    "timelord": "ethgreen_timelord_launcher ethgreen_timelord ethgreen_full_node".split(),
    "timelord-only": "ethgreen_timelord".split(),
    "timelord-launcher-only": "ethgreen_timelord_launcher".split(),
    "wallet": "ethgreen_wallet ethgreen_full_node".split(),
    "wallet-only": "ethgreen_wallet".split(),
    "introducer": "ethgreen_introducer".split(),
    "simulator": "ethgreen_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
