# Regras de Negócio - Sistema de Gestão de Eventos (Eventus)

## 1. Introdução
Este documento reúne as regras de negócio derivadas da elicitação. Elas definem o comportamento esperado do sistema e devem ser validadas junto à organização antes da implementação final, porque algumas decisões ainda exigem confirmação.

## 2. Regras de Negócio

### RN-01 - Tipos de evento
Um evento pode ser gratuito ou pago, e essa classificação deve ser configurável pelo organizador.

### RN-02 - Limite de vagas
Cada evento deve possuir número máximo de participantes, definido pelo organizador no momento do cadastro.

### RN-03 - Inscrição duplicada
O mesmo participante não pode se inscrever duas vezes no mesmo evento.

### RN-04 - Pagamento obrigatório para eventos pagos
Eventos pagos só podem ser considerados confirmados após o processamento e a validação do pagamento.

### RN-05 - Confirmação da inscrição
A inscrição deve entrar em estado pendente até que a validação do pagamento ou da disponibilidade da vaga seja concluída.

### RN-06 - Cancelamento pelo participante
O participante pode cancelar sua própria inscrição, desde que a regra do evento permita essa ação no momento do cancelamento.

### RN-07 - Bloqueio de cancelamento
Eventos com política de cancelamento restrita devem impedir o cancelamento após o prazo ou condição configurada pela organização.

### RN-08 - Reembolso
O valor de reembolso, quando aplicável, deve seguir a política definida para o evento e para o tipo de pagamento.

### RN-09 - Lista de espera
Quando um evento está lotado, a inscrição deve ser registrada em lista de espera, mantendo ordem de entrada.

### RN-10 - Promoção automática da lista de espera
Quando uma vaga é liberada, o participante mais antigo da fila deve receber a oportunidade de ocupar a vaga e ser notificado.

### RN-11 - Certificado
Certificados devem ser emitidos apenas para participantes elegíveis, conforme as regras definidas pela organização e pelo evento.

### RN-12 - Presença mínima
Se a organização exigir presença mínima, apenas participantes que atenderem ao critério estabelecido poderão receber o certificado.

### RN-13 - Conflito de horários
Participantes não podem se inscrever em atividades que tenham sobreposição de horário, salvo exceções explicitamente permitidas pelo organizador.

### RN-14 - Acesso do palestrante
Palestrantes podem visualizar apenas os participantes vinculados às atividades sob sua responsabilidade.

### RN-15 - Acesso financeiro
A equipe financeira pode visualizar informações relacionadas a pagamentos, valores, status de confirmação e regras de reembolso, mas não deve ter acesso indiscriminado a dados de outras áreas do sistema.

### RN-16 - Acesso do organizador
O organizador pode gerenciar vagas, regras de evento, inscrições, lista de espera e status geral do evento, dentro do escopo do seu projeto ou área de atuação.

### RN-17 - Eventos simultâneos
Cada evento deve ser gerenciado de forma independente, com seu próprio controle de inscrição, vagas e fila de espera.

### RN-18 - Notificações
O sistema deve notificar o participante sobre eventos relevantes do fluxo de inscrição, pagamento, cancelamento, lista de espera, promoção e certificado.

## 3. Decisões pendentes de negócio
A organização ainda precisa confirmar as seguintes regras antes da implementação final:
- Prazo máximo para cancelamento de inscrição;
- Política de reembolso para cada tipo de evento;
- Critério de elegibilidade para emissão automática de certificado;
- Mecanismo de notificação (e-mail, SMS, WhatsApp, push ou outro);
- Tempo de retenção da vaga durante o checkout;
- Critério de conflito de horários entre atividades;
- Dados que o palestrante pode visualizar além do nome e da atividade.

## 4. Observação
Essas regras são fundamentais para a consistência do sistema e devem ser formalizadas em documento de negócio antes do início do desenvolvimento, para reduzir retrabalho e conflitos de interpretação.
