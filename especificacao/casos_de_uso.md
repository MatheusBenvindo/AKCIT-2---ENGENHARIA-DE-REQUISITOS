# Casos de Uso

## UC01 - Consultar eventos disponíveis
Ator: Participante

Objetivo: visualizar eventos disponíveis e escolher uma atividade de interesse.

Fluxo principal:
1. O participante acessa a página inicial de eventos.
2. O sistema exibe a lista de eventos disponíveis.
3. O participante aplica filtros e visualiza as opções relevantes.

## UC02 - Realizar inscrição em evento gratuito
Ator: Participante

Objetivo: confirmar participação em evento gratuito.

Fluxo principal:
1. O participante seleciona um evento gratuito.
2. O sistema valida a disponibilidade do evento.
3. O sistema registra a inscrição e emite o comprovante.

## UC03 - Realizar inscrição em evento pago
Ator: Participante

Objetivo: concluir inscrição em evento pago após pagamento validado.

Fluxo principal:
1. O participante seleciona um evento pago.
2. O sistema direciona para o processo de pagamento.
3. O pagamento é validado.
4. O sistema confirma a inscrição e gera o comprovante.

## UC04 - Cancelar inscrição
Ator: Participante

Objetivo: cancelar uma inscrição conforme regra do evento.

Fluxo principal:
1. O participante solicita o cancelamento.
2. O sistema valida o prazo e a regra do evento.
3. O sistema confirma ou rejeita o cancelamento.
4. O sistema atualiza o status da vaga.

## UC05 - Entrar na lista de espera
Ator: Participante

Objetivo: aguardar uma vaga quando o evento estiver lotado.

Fluxo principal:
1. O participante tenta se inscrever em um evento lotado.
2. O sistema registra a inscrição na fila de espera.
3. O sistema mantém a ordem da fila e notifica o participante quando houver vaga.

## UC06 - Gerenciar vagas e fila de espera
Ator: Organizador

Objetivo: controlar vagas, status e fila de espera do evento.

Fluxo principal:
1. O organizador acessa o painel do evento.
2. O sistema exibe vagas disponíveis, lotadas e fila de espera.
3. O organizador acompanha a evolução e pode tomar ações conforme necessidade.

## UC07 - Validar pagamento e reembolso
Ator: Equipe Financeira

Objetivo: confirmar pagamentos e aplicar as regras de reembolso.

Fluxo principal:
1. A equipe financeira acessa as inscrições pendentes.
2. O sistema mostra dados financeiros e status da transação.
3. A equipe valida o pagamento ou aplica a regra de reembolso.
4. O sistema atualiza o status da inscrição.

## UC08 - Visualizar inscritos do evento
Ator: Palestrante

Objetivo: consultar os participantes vinculados às suas atividades.

Fluxo principal:
1. O palestrante acessa a área da atividade.
2. O sistema exibe a lista de inscritos autorizados.
3. O sistema bloqueia acesso a dados fora do escopo do palestrante.
