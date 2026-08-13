# Critérios de Aceitação

## CA01 - Inscrição em evento gratuito
- O participante deve conseguir acessar a página de detalhes do evento.
- Se o evento for gratuito e estiver disponível, o sistema deve registrar a inscrição.
- O sistema deve apresentar confirmação e comprovante após a inscrição.

## CA02 - Inscrição em evento pago
- O participante deve conseguir selecionar um evento pago e seguir o fluxo de pagamento.
- Se o pagamento for validado, a inscrição deve ser confirmada.
- Se o pagamento não for validado, o sistema deve manter a inscrição com status pendente.

## CA03 - Cancelamento de inscrição
- O participante deve conseguir cancelar uma inscrição ativa dentro do prazo definido.
- Se o evento possuir cancelamento bloqueado, o sistema deve rejeitar a ação e informar a regra.
- A ação deve atualizar a disponibilidade de vagas e a fila de espera, quando houver.

## CA04 - Lista de espera
- Quando o evento estiver lotado, o sistema deve registrar o participante na fila de espera.
- Quando uma vaga for liberada, o primeiro participante da fila deve receber a oportunidade de confirmação.
- O sistema deve notificar o participante sobre a promoção da vaga.

## CA05 - Emissão de certificado
- Se o participante atender à regra de presença ou participação do evento, o sistema deve emitir o certificado.
- Se o participante não atender ao critério, o sistema deve bloquear a emissão e informar o motivo.
- O sistema deve registrar o resultado da emissão na base de dados.

## CA06 - Acesso do palestrante
- O palestrante deve visualizar somente os participantes relacionados a suas atividades.
- O sistema deve bloquear qualquer tentativa de acesso fora do escopo da responsabilidade do palestrante.
- O acesso deve ser auditado e registrado.

## CA07 - Painel do organizador
- O organizador deve visualizar vagas disponíveis, vagas ocupadas e fila de espera em um mesmo painel.
- O sistema deve atualizar o painel assim que houver alteração de inscrição ou cancelamento.
- O organizador deve conseguir acompanhar o status geral do evento de forma clara.
