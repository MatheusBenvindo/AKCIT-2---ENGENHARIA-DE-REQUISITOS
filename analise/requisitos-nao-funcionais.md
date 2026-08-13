# Requisitos Não Funcionais - Sistema de Gestão de Eventos (Eventus)

## 1. Objetivo
Este documento descreve os requisitos não funcionais que garantem qualidade, segurança, desempenho, disponibilidade e governança do sistema de gestão de eventos da Eventus.

## 2. Requisitos Não Funcionais

### RNF-01 - Segurança
O sistema deve garantir autenticação e autorização por perfil, protegendo dados pessoais, financeiros e administrativos.

Critérios:
- todas as operações sensíveis devem exigir autenticação;
- usuários devem acessar somente os dados permitidos ao seu perfil;
- dados financeiros e pessoais devem ser protegidos contra acesso indevido.

### RNF-02 - Proteção de dados pessoais
O sistema deve cumprir normas de proteção de dados e armazenar somente informações estritamente necessárias para inscrição, pagamento e certificação.

Critérios:
- dados pessoais devem ser armazenados com proteção adequada;
- o sistema deve permitir o controle de consentimento e uso das informações;
- registros de auditoria devem estar disponíveis para consultas autorizadas.

### RNF-03 - Integridade de transações
O sistema deve garantir consistência de dados em operações críticas, como inscrição, confirmação de pagamento e cancelamento.

Critérios:
- uma inscrição não pode ser considerada confirmada sem validação adequada;
- operações de cancelamento e pagamento devem ser atômicas;
- falhas temporárias não devem gerar duplicidade de registros.

### RNF-04 - Disponibilidade
O sistema deve estar disponível conforme a necessidade operacional da organização, principalmente em períodos de alta demanda de inscrições e pagamentos.

Critérios:
- disponibilidade mínima esperada de 99,9% em operação normal;
- o sistema deve apresentar mecanismos de recuperação ante falhas;
- operações críticas devem suportar falhas temporárias sem perda de consistência.

### RNF-05 - Performance
O sistema deve responder rapidamente às operações mais frequentes, como consulta de eventos, inscrição, pagamento e geração de comprovantes.

Critérios:
- tempo de resposta de consulta pública em até 3 segundos em condições normais;
- a operação de inscrição deve ser concluída em até 5 segundos em cenários típicos;
- o sistema deve suportar múltiplos acessos simultâneos durante períodos de pico.

### RNF-06 - Escalabilidade
O sistema deve suportar crescimento no número de eventos, participantes e transações sem degradação significativa de desempenho.

Critérios:
- o sistema deve manter desempenho aceitável com aumento de volume de inscrições;
- o modelo de dados e a arquitetura devem permitir expansão por evento e por usuário;
- a fila de espera e o processamento de pagamentos devem escalar de forma estável.

### RNF-07 - Confiabilidade e recuperação
O sistema deve ser resiliente a falhas temporárias e permitir a recuperação completa de operações interrompidas.

Critérios:
- o sistema deve manter registro das transações importantes;
- falhas de rede ou processamento não devem corromper o estado da inscrição;
- o sistema deve permitir restauração do estado após falhas sem intervenção manual intensa.

### RNF-08 - Auditabilidade
Todas as ações relevantes do sistema devem ser registradas para rastreabilidade e análise.

Critérios:
- o sistema deve gerar log de ações como inscrição, cancelamento, confirmação de pagamento e promoção de lista de espera;
- logs devem conter identificador do usuário, data/hora e ação executada;
- a auditoria deve permitir investigação de inconsistências ou incidentes.

### RNF-09 - Usabilidade
A interface do sistema deve ser clara e acessível para os usuários dos diferentes perfis.

Critérios:
- fluxos de inscrição e cancelamento devem ser intuitivos;
- informações de vagas, regras e pagamentos devem ser explícitas;
- o sistema deve apresentar mensagens de erro ou confirmação compreensíveis.

### RNF-10 - Compatibilidade
O sistema deve operar corretamente em navegadores modernos e em dispositivos de uso comum para participantes e organizadores.

Critérios:
- a aplicação deve funcionar em navegadores atuais;
- a interface deve ser responsiva para desktop e mobile;
- a navegação deve preservar a funcionalidade nas principais resoluções de tela.

### RNF-11 - Manutenibilidade
O sistema deve ser desenvolvido com boas práticas de arquitetura e documentação, facilitando evoluções futuras.

Critérios:
- o código deve ser modular e organizado por domínio;
- regras de negócio devem estar documentadas;
- mudanças em regras de eventos devem ser aplicadas sem impacto geral desnecessário.

### RNF-12 - Observabilidade
O sistema deve permitir monitoramento de erros, desempenho e comportamento do negócio.

Critérios:
- o sistema deve ter indicadores de disponibilidade e erros;
- o ambiente deve permitir acompanhamento de transações críticas;
- o suporte técnico deve localizar falhas por evento, usuário ou fluxo de negócio.

## 3. Resumo
Os requisitos não funcionais acima são fundamentais para que o sistema de gestão de eventos seja seguro, estável, útil e escalável. Eles complementam os requisitos funcionais e devem ser considerados desde a etapa de desenho da solução.
