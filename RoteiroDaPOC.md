# POC - Smart Contract
## Requisitos
- Visual Studio Code;
- Python 3.7 ou uma versão mais atual.

Após instalar os requisitos acima também será necessário instalar:
- A extensão [Neo Blockchain Toolkit](https://marketplace.visualstudio.com/items?itemName=ngd-seattle.neo-blockchain-toolkit) para o VS Code;
- O package [neo3-boa](https://github.com/CityOfZion/neo3-boa#quickstart) no Python:
    - Abrir o terminar;
    - Use:
        - ``python -m venv venv`` para criar um ambiente virtual para python;
        - ``venv\Scripts\activate.bat`` para ligar o ambiente;
        - ``pip install neo3-boa`` para instalar a ferramenta de desenvolvimento de *Smart Contracts*;



## Desenvolvendo o *smart contract*
Crie um arquivo python, ele será o contrato que iremos desenvolver. A blockchain Neo utiliza código compilado, por isso, diferente do Python, será necessário especificar o tipo dos parametros de entrada e saída. Dentro do contrato, escreva o código abaixo:
```python
from typing import Any
from boa3.builtin import public
from boa3.builtin.interop import storage

@public
def _deploy(data: Any, is_updating: bool):
    pass
    
@public
def set_information(info: string):
    pass
    
@public
def get_information() -> string:
    pass
```
Serão usados apenas esses três metódos neste contrato, o método `_deploy` será executado quando o contrato for publicado na blockchain, os outros dois serão usados para ler uma informação que está guardada na blockchain e a para modificar essa informação.

Acima dos métodos existe o decorator `@public` que indica que o método pode ser chamado por qualquer usuário, métodos sem esse decorator não podem ser invocados.

> Os imports relacionados a blockchain começarão com o caminho `boa3.builtin`.

### Funções

#### _deploy
Neste método, quando o contrato for divulgado na blockchain, a string `Hello World` será armazenada na chave `memória`.
```python
@public
def _deploy(data: Any, is_updating: bool):
    storage.put('memória', 'Hello World')
```

compilar
## Criando uma rede local
criar no vscode
## Criar conta e dar dinheiros
## Testando o *smart contract*
Fazer um invoke com o vscode
talvez explicar os witness scopes
## (Opcional) fazer deploy na TestNet/MainNet ????
Não sei se precisa