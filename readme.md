# README

## Descrição
Este script em Python conecta-se a um banco de dados Oracle, executa uma consulta SQL para gerar um relatório e exporta os dados para um arquivo Excel. Em seguida, compacta o arquivo Excel em um formato ZIP e o envia por e-mail para um destinatário especificado. Ele utiliza variáveis de ambiente para facilitar a configuração das credenciais do banco de dados e do e-mail.

## Pré-requisitos
- **Python 3.x** instalado.
- **Bibliotecas Python**: O script requer as bibliotecas `cx_Oracle`, `pandas`, `smtplib`, `zipfile`, `email.message`, `os`, e `dotenv`. Instale-as com o seguinte comando:
  ```bash
  pip install cx_Oracle pandas python-dotenv
  ```

- **Variáveis de Ambiente**:
  Crie um arquivo `.env` na mesma pasta do script e defina as seguintes variáveis de ambiente:
  ```dotenv
  USERNAME=seu_usuario
  PASSWORD=sua_senha
  DSN=host:porta/nome_servico

  EMAIL_HOST=smtp.gmail.com
  EMAIL_PORT=587
  EMAIL_HOST_USER=seu_email@gmail.com
  EMAIL_HOST_PASSWORD=sua_senha_de_app
  EMAIL_TO=destinatario@exemplo.com
  ```

## Configuração e Execução
1. **Configurar o Banco de Dados**:
   - Verifique que o Oracle Database está configurado e acessível com o DSN, usuário e senha corretos.

2. **Configurar o E-mail**:
   - Configure as credenciais de e-mail no arquivo `.env`. Certifique-se de que a conta de e-mail permite o envio com a senha do aplicativo (app password) caso necessário.

3. **Executar o Script**:
   - Execute o script no terminal:
     ```bash
     python main.py
     ```

## Estrutura do Script
1. **Conexão ao Banco de Dados**:
   - Conecta-se ao Oracle Database usando `cx_Oracle` e executa a consulta SQL, armazenando os resultados em um `DataFrame`.

2. **Geração do Relatório**:
   - Exporta o `DataFrame` para um arquivo Excel (`.xlsx`).
   - Compacta o arquivo Excel em um arquivo ZIP usando `zipfile`.

3. **Envio de E-mail com Anexo**:
   - Configura o e-mail e anexa o arquivo ZIP.
   - Envia o e-mail para o destinatário especificado.

4. **Limpeza**:
   - Remove o arquivo Excel original para liberar espaço.

## Observação
Este script foi projetado para contas de e-mail com suporte a TLS (como Gmail). Para outro provedor, ajuste `EMAIL_HOST` e `EMAIL_PORT` conforme necessário.

## Exemplo de Saída
No terminal, o script exibirá uma mensagem de sucesso:
```plaintext
Arquivo ZIP 'seu_arquivo.zip' gerado e enviado com sucesso!
```