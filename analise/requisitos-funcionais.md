# Requisitos Funcionais - Sistema de Gestão de Eventos (Eventus)

## 1. Introdução
Este documento reúne os requisitos funcionais do sistema, com foco nas necessidades dos participantes, organizadores, equipe financeira, palestrantes e equipe de TI. Os requisitos abaixo foram escritos de forma objetiva, verificável e alinhada às necessidades identificadas na elicitação.

## 2. Requisitos Funcionais

### RF-01 - Consulta pública de eventos
O sistema deve permitir que qualquer usuário acessível ao público visualize a lista de eventos disponíveis, incluindo informações como nome, data, horário, local, categoria, vagas disponíveis, tipo (gratuito ou pago) e status do evento.

Critério de verificação:
- A interface deve exibir eventos ativos e futuros;
- A busca deve filtrar por data, categoria, tipo de evento e disponibilidade;
- O sistema deve informar corretamente a quantidade de vagas restantes.

### RF-02 - Inscrição de participante em evento
O sistema deve permitir que um participante realize inscrição em um evento disponível, desde que as condições de disponibilidade, pagamento e regras de negócio do evento permitam a inscrição.

Critério de verificação:
- A inscrição só é concluída após validação das regras do evento;
- O sistema deve registrar a inscrição com data e hora de confirmação;
- O sistema deve impedir inscrição duplicada para o mesmo participante no mesmo evento.

### RF-03 - Controle automático de vagas
O sistema deve controlar a quantidade de vagas disponíveis para cada evento em tempo real e bloquear novas inscrições quando a capacidade for atingida.

Critério de verificação:
- A contagem de vagas deve refletir inscrições confirmadas e cancelamentos realizados;
- O sistema deve impedir inscrições além da capacidade definida;
- O evento deve indicar corretamente status de lotado.

### RF-04 - Lista de espera
Quando um evento estiver lotado, o sistema deve permitir que o participante insira-se em lista de espera e, automaticamente, promove-lo para a vaga assim que houver liberação.

Critério de verificação:
- O sistema deve registrar a ordem de entrada na lista de espera;
- A promoção deve ocorrer para o primeiro participante elegível da fila;
- O participante promovido deve receber notificação da confirmação.

### RF-05 - Pagamento e confirmação de inscrição
Para eventos pagos, o sistema deve permitir o processamento do pagamento e confirmar a inscrição somente após a validação do pagamento pela equipe financeira ou pelo próprio fluxo do sistema, conforme a regra do evento.

Critério de verificação:
- O sistema deve exigir pagamento para eventos pagos;
- A inscrição deve permanecer pendente até a confirmação do pagamento;
- A confirmação deve gerar registro de pagamento e status de inscrição.

### RF-06 - Emissão de comprovante de inscrição
Após a inscrição ou confirmação de pagamento, o sistema deve emitir um comprovante eletrônico para o participante, com dados do evento, valor, data da inscrição e código de confirmação.

Critério de verificação:
- O comprovante deve estar disponível imediatamente após a confirmação;
- O participante deve conseguir visualizar e baixar o comprovante;
- O comprovante deve conter identificação do evento e do participante.

### RF-07 - Cancelamento de inscrição pelo participante
O participante deve poder cancelar sua própria inscrição, respeitando as regras definidas para o evento e o período de cancelamento.

Critério de verificação:
- O sistema deve permitir cancelamento apenas para inscrições válidas;
- O cancelamento deve atualizar a contagem de vagas e a lista de espera;
- O sistema deve registrar a justificativa, quando exigida, ou a ação de cancelamento.

### RF-08 - Bloqueio de cancelamento para eventos específicos
O organizador deve ser capaz de configurar eventos que não permitam cancelamento após determinado prazo ou em determinadas condições, e o sistema deve bloquear essa ação.

Critério de verificação:
- O sistema deve impedir cancelamentos quando a regra do evento o proíba;
- A regra deve ser visível ao participante no momento da inscrição;
- A tentativa de cancelamento inválido deve ser rejeitada com mensagem adequada.

### RF-09 - Reembolso conforme regra do evento
O sistema deve aplicar regras de reembolso conforme o tipo de evento, data do cancelamento, modalidade de pagamento e política da organização.

