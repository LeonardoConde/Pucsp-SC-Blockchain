from typing import Any
from boa3.builtin import public
from boa3.builtin.interop import storage

@public
def _deploy(data: Any, is_updating: bool):
    storage.put('memória', 'Hello World')
    
@public
def set_information(info: str):
    storage.put('memória', info)
    
@public
def get_information() -> str:
    return storage.get('memória').to_str()