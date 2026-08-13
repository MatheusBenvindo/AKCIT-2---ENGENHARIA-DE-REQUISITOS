# Sistema de Gestão de Eventos - Eventus

## Visão geral
Este projeto documenta a análise e a especificação de requisitos para o sistema de gestão de eventos da empresa Eventus. O objetivo é centralizar o controle de inscrições, vagas, pagamentos, cancelamentos, filas de espera e emissão de certificados.

## Objetivo

Permitir que participantes, organizadores, equipe financeira, palestrantes e equipe de TI gerenciem, acompanhem e validem o ciclo completo de eventos, com regras claras de negócio, controle de acesso e rastreabilidade do processo.

## Como a IA ajudou na melhoria da qualidade
A inteligência artificial foi utilizada para:

1. separar corretamente requisitos funcionais de regras de negócio;
2. remover ambiguidades e ruídos da elicitação inicial;
3. transformar observações vagas em requisitos verificáveis;
4. identificar lacunas que ainda precisam ser confirmadas pela organização;
5. estruturar a documentação em arquivos Markdown prontos para revisão e evolução.

Essa ajuda foi essencial para transformar a elicitação bruta em uma especificação mais técnica, consistente e adequada à prática de engenharia de requisitos.

## Artefato de especificação escolhido
Optamos por usar Histórias de Usuário com Critérios de Aceitação em formato BDD como artefato principal de especificação.

### Motivos da escolha
- o sistema possui vários perfis de usuário com necessidades diferentes;
- o foco principal está no valor entregue em cada fluxo de negócio;
- as regras variam por evento e por perfil;
- o formato facilita a validação com stakeholders e a priorização no backlog.

## Arquivos gerados

- [analise/requisitos-funcionais.md](analise/requisitos-funcionais.md)
- [analise/requisitos-nao-funcionais.md](analise/requisitos-nao-funcionais.md)
- [analise/regras-de-negocio.md](analise/regras-de-negocio.md)
- [analise/duvidas-e-lacunas.md](analise/duvidas-e-lacunas.md)
- [especificacao/historias-de-usuario.md](especificacao/historias-de-usuario.md)
- [especificacao/casos_de_uso.md](especificacao/casos_de_uso.md)
- [especificacao/criterios_de_aceitacao.md](especificacao/criterios_de_aceitacao.md)

## Observação importante
A análise foi refinada, mas algumas regras ainda dependem de decisão de negócio da organização. Isso é positivo, porque deixa explícitas as pendências que precisam ser confirmadas antes do desenvolvimento.

Em engenharia de requisitos, essa separação entre o que já está definido e o que ainda precisa ser validado é uma boa prática essencial.

## Conclusão
A entrega ficou mais sólida porque foi organizada com base em critérios de qualidade de requisitos: completude, consistência, verificabilidade, clareza e rastreabilidade. A documentação agora está mais próxima do que uma equipe de desenvolvimento e de negócio precisaria para iniciar a solução com menos retrabalho e menos interpretação equivocada.

