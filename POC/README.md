# POC - Smart Contract na N3
## Requisitos
- [Visual Studio Code](https://code.visualstudio.com/);
- [Python](https://www.python.org/downloads/) 3.7 ou uma versão mais atual.

Após instalar os requisitos acima também será necessário instalar:
- A extensão [Neo Blockchain Toolkit](https://marketplace.visualstudio.com/items?itemName=ngd-seattle.neo-blockchain-toolkit) para o VS Code;
- [DotNet](https://dotnet.microsoft.com/en-us/download) versão 5 ou mais atualizada;
- O package [neo3-boa](https://github.com/CityOfZion/neo3-boa) no Python:
    - Abrir o terminal no diretório do projeto (No Powershell nem sempre roda);
    - Use no terminal:
        - Para criar um ambiente virtual para python:
            ```sh
            python -m venv venv
            ```
        - Para ligar o ambiente (no Windows):
            ```sh
            venv\Scripts\activate.bat
            ```
        - Para instalar a ferramenta de desenvolvimento de *Smart Contracts*:
            ```sh
            pip install neo3-boa
            ```

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
def set_information(info: str):
    pass
    
@public
def get_information() -> str:
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
#### set_information
Esse método é apenas um exemplo de como se modifica um dado na blockchain:

```python
@public
def set_information(info: str):
    storage.put('memória', info)
```
A blockchain não aceita objetos, então, caso você precise salvar um objeto é necessário [serializar].(https://dojo.coz.io/neo3/boa/boa3/builtin/nativecontract/boa3-builtin-nativecontract-stdlib.html)

#### get_information
Esse método é apenas um exemplo de como se lê um dado na blockchain:

```python
@public
def get_information() -> str:
    return storage.get('memória').to_str()
```


### Compilação
Antes de publicar o **Smart Contract** é preciso compilar ele. Caso você tenha instalado o package do neo3-boa na venv é necessário que ela esteja ativa Os arquivos que são importados para os contratos não precisam ser compilados, apenas o contrato em si. Para compilar o contrato use o comando abaixo no terminal:
```sh
neo3-boa <nome-do-arquivo>.py
```
Caso o arquivo não esteja no mesmo diretório que o terminal, é possivel compilar passando o caminho do arquivo:
```sh
neo3-boa <caminho-do-arquivo>.py
```
![Compilação](/POC/doc-images/exemplo-de-compilacao.png "Compilação")

Após executado, 2 arquivos com o mesmo nome do arquivo serão gerados, um com extensão ``.manifest.json`` e o outro com ``.nef``. O arquivo de extensão ``.manifest.json`` é o arquivo que que contém as informações do contrato e as assinaturas dos métodos públicos do contrato compilado, enquanto o de extensão ``.nef`` é o arquivo do contrato em bytes. Caso precise recompilar, não há necessidade de apagá-los, o compilador já sobrescreve os arquivos.

### Tipos de rede
A publicação é quando um contrato é registrado na blockchain e liberado para outros usuários usarem. A rede da Neo permite que um contrato seja publicado em 3 tipos de rede:

- Privada (localmente): <br>
  Serve para fazer teste locais e [debuggar](https://github.com/neo-project/neo-debugger) se necessário. Para debuggar o contratos compilados com o neo3-boa é necessário adicionar a [flag](https://github.com/CityOfZion/neo3-boa#configuring-the-debugger) `-d` ou `--debug` durante a compilação;
> OBS: Uma [flag](https://www.ibm.com/docs/en/aix/7.1?topic=names-command-flags) é uma operação que altera um comando.
- TestNet:  <br>
  Serve fazer testes em um ambiente próximo ao ambiente de produção, na qual pode ser testada de diversos lugares.
- MainNet:  <br>
  É a rede oficial da Neo.

> OBS 2: Caso queira aprender como usar o debugger da Neo, existe um [tutorial](https://ngdenterprise.com/neo-tutorials/quickstart5.html) em inglês só para isso. 

### Criando uma rede local:
Neste tópico iremos ensinar como criar uma rede privada. Tendo a extensão da Neo para Visual Studio Code instalada:
- Clique nela e espere carregar; 

![Sidebar VSCode](/POC/doc-images/sidebar-vscode.png "Sidebar VSCode")
- Abra a aba `QUICK START`;
- Clique no botão `Create a new Neo Express Instance` e selecione a opção de 1 nó;
  - Caso não apareça o botão, clique na reticências da aba `BLOCKCHAINS` e clique no botão `Create private blockchain`;
- Abrirá uma janela de salvar arquivos, salve-o e a rede irá iniciar automaticamente;

Caso queira desligar a rede, procure na aba `BLOCKCHAINS` a rede terminada com `.neo-express`, clique com o botão direito e clique em `Stop blockchain`. Para iniciar novamente, clique no botão `Start Neo Express` localizado na aba `QUICK START` ou procure na aba `BLOCKCHAIN` a rede terminada com `.neo-express`, clique com o botão direito e clique em `Start blockchain`.

### Criando uma conta e recebendo fundos:
Para criar um contrato, antes é necessário criar uma wallet (carteira digital). A blockchain da Neo usa primariamente 2 tipos de tokens, o NEO e o GAS. Para cada método que modifica algo na blockchain da Neo é cobrado uma taxa em GAS.
#### Rede privada
  Na aba `BLOCKCHAINS`: 
- Clique com o botão direito na rede terminada com `.neo-express`;
- Clique em `Create wallet`;
- Dê um nome para a carteira.

Para dar fundos a uma carteira na rede privada, na aba `BLOCKCHAINS`:
- Clique com o botão direito na rede terminada com `.neo-express`;
- Clique em `Transfer assets`;
- Selecione o token;
- Digite um valor para transferir;
- Selecione a carteira de quem será enviado;
- Selecione a carteira de quem irá receber.

#### Rede TestNet e/ou MainNet

Existem várias wallets compatíveis com a blockchain da Neo 3, nós recomendamos a [Neon Wallet](https://neonwallet.com/). Para pegar fundos na TestNet, você pode usar [esse site]( https://n3t5wish.ngd.network). Já para ter fundos a MainNet, é preciso comprar fundos.

### Publicando o contrato
Nesse tutorial iremos publicar apenas na rede privada por questões de tempo. Então tendo compilado o contrato, transfira da carteira genesis (o primeiro nó da blockchain) 100 GAS para a carteira que você criou. Após isso na aba `QUICK START`:
- Clique no botão `Deploy a contract`;
- Selecione a carteira na qual quer atrelar ao contrato;
- Selecione o arquivo de extensão `.nef` do contrato;
Pronto, seu contrato está publicado na rede local.

Para publicar na TestNet e MainNet, o processo de publicação é igual para qualquer linguagem de programação, ou seja, é possivel seguir a [documentação oficial](https://docs.neo.org/docs/en-us/develop/network/testnet.html).

### Usando o contrato
Para usar o contrato é preciso "invocar" ele. Para isso, na aba `QUICK START`:
- Clique em `Invoke a contract`;
- Escolha a rede que deseja, no caso desse tutorial é a rede terminada em `.neo-express`;
- Selecione o contrato o seu contrato;
- Digite no campo `Operation` o nome do método a ser usado;
- Inclua os parâmetros, caso tenha, na seção `Arguments`, caso sua função tenha mais de um parâmetro, de um clique na janela aberta e irá aparecer um novo campo para adicionar o próximo argumento;

![Exemplo Chamada Get](/POC/doc-images/exemplo-chamada-de-metodo-get.png "Exemplo Chamada Get")

![Exemplo Chamada Set](/POC/doc-images/exemplo-chamada-de-metodo.png "Exemplo Chamada Set")

- Clique em `Run this step`;
- Escolha a wallet que usará o contrato;
- Escolha de que modo chamará o contrato:
  - CalledByEntry: Esse modo é para escrita e possui custo ao ser usado, essa opção serve para assinar apenas a primeira chamada ao contrato;
  - Global: Esse modo é para escrita e possui custo ao ser usado, ao contrario do CalledByEntry, se outro contrato for chamado durante a invocação, a assinatura será usada novamente;
  - None: Esse modo é só para leitura da blockchain e não possui custo ao ser usado.

Espere um pouco e pronto! Você usou o contrato que você publicou! Irá aparecer uma janela de histórico de usos da blockchain, é possivel clicar em cada uso e ver as informações que ele carrega.

![Exemplo Info Chamada](/POC/doc-images/exemplo-info-chamada.png "Exemplo Info Chamada")

Os métodos dos contratos que são publicados na TestNet e/ou MainNet podem ser conferidos por indexadores de blocos, como o [Neo Dora](https://dora.coz.io/contracts)