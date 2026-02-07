# 📦 Sistema de Extração Inteligente de Dados Logísticos

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-purple.svg)
![Gmail API](https://img.shields.io/badge/Gmail-API-red.svg)
![Google Calendar](https://img.shields.io/badge/Google-Calendar-green.svg)

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

Este sistema automatiza completamente esse processo, utilizando **GPT-4o-mini** para entender o contexto dos emails e extrair automaticamente as informações relevantes em formato estruturado. Além disso, gera relatórios em Excel e cria eventos automaticamente no Google Calendar, pronto para integração com sistemas de gestão logística.

---

## 🚀 Funcionalidades

- ✅ **Integração com Gmail API** - Acesso seguro e automatizado à caixa de entrada
- ✅ **Extração Inteligente com IA** - Utiliza GPT-4o-mini para compreender contexto e extrair dados
- ✅ **Estruturação Automática** - Dados extraídos em formato estruturado (Pydantic)
- ✅ **Suporte a Múltiplos Remetentes** - Processa emails de vários fornecedores/parceiros logísticos
- ✅ **Exportação para Excel** - Gera arquivos Excel com timestamp para análise e backup
- ✅ **Integração com Google Calendar** - Cria eventos automaticamente no Google Agenda
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
| **Google Calendar API** | v3 | Criação automática de eventos |
| **Pandas** | 2.3.3+ | Manipulação e análise de dados |
| **OpenPyXL** | 3.1.5+ | Geração de arquivos Excel |
| **Pydantic** | 2.12.5+ | Validação e estruturação de dados |
| **Google Auth** | Latest | Autenticação OAuth2 |

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter:

- Python 3.10 ou superior instalado
- Conta Google com acesso ao Gmail e Google Calendar
- Chave de API da OpenAI
- Acesso à internet para autenticação OAuth2

---

## 🔧 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/DSagentpy/AI-Logistics-Email-Automation.git
cd AI-Logistics-Email-Automation
```

### 2. Instale as dependências

```bash
# Usando uv (recomendado)
uv sync

# Ou usando pip
pip install -r requirements.txt
```

### 3. Configure as credenciais do Google

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto ou selecione um existente
3. Ative as seguintes APIs:
   - **Gmail API**
   - **Google Calendar API**
4. Crie credenciais OAuth 2.0 (tipo: Aplicativo de desktop)
5. Baixe o arquivo `credentials.json` e coloque na raiz do projeto

### 4. Configure a API da OpenAI

1. Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave_aqui
```

2. Obtenha sua chave em: [OpenAI Platform](https://platform.openai.com/api-keys)

### 5. Crie a pasta de saída (opcional)

```bash
mkdir outputs
```

---

## 🎮 Como Usar

### Execução Básica

```bash
python main.py
```

### Personalização

Edite o arquivo `main.py` para alterar os remetentes:

```python
REMETENTE_LOGISTICO = [
    "fornecedor1@email.com",
    "fornecedor2@email.com"
]
```

### Fluxo de Funcionamento

1. 🔐 **Autenticação**: O sistema autentica com sua conta Google (primeira execução abre navegador)
2. 📧 **Busca**: Busca os últimos 10 emails de cada remetente especificado
3. 🤖 **Processamento**: Cada email é processado pela IA para extração de dados
4. 📊 **Estruturação**: Dados são organizados em DataFrame (Pandas)
5. 💾 **Exportação**: Gera arquivo Excel na pasta `outputs/` com timestamp
6. 📅 **Calendário**: Cria eventos automaticamente no Google Calendar
7. ✅ **Confirmação**: Exibe mensagem de sucesso e links dos eventos criados

### Exemplo de Saída

**Console:**
```
Arquivo salvo com sucesso!
Evento criado: https://calendar.google.com/calendar/event?eid=...
Evento criado: https://calendar.google.com/calendar/event?eid=...
```

**Arquivo Excel gerado:**
```
outputs/programacoes_20240115_143022.xlsx
```

**Estrutura do Excel:**
| material | volume | data_prevista |
|----------|--------|---------------|
| Paletes de produtos eletrônicos | 45.5 | 15/01/2024 14:30 |
| Container de matéria-prima | 120.0 | 16/01/2024 09:00 |

**Eventos no Google Calendar:**
- Título: "Recebimento - [Material]"
- Descrição: Material e volume em toneladas
- Data/Hora: Conforme extraído do email

---

## 📁 Estrutura do Projeto

```
AI-Logistics-Email-Automation/
│
├── main.py                 # Ponto de entrada principal
├── gmail_service.py        # Serviço de integração com Gmail e Calendar
├── extractor_chain.py      # Cadeia de extração com LangChain
├── models.py               # Modelos Pydantic para validação
├── credentials.json        # Credenciais OAuth2 do Google (não versionado)
├── token.json              # Token de autenticação (gerado automaticamente)
├── .env                    # Variáveis de ambiente (não versionado)
├── pyproject.toml          # Configuração do projeto e dependências
├── outputs/                # Pasta com arquivos Excel gerados
│   └── programacoes_*.xlsx
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
   - Criar lembretes automáticos no calendário

### 2. **Rastreamento de Materiais**
   - Monitorar materiais em trânsito
   - Atualizar sistemas de inventário automaticamente
   - Manter histórico em arquivos Excel

### 3. **Otimização de Rotas**
   - Coletar dados de programações para planejamento de rotas
   - Análise de padrões de entrega
   - Visualização de programações no calendário

### 4. **Compliance e Auditoria**
   - Registro automático de comunicações
   - Rastreabilidade de informações
   - Histórico documentado em Excel

### 5. **Agendamento Automático**
   - Eventos criados automaticamente no Google Calendar
   - Notificações configuráveis
   - Sincronização com dispositivos móveis

---


</div>
