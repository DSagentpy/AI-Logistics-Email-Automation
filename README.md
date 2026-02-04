# 📦 Sistema de Extração Inteligente de Dados Logísticos

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-purple.svg)
![Gmail API](https://img.shields.io/badge/Gmail-API-red.svg)

**Automatize a extração de informações de emails logísticos com Inteligência Artificial**

[Funcionalidades](#-funcionalidades) • [Instalação](#-instalação) • [Uso](#-como-usar) • [Tecnologias](#-tecnologias)

</div>

---

## 🎯 Sobre o Projeto

Sistema automatizado que utiliza **Inteligência Artificial** para extrair informações estruturadas de emails relacionados à logística e programação de entregas. Desenvolvido para otimizar processos operacionais, reduzir erros manuais e acelerar o processamento de informações críticas em operações logísticas.

### 💡 Problema que Resolve

Em ambientes logísticos, profissionais recebem diariamente dezenas de emails contendo informações sobre:
- Materiais a serem entregues
- Volumes e quantidades
- Datas e horários de programação
- Instruções de entrega

Processar essas informações manualmente é **lento, propenso a erros** e consome tempo valioso que poderia ser dedicado a atividades estratégicas.

### ✨ Solução

Este sistema automatiza completamente esse processo, utilizando **GPT-4o-mini** para entender o contexto dos emails e extrair automaticamente as informações relevantes em formato estruturado, pronto para integração com sistemas de gestão logística.

---

## 🚀 Funcionalidades

- ✅ **Integração com Gmail API** - Acesso seguro e automatizado à caixa de entrada
- ✅ **Extração Inteligente com IA** - Utiliza GPT-4o-mini para compreender contexto e extrair dados
- ✅ **Estruturação Automática** - Dados extraídos em formato JSON estruturado (Pydantic)
- ✅ **Filtragem por Remetente** - Busca emails específicos de fornecedores/parceiros logísticos
- ✅ **Processamento em Lote** - Processa múltiplos emails simultaneamente
- ✅ **Tratamento de Erros** - Sistema robusto com tratamento de exceções

---

## 🛠️ Tecnologias

| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| **Python** | 3.10+ | Linguagem principal |
| **LangChain** | Latest | Framework para aplicações com LLM |
| **OpenAI GPT-4o-mini** | - | Modelo de IA para extração de dados |
| **Gmail API** | v1 | Integração com Gmail |
| **Pydantic** | 2.12.5+ | Validação e estruturação de dados |
| **Google Auth** | Latest | Autenticação OAuth2 |

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter:

- Python 3.10 ou superior instalado
- Conta Google com acesso ao Gmail
- Chave de API da OpenAI
- Acesso à internet para autenticação OAuth2

---

## 🔧 Instalação

### 1. Clone o repositório

```bash
git clone <seu-repositorio>
cd "projeto email"
```

### 2. Instale as dependências

```bash
# Usando uv (recomendado)
uv sync

# Ou usando pip
pip install -r requirements.txt
```

### 3. Configure as credenciais do Gmail

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto ou selecione um existente
3. Ative a **Gmail API**
4. Crie credenciais OAuth 2.0 (tipo: Aplicativo de desktop)
5. Baixe o arquivo `credentials.json` e coloque na raiz do projeto

### 4. Configure a API da OpenAI

1. Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave_aqui
```

2. Obtenha sua chave em: [OpenAI Platform](https://platform.openai.com/api-keys)

---

## 🎮 Como Usar

### Execução Básica

```bash
python main.py
```

### Personalização

Edite o arquivo `main.py` para alterar o remetente:

```python
REMETENTE_LOGISTICO = "seu_fornecedor@email.com"
```

### Fluxo de Funcionamento

1. 🔐 **Autenticação**: O sistema autentica com sua conta Gmail (primeira execução abre navegador)
2. 📧 **Busca**: Busca os últimos 10 emails do remetente especificado
3. 🤖 **Processamento**: Cada email é processado pela IA para extração de dados
4. 📊 **Saída**: Dados estruturados são exibidos no console

### Exemplo de Saída

```json
{
  "material": "Paletes de produtos eletrônicos",
  "volume": 45.5,
  "data_horario_previsto": "2024-01-15T14:30:00"
}
```

---

## 📁 Estrutura do Projeto

```
projeto email/
│
├── main.py                 # Ponto de entrada principal
├── gmail_service.py        # Serviço de integração com Gmail
├── extractor_chain.py      # Cadeia de extração com LangChain
├── models.py               # Modelos Pydantic para validação
├── credentials.json        # Credenciais OAuth2 do Google (não versionado)
├── token.json              # Token de autenticação (gerado automaticamente)
├── .env                    # Variáveis de ambiente (não versionado)
├── pyproject.toml          # Configuração do projeto e dependências
└── README.md               # Este arquivo
```

---

## 🔍 Modelo de Dados

O sistema extrai e valida as seguintes informações:

```python
class ProgramacaoEntrega(BaseModel):
    material: str              # Descrição do material/produto
    volume: float              # Volume em m³ ou quantidade
    data_horario_previsto: datetime  # Data e hora da entrega programada
```

---

## 💼 Casos de Uso na Logística

### 1. **Gestão de Entregas**
   - Automatizar o registro de programações de entrega
   - Integrar com sistemas WMS/TMS

### 2. **Rastreamento de Materiais**
   - Monitorar materiais em trânsito
   - Atualizar sistemas de inventário automaticamente

### 3. **Otimização de Rotas**
   - Coletar dados de programações para planejamento de rotas
   - Análise de padrões de entrega

### 4. **Compliance e Auditoria**
   - Registro automático de comunicações
   - Rastreabilidade de informações

---

## 🎨 Personalização

### Alterar o Modelo de IA

No arquivo `extractor_chain.py`:

```python
llm = ChatOpenAI(model="gpt-4", temperature=0)  # Usar GPT-4 completo
```

### Ajustar Campos Extraídos

Edite o modelo em `models.py` e o prompt em `extractor_chain.py`:

```python
class ProgramacaoEntrega(BaseModel):
    material: str
    volume: float
    data_horario_previsto: datetime
    endereco_entrega: str  # Novo campo
    contato_responsavel: str  # Novo campo
```

### Modificar Quantidade de Emails

Em `gmail_service.py`:

```python
maxResults=50  # Aumentar limite
```

---

## 🔒 Segurança

- ✅ Credenciais armazenadas localmente (não versionadas)
- ✅ Autenticação OAuth2 segura
- ✅ Tokens salvos em arquivo local (`token.json`)
- ⚠️ **Importante**: Nunca commite `credentials.json`, `token.json` ou `.env`

---

## 🐛 Troubleshooting

### Erro de Autenticação Gmail
- Verifique se `credentials.json` está na raiz do projeto
- Certifique-se de que a Gmail API está habilitada no Google Cloud Console

### Erro de API Key OpenAI
- Verifique se o arquivo `.env` existe e contém `OPENAI_API_KEY`
- Confirme se a chave está válida e tem créditos disponíveis

### Nenhum email encontrado
- Verifique se o endereço do remetente está correto
- Confirme que existem emails desse remetente na caixa de entrada

---

## 📈 Melhorias Futuras

- [ ] Interface web para visualização dos dados
- [ ] Exportação para Excel/CSV
- [ ] Integração com sistemas ERP/WMS
- [ ] Dashboard de métricas logísticas
- [ ] Suporte a múltiplos remetentes
- [ ] Notificações em tempo real
- [ ] Histórico de extrações
- [ ] API REST para integração

---

## 👤 Autor

Desenvolvido para otimizar processos logísticos e demonstrar o poder da IA aplicada à automação de processos.


