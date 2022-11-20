from __future__ import annotations

from typing import Any

from ethgreen.types.blockchain_format.program import Program


def json_to_ethgreenlisp(json_data: Any) -> Any:
    list_for_ethgreenlisp = []
    if isinstance(json_data, list):
        for value in json_data:
            list_for_ethgreenlisp.append(json_to_ethgreenlisp(value))
    else:
        if isinstance(json_data, dict):
            for key, value in json_data:
                list_for_ethgreenlisp.append((key, json_to_ethgreenlisp(value)))
        else:
            list_for_ethgreenlisp = json_data
    return Program.to(list_for_ethgreenlisp)
