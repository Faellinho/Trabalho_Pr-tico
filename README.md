# Trabalho_Pratico
Trabalho prático de python
Rafael Lucas do Nascimento Sales
Projeto Desenvolve - Itabira
PDita157
A melhor extensão para colar a resposta acima, especialmente se você estiver usando um editor de texto ou uma plataforma que suporte formatação de texto, é a extensão **.md** (Markdown). O Markdown é amplamente utilizado para documentação por sua simplicidade e capacidade de gerar documentos bem formatados. 

Aqui está um exemplo de como você pode formatar a resposta acima em um arquivo Markdown:

# Documento Descritivo do Projeto

## Introdução

A empresa modelada é a **Bookstore Inc.**, uma livraria que oferece uma ampla gama de livros físicos e digitais. O sistema de gerenciamento desenvolvido visa facilitar o controle de usuários e produtos, permitindo operações como adicionar, editar, remover e listar registros de forma eficiente.

### Tipos de Usuários

1. **Gerente**: Usuário com todas as permissões, incluindo gerenciamento completo de usuários e produtos.
2. **Funcionário**: Usuário com permissões para adicionar, editar e visualizar produtos, mas sem acesso para alterar registros de usuários.
3. **Cliente**: Usuário com permissão para visualizar produtos e realizar compras.

### Produtos e Serviços

A Bookstore Inc. oferece livros com os seguintes atributos:
- Nome
- Autor
- Preço
- Quantidade em estoque

## Implementação

### Usuários

#### Estrutura de Dados

Os usuários são armazenados em um dicionário, onde a chave é o `id` do usuário e o valor é outro dicionário contendo as informações do usuário (`nome`, `tipo` e `senha`).

#### Arquivo de Registro

O arquivo de registro de usuários é um arquivo CSV com a seguinte estrutura:
- `id`: Identificador único do usuário.
- `nome`: Nome do usuário.
- `tipo`: Tipo de usuário (Gerente, Funcionário, Cliente).
- `senha`: Senha para controle de acesso.

#### Funcionalidades CRUD

1. **Create**: Função para adicionar novos usuários ao sistema.
   ```python
   def adicionar_usuario(usuarios, id, nome, tipo, senha):
   ```

2. **Read**: Função para listar todos os usuários registrados.
   ```python
   def listar_usuarios(usuarios):
   ```

3. **Update**: Função para atualizar informações de um usuário existente.
   ```python
   def atualizar_usuario(usuarios, id, nome=None, tipo=None, senha=None):
   ```

4. **Delete**: Função para remover um usuário do sistema.
   ```python
   def remover_usuario(usuarios, id):
   ```

### Produtos

#### Estrutura de Dados

Os produtos são armazenados em uma lista de dicionários, onde cada dicionário contém os detalhes de um produto (`id`, `nome`, `autor`, `preco`, `quantidade`).

#### Arquivo de Registro

O arquivo de registro de produtos é um arquivo CSV com a seguinte estrutura:
- `id`: Identificador único do produto.
- `nome`: Nome do livro.
- `autor`: Autor do livro.
- `preco`: Preço do livro.
- `quantidade`: Quantidade em estoque.

#### Funcionalidades CRUD

1. **Create**: Função para adicionar novos produtos ao sistema.
   ```python
   def adicionar_produto(produtos, id, nome, autor, preco, quantidade):
   ```

2. **Read**: Função para listar todos os produtos registrados.
   ```python
   def listar_produtos(produtos):
   ```

3. **Update**: Função para atualizar informações de um produto existente.
   ```python
   def atualizar_produto(produtos, id, nome=None, autor=None, preco=None, quantidade=None):
   ```

4. **Delete**: Função para remover um produto do sistema.
   ```python
   def remover_produto(produtos, id):
   ```

#### Funcionalidades Adicionais

1. **Buscar Produto**: Função para buscar um produto específico pelo nome ou código.
   ```python
   def buscar_produto(produtos, chave):
   ```

2. **Ordenar por Nome**: Função para listar produtos ordenados por nome.
   ```python
   def ordenar_produtos_por_nome(produtos):
   ```

3. **Ordenar por Preço**: Função para listar produtos ordenados por preço.
   ```python
   def ordenar_produtos_por_preco(produtos):
   ```

## Conclusão

### Dificuldades Encontradas

As principais dificuldades encontradas foram garantir a integridade dos dados durante a leitura e escrita dos arquivos CSV e a implementação de um sistema de permissões robusto para diferentes tipos de usuários. 

### Escolhas Bem-Sucedidas

A escolha de usar dicionários para armazenar usuários e listas de dicionários para produtos foi eficaz, pois permitiu um acesso rápido e fácil aos dados, além de simplificar as operações CRUD.

### O Que Faltou Fazer

Faltou implementar uma interface gráfica para tornar o sistema mais amigável ao usuário. Além disso, a inclusão de um sistema de histórico de compras para clientes poderia agregar valor ao sistema.

### O Que Faria Diferente

No futuro, planejo modularizar o código, dividindo-o em múltiplos arquivos para melhorar a organização e a manutenção. Além disso, a implementação de testes automatizados garantiria a robustez e a confiabilidade do sistema.