Critério de verificação:
- O sistema deve calcular o valor reembolsável de acordo com a regra do evento;
- O sistema deve registrar a decisão de reembolso ou não reembolso;
- A equipe financeira deve visualizar os casos elegíveis para análise.

### RF-10 - Emissão de certificados
O sistema deve permitir a geração de certificados para participantes que concluíram o evento ou atenderam aos critérios definidos pela organização, como presença mínima ou participação validada.

Critério de verificação:
- O certificado deve ser emitido apenas para participantes elegíveis;
- O sistema deve permitir visualização e download do certificado;
- O sistema deve registrar a data de emissão e o evento relacionado.

### RF-11 - Inscrição em workshop no mesmo dia
O sistema deve permitir que um participante realize inscrições em diferentes atividades do mesmo dia, desde que não haja conflito de horário ou regras específicas do evento que impeçam a sobreposição.

Critério de verificação:
- O sistema deve detectar conflito de agenda antes da confirmação;
- A inscrição deve ser bloqueada quando houver sobreposição de horários;
- O sistema deve informar ao participante a razão da rejeição.

### RF-12 - Gestão de participantes por palestrante
O palestrante deve poder visualizar a lista de participantes inscritos em suas atividades, sem ter acesso completo a dados financeiros ou administrativos do sistema.

Critério de verificação:
- O palestrante acessa apenas as atividades sob sua responsabilidade;
- A lista deve conter nome do participante, inscrição e dados relevantes da atividade;
- O palestrante não deve ver dados sensíveis de pagamento.

### RF-13 - Visualização de inscrições em tempo real para o organizador
O organizador deve visualizar, em tempo real, o total de inscritos e o status das vagas de cada evento sob sua gestão.

Critério de verificação:
- O painel deve atualizar após cada inscrição, cancelamento ou promoção da lista de espera;
- O total exibido deve refletir o estado atual do evento;
- O organizador deve conseguir identificar eventos lotados e em lista de espera.

### RF-14 - Eventos simultâneos
O sistema deve suportar a gestão de múltiplos eventos ocorrendo em paralelo, com controle independente de vagas, inscrições e pagamentos.

Critério de verificação:
- O sistema deve manter contagem isolada por evento;
- O cadastro de um evento não deve interferir no outro;
- A fila de espera deve operar de forma independente por evento.

### RF-15 - Notificações ao participante
O sistema deve enviar notificações ao participante sobre confirmação de inscrição, cancelamento, lista de espera, promoção, reembolso e emissão de certificado, conforme o canal definido pela organização.

Critério de verificação:
- A notificação deve ser disparada em condições específicas do fluxo;
- O sistema deve registrar o envio e o status da mensagem;
- O participante deve receber confirmação do evento de interesse.

### RF-16 - Gestão de eventos e atividades pelo organizador
O organizador deve poder cadastrar, alterar, ativar e desativar eventos, além de definir regras de vagas, pagamentos, cancelamento e certificados para cada atividade.

Critério de verificação:
- O cadastro deve permitir dados obrigatórios do evento;
- O organizador deve alterar regras sem afetar outros eventos;
- O sistema deve manter histórico das mudanças relevantes.

### RF-17 - Acesso e visão por perfil
O sistema deve disponibilizar funcionalidades específicas conforme o perfil do usuário: participante, organizador, financeiro, palestrante e equipe de TI.

Critério de verificação:
- Cada perfil deve acessar apenas os módulos relevantes;
- A autenticação deve identificar corretamente o perfil do usuário;
- A operação fora do escopo do perfil deve ser negada.

### RF-18 - Logs e rastreabilidade de ações
O sistema deve registrar eventos importantes, como inscrição, cancelamento, confirmação de pagamento, promoção de lista de espera e emissão de certificado.

Critério de verificação:
- O sistema deve manter histórico de ações realizadas;
- A auditoria deve permitir consulta por usuário, evento e data;
- As alterações relevantes devem estar associadas ao responsável.

## 3. Observações
Os requisitos acima refletem a elicitação e foram estruturados para evitar ambiguidades. Ainda existem decisões de negócio que precisam ser confirmadas pela organização antes da implementação final, conforme descrito em [duvidas-e-lacunas.md](duvidas-e-lacunas.md).
