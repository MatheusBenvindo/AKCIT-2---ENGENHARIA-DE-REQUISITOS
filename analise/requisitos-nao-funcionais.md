# Requisitos Não Funcionais - Sistema de Gestão de Eventos (Eventus)

## 1. Objetivo
Este documento descreve os requisitos não funcionais que garantem qualidade, segurança, performance, disponibilidade e governança do sistema de gestão de eventos.

## 2. Requisitos Não Funcionais

### RNF-01 - Segurança
O sistema deve garantir autenticação e autorização por perfil, protegendo dados pessoais, financeiros e administrativos.

Critérios:
- Todas as operações sensíveis devem exigir autenticação;
- Usuários devem acessar apenas os dados permitidos ao seu perfil;
- Dados financeiros e pessoais devem ser protegidos contra acesso indevido.

### RNF-02 - Proteção de dados pessoais
O sistema deve cumprir normas de proteção de dados e armazenar apenas informações estritamente necessárias para o processo de inscrição, pagamento e certificação.

Critérios:
- Dados pessoais devem ser armazenados com proteção adequada;
- O sistema deve permitir o controle de consentimento e uso de informações;
- Registros de auditoria devem estar disponíveis para consultas autorizadas.

### RNF-03 - Integridade de transações
O sistema deve garantir consistência de dados em operações críticas, como inscrição, confirmação de pagamento e cancelamento.

Critérios:
- Uma inscrição não pode ser considerada confirmada sem validação adequada;
- Operações de cancelamento e pagamento devem ser atômicas;
- Falhas temporárias não devem gerar duplicidade de registros.

### RNF-04 - Disponibilidade
O sistema deve estar disponível conforme a necessidade operacional da organização, especialmente em períodos de inscrição e confirmação de pagamentos.

Critérios:
- Disponibilidade mínima esperada de 99,9% em operação normal;
- O sistema deve apresentar mecanismos de recuperação ante falhas;
- Operações críticas devem suportar falhas temporárias sem perda de consistência.

### RNF-05 - Performance
O sistema deve responder rapidamente às operações mais frequentes, como consulta de eventos, inscrição, pagamento e geração de comprovantes.

Critérios:
- Tempo de resposta de consulta pública em até 3 segundos em condições normais;
- A operação de inscrição deve ser concluída em até 5 segundos em cenários típicos;
- O sistema deve suportar múltiplos acessos simultâneos durante períodos de pico.

### RNF-06 - Escalabilidade
O sistema deve suportar crescimento no número de eventos, participantes e transações sem degradação significativa de desempenho.

Critérios:
- O sistema deve manter desempenho aceitável com aumento de volume de inscrições;
- O modelo de dados e arquitetura devem permitir expansão por evento e por usuário;
- A fila de espera e o processamento de pagamentos devem escalar de forma estável.

### RNF-07 - Confiabilidade e recuperação
O sistema deve ser resiliente a falhas temporárias e permitir a recuperação completa de operações interrompidas.

Critérios:
- O sistema deve manter registro das transações importantes;
- Falhas de rede ou processamento não devem corromper o estado da inscrição;
- O sistema deve permitir restauração do estado após falhas sem intervenção manual intensa.

### RNF-08 - Auditabilidade
Todas as ações relevantes do sistema devem ser registradas para rastreabilidade e análise.

Critérios:
- O sistema deve gerar log de ações como inscrição, cancelamento, confirmação de pagamento e promoção de lista de espera;
- Logs devem conter identificador do usuário, data/hora e ação executada;
- A auditoria deve permitir investigação de inconsistências ou incidentes.

### RNF-09 - Usabilidade
A interface do sistema deve ser clara e acessível para os usuários dos diferentes perfis.

Critérios:
- Fluxos de inscrição e cancelamento devem ser intuitivos;
- Informações de vagas, regras e pagamentos devem ser explícitas;
- O sistema deve apresentar mensagens de erro ou confirmação compreensíveis.

### RNF-10 - Compatibilidade
O sistema deve operar corretamente em navegadores modernos e em dispositivos de uso comum para participantes e organizadores.

Critérios:
- A aplicação deve funcionar em navegadores atuais;
- A interface deve ser responsiva para desktop e mobile;
- A navegação deve preservar a funcionalidade nas principais resoluções de tela.

### RNF-11 - Manutenibilidade
O sistema deve ser desenvolvido com boas práticas de arquitetura e documentação, facilitando evoluções futuras.

Critérios:
- O código deve ser modular e organizado por domínio;
- Regras de negócio devem estar documentadas;
- Mudanças em regras de eventos devem ser aplicadas sem impacto geral desnecessário.

### RNF-12 - Observabilidade
O sistema deve permitir monitoramento de erros, desempenho e comportamento do negócio.

Critérios:
- O sistema deve ter indicadores de disponibilidade e erros;
- O ambiente deve permitir acompanhamento de transações críticas;
- O suporte técnico deve localizar falhas por evento, usuário ou fluxo de negócio.

## 3. Resumo
Os requisitos não funcionais acima são fundamentais para que o sistema de gestão de eventos seja seguro, estável, útil e escalável. Eles complementam os requisitos funcionais e devem ser considerados desde a etapa de desenho da solução.
