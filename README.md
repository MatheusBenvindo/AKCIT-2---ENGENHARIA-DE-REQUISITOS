# Monitor de APIs - Gestão de Riscos e Comunicação

Link do repositório: [LINK AQUI]

## 1. Cenário do Projeto
Este projeto consiste em um script Python para consumo e monitoramento de dados de uma API HTTP externa. O objetivo principal do script é realizar requisições periódicas a um endpoint específico, validar o status da resposta e salvar os dados localmente para análise posterior.

## 2. Riscos Técnicos Identificados
1. **Indisponibilidade do Endpoint (Down Time):** Falha temporária ou permanente no servidor de destino da API, impedindo a coleta dos dados.
2. **Mudança Inesperada no Payload (Quebra de Contrato):** Alteração na estrutura do JSON retornado pela API sem aviso prévio, causando falhas na etapa de parsing do script.
3. **Estouro do Limite de Requisições (Rate Limit Exceeded):** Bloqueio temporário das requisições por exceder a cota contratada ou permitida pelo provedor do serviço.

## 3. Estratégia de Resposta a Riscos (Rate Limit e Indisponibilidade)
Para mitigar a indisponibilidade temporária e o estouro de rate limit, foi implementada a estratégia de **tentativas de requisição com recuo exponencial (Exponential Backoff com Jitter)**. 

Se a requisição retornar um código HTTP 429 (Too Many Requests) ou 5xx (Erros no Servidor), o script aguarda um tempo que cresce exponencialmente a cada falha subsequente, adicionando uma variação aleatória (jitter) para evitar a sobrecarga síncrona do servidor de destino. O script está configurado para realizar no máximo 5 tentativas antes de registrar o erro definitivo nos logs e notificar o operador.

## 4. Apoio da Inteligência Artificial na Atividade
A IA foi utilizada para mapear cenários de falha puramente técnicos de infraestrutura HTTP, auxiliando a isolar esses problemas dos riscos de negócio (como atrasos na entrega ou falta de orçamento). O uso da IA facilitou a identificação de comportamentos específicos de redes e protocolos de comunicação (como timeouts e códigos de erro de gateway).

## 5. Limitações e Cuidados com a IA
Durante o processo, a IA sugeriu repetidamente metodologias formais e pesadas de gestão de riscos (como matrizes de risco probabilísticas completas e documentações extensas). Essa abordagem representaria superdimensionamento de engenharia (*overengineering*) para um script simples e de baixo impacto como este monitor. Foi necessário filtrar as sugestões para extrair apenas os tratamentos técnicos aplicáveis diretamente ao código.
