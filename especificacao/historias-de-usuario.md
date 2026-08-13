# Especificação - Histórias de Usuário com Critérios de Aceitação (BDD)

## 1. Artefato escolhido
Para este projeto, o melhor artefato de especificação é a abordagem de Histórias de Usuário com Critérios de Aceitação em formato BDD.

### Justificativa
- A solução possui múltiplos perfis de usuário com necessidades distintas;
- O foco do sistema está no fluxo de negócio e na experiência do usuário;
- Há regras de negócio que mudam por evento e por perfil;
- O artefato facilita comunicação com stakeholders e validação rápida das entregas.

## 2. Histórias de Usuário

### HU-01 - Consultar eventos disponíveis
Como participante, eu quero visualizar os eventos disponíveis com suas informações básicas para escolher uma atividade de interesse.

Critérios de aceitação:
- Dado que o participante acessa a página de eventos;
- Quando ele aplica filtros por data, categoria ou tipo de evento;
- Então o sistema deve exibir apenas eventos ativos e disponíveis no período selecionado.

- Dado que um evento está lotado;
- Quando o participante visualiza a listagem;
- Então o sistema deve indicar que o evento está indisponível ou em lista de espera.

### HU-02 - Realizar inscrição em evento gratuito
Como participante, eu quero me inscrever em um evento gratuito para confirmar minha participação.

Critérios de aceitação:
- Dado que o participante esteja autenticado;
- E que o evento esteja disponível;
- Quando ele confirmar a inscrição;
- Então o sistema deve registrar a inscrição e enviar comprovante de confirmação.

### HU-03 - Realizar inscrição em evento pago
Como participante, eu quero pagar e confirmar minha inscrição em um evento pago para garantir minha vaga.

Critérios de aceitação:
- Dado que o participante selecionou um evento pago;
- Quando ele conclui o pagamento;
- Então o sistema deve confirmar a inscrição somente após validação do pagamento.

- Dado que o pagamento não foi confirmado;
- Quando o participante tenta concluir a inscrição;
- Então o sistema deve manter a inscrição em status pendente e informar o motivo.

### HU-04 - Cancelar inscrição
Como participante, eu quero cancelar minha inscrição quando necessário para liberar minha vaga ou cumprir uma regra de negócio.

Critérios de aceitação:
- Dado que a inscrição está ativa;
- Quando o participante solicita cancelamento dentro do prazo permitido;
- Então o sistema deve cancelar a inscrição e atualizar a disponibilidade do evento.

- Dado que o evento tem cancelamento bloqueado;
- Quando o participante tenta cancelar;
- Então o sistema deve rejeitar a ação e apresentar a regra aplicada.

### HU-05 - Participar de lista de espera
Como participante, eu quero entrar na lista de espera quando o evento estiver lotado para tentar obter uma vaga disponível.

Critérios de aceitação:
- Dado que o evento está lotado;
- Quando o participante solicita entrada na fila de espera;
- Então o sistema deve registrá-lo na ordem correta da fila.

- Dado que uma vaga foi liberada;
- Quando o sistema identifica a próxima posição disponível;
- Então deve promover o participante da fila e enviar notificação de confirmação.

### HU-06 - Receber comprovante
Como participante, eu quero receber o comprovante da minha inscrição para manter registro da confirmação.

Critérios de aceitação:
- Dado que a inscrição foi confirmada;
- Quando o sistema conclui o fluxo;
- Então o participante deve receber e visualizar o comprovante eletrônico.

### HU-07 - Emitir certificado
Como participante, eu quero receber o certificado após a conclusão do evento para registrar minha participação.

Critérios de aceitação:
- Dado que o evento exige participação ou presença mínima;
- Quando o participante atende ao critério definido;
- Então o sistema deve emitir o certificado.

- Dado que o participante não atende ao critério;
- Quando o sistema tenta gerar o certificado;
- Então o sistema deve bloquear a emissão e apresentar a regra aplicável.

### HU-08 - Gerenciar vagas e fila de espera
Como organizador, eu quero controlar vagas, fila de espera e status dos participantes para administrar os eventos de forma eficiente.

Critérios de aceitação:
- Dado que o organizador acessa o painel do evento;
- Quando ele visualiza a contagem de vagas;
- Então o sistema deve mostrar vagas confirmadas, vagas disponíveis e lista de espera.

- Dado que uma inscrição é cancelada;
- Quando a vaga é liberada;
- Então o sistema deve atualizar o painel e promover o próximo participante elegível.

### HU-09 - Validar pagamento
Como equipe financeira, eu quero confirmar pagamentos e regras de reembolso para liberar inscrições e manter o controle financeiro.

Critérios de aceitação:
- Dado que o participante concluiu o pagamento;
- Quando a equipe financeira valida a transação;
- Então o sistema deve confirmar a inscrição.

- Dado que um cancelamento é solicitado;
- Quando a regra de reembolso for aplicada;
- Então o sistema deve calcular e registrar o valor a ser devolvido ou negado.

### HU-10 - Visualizar inscritos do evento
Como palestrante, eu quero ver a lista de inscritos nas minhas atividades para organizar a participação e a dinâmica do evento.

Critérios de aceitação:
- Dado que o palestrante acessa sua área de atividades;
- Quando ele seleciona uma atividade;
- Então o sistema deve exibir a lista de inscritos vinculados àquele evento.

- Dado que o palestrante tenta acessar outra atividade fora do seu escopo;
- Quando ele tenta visualizar a lista;
- Então o sistema deve negar o acesso por falta de permissão.

## 3. Observação
Estas histórias descrevem principalmente o comportamento do sistema em termos de valor para o usuário. Elas devem ser complementadas por regras de negócio, requisitos não funcionais e definição de prioridades em backlog.
