# Critérios de Aceitação

## CA01 - Cadastro de alertas de vagas
- O sistema deve permitir que um usuário cadastre um alerta informando pelo menos um termo de busca, uma área de TI e uma localidade.
- O alerta deve ser persistido com status ativo após confirmação do cadastro.
- O sistema deve exibir uma mensagem de sucesso ao salvar o alerta.

## CA02 - Filtros por banca examinadora
- O usuário deve conseguir selecionar uma banca examinadora em uma lista disponível no filtro de busca.
- A consulta deve retornar apenas os editais associados à banca examinadora selecionada.
- Quando não houver resultados, o sistema deve exibir uma mensagem indicando ausência de ocorrências.

## CA03 - Leitura de retificações de editais
- O sistema deve exibir todas as retificações associadas a um edital em ordem cronológica.
- Cada retificação deve mostrar, no mínimo, data, descrição da alteração e impacto no edital.
- O usuário deve conseguir acessar o conteúdo da retificação diretamente a partir da tela do edital.
