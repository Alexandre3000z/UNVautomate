# UNV Automate

Bem-vindo ao **UNV Automate**, uma aplicação desenvolvida para facilitar a configuração em lote de câmeras UNV. Esta ferramenta permite que você preencha uma planilha com os dados das câmeras (como IPs, máscaras, gateways e nomes) e automatize o processo de configuração, oferecendo uma alternativa confiável ao aplicativo oficial da fabricante, que apresentava falhas frequentes.

## Objetivo

O **UNV Automate** foi criado para resolver os problemas de confiabilidade do software oficial da UNV na configuração em lote de câmeras. Com esta aplicação, você pode:
- Configurar múltiplas câmeras de forma eficiente e segura.
- Reduzir erros manuais ao usar uma planilha Excel para entrada de dados.
- Garantir consistência nas configurações de rede, horário, OSD e áudio/vídeo.

## Funcionalidades

- **Leitura de planilha Excel**: Lê dados de câmeras (IP antigo, IP novo, máscara, gateway, nome) de um arquivo Excel.
- **Automação de configurações**: Configura automaticamente parâmetros de rede, horário, OSD e áudio/vídeo via interface web das câmeras UNV.
- **Registro de status**: Marca cada configuração como "Sim" (sucesso, com fundo verde) ou "Não" (falha, com fundo vermelho) na coluna `Concluida` do Excel.
- **Interface sem console**: Executa em modo gráfico, ideal para usuários finais.

## Pré-requisitos

Para executar o **UNV Automate**, você precisa:

- **Sistema operacional**: Windows (testado em Windows 10/11).
- **Python** (se executar o código-fonte): Versão 3.8 ou superior.
- **Dependências**:
  - Instale as bibliotecas necessárias com:
    ```bash
    pip install selenium pandas openpyxl numpy
    ```
- **ChromeDriver**: Um `chromedriver.exe` compatível com a versão do Google Chrome instalada. Você pode atualizá-lo com:
  ```bash
  pip install --upgrade chromedriver-autoinstaller
  ```
- **Google Chrome**: Navegador atualizado.
- **Planilha Excel**: Um arquivo `FonteDados.xlsx` com as colunas `IP ANTIGO`, `IP NOVO`, `MASCARA`, `GATEWAY` e `NOME`.

## Instalação

1. **Baixe o executável**:
   - Faça o download do instalador ou da pasta `UNVconfig` (disponível na seção de releases).
   - Se usar o instalador, execute-o e siga as instruções para instalar o programa.

2. **Prepare a planilha**:
   - Crie um arquivo `FonteDados.xlsx` com as colunas:
     ```
     | IP ANTIGO | IP NOVO | MASCARA | GATEWAY | NOME |
     ```
   - Exemplo:
     ```
     | 192.168.1.1 | 192.168.1.2 | 255.255.255.0 | 192.168.1.254 | Cam1 |
     | 192.168.1.3 | 192.168.1.4 | 255.255.255.0 | 192.168.1.254 | Cam2 |
     ```
   - Coloque o arquivo na mesma pasta do executável ou especifique o caminho correto.

3. **Execute o programa**:
   - Abra a pasta `UNVconfig` e execute `UNVconfig.exe`.
   - O programa lerá a planilha, configurará as câmeras e atualizará a coluna `Concluida` no Excel.

## Como usar

1. **Preencha a planilha**:
   - Insira os dados das câmeras no arquivo `FonteDados.xlsx`.
   - Certifique-se de que os IPs em `IP ANTIGO` são acessíveis e que o ChromeDriver está atualizado.

2. **Execute o UNV Automate**:
   - Clique duas vezes em `UNVconfig.exe`.
   - O programa acessará cada câmera via `IP ANTIGO`, aplicará as configurações (IP novo, máscara, gateway, nome, etc.) e marcará o status na coluna `Concluida`.

3. **Verifique os resultados**:
   - Abra o `FonteDados.xlsx` após a execução.
   - A coluna `Concluida` mostrará:
     - **Sim** (fundo verde): Configuração bem-sucedida.
     - **Não** (fundo vermelho): Falha na configuração.

## Solução de problemas

- **Erro "No module named 'numpy'"**:
  - Certifique-se de que o `numpy` está instalado:
    ```bash
    pip install numpy
    ```
  - Se usar o código-fonte, adicione `import numpy` no início do `index.py`.

- **Executável sinalizado como vírus**:
  - O Windows Defender ou outros antivírus podem sinalizar o `UNVconfig.exe` como falso positivo.
  - Adicione uma exclusão temporária no Windows Defender:
    - Configurações > Segurança do Windows > Proteção contra vírus > Gerenciar configurações > Adicionar exclusão > Selecione a pasta do programa.
  - Envie o executável para análise em `https://www.microsoft.com/en-us/wdsi/filesubmission`.

- **Erro de conexão com IPs**:
  - Verifique se os IPs em `IP ANTIGO` são válidos e acessíveis.
  - Teste manualmente no Chrome (ex.: `http://192.168.1.1`).
  - Se as câmeras usam uma porta específica, ajuste o código em `index.py`:
    ```python
    url = f"http://{ipAntigo}:8080"  # Substitua pela porta correta
    ```

- **Erro de elemento não encontrado**:
  - Os XPaths no código (ex.: `//*[@id="banner"]`) podem variar entre modelos de câmeras UNV. Inspecione a interface web da câmera com o Chrome DevTools para confirmar os XPaths.

## Desenvolvimento

O **UNV Automate** foi desenvolvido com:
- **Python**: Para lógica de automação.
- **Selenium**: Para interagir com a interface web das câmeras.
- **Pandas e Openpyxl**: Para manipulação de planilhas Excel.
- **PyInstaller**: Para gerar o executável.

Se você deseja contribuir ou modificar o código:
1. Clone o repositório (se disponível).
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Edite o `index.py` ou os arquivos em `config/` e `services/`.
4. Recompile o executável:
   ```bash
   pyinstaller --clean build.spec
   ```

## Contato

Para suporte ou sugestões, entre em contato com o desenvolvedor:
- **E-mail**: joaoalexandrems.profissional@gmail.com



---

Desenvolvido com ❤️ para facilitar a configuração de câmeras UNV.