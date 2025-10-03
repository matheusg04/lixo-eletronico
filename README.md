# Documentando o Projeto: Aplicação Web para Descarte de Resíduos

## Resumo do Projeto  
Este projeto tem como objetivo desenvolver uma aplicação web que auxilie a população no descarte correto de resíduos como pilhas, óleo de cozinha e lixo eletrônico. A solução permite que o usuário informe seu CEP e visualize pontos de coleta próximos, com informações fornecidas sobre cada local. A proposta busca contribuir para a conscientização ambiental e facilitar o acesso a locais de descarte adequados.

## Definição do Problema  
Grande parte da população não sabe onde descartar corretamente resíduos que não podem ir no lixo comum, como eletrônicos, pilhas e óleo usado. O resultado é o descarte incorreto, que contamina o solo, a água e causa impactos ambientais graves.  
Esse problema atinge tanto o cidadão, que carece de informações acessíveis, quanto a sociedade em geral, que sofre com os efeitos da poluição.

## Objetivos  
- Criar uma plataforma digital que mostre pontos de coleta próximos ao usuário.  
- Fornecer informações claras sobre quais tipos de resíduos cada ponto aceita.  
- Facilitar a busca pelo CEP e a visualização em mapa interativo.  
- Promover a conscientização ambiental através da tecnologia.

## Stack Tecnológico  
Para o desenvolvimento da aplicação foram escolhidas tecnologias acessíveis e de fácil integração:  
- Frontend: HTML, CSS e JavaScript, para construção das interfaces de usuário.  
- Backend: Python com Flask (ou Node.js como alternativa), para gerenciar rotas e requisições.  
- Banco de Dados: MySQL ou SQLite, para armazenar informações dos pontos de coleta.  
- APIs de Mapas: Google Maps ou Leaflet, para exibir a localização geográfica dos pontos.

## Descrição da Solução  
O sistema será dividido em duas partes principais:

1. **Área do usuário**: onde será possível digitar o CEP e encontrar pontos de coleta próximos. O mapa exibirá os locais cadastrados e mostrará informações como endereço, resíduos aceitos e horário de funcionamento.  
2. **Área de administração**: destinada ao cadastro e atualização dos pontos de coleta (CRUD básico).

## Arquitetura  
A arquitetura seguirá o modelo cliente-servidor. O frontend fará as requisições ao backend, que consultará o banco de dados e retornará os pontos de coleta correspondentes. O mapa será integrado ao frontend, consumindo uma API de geolocalização.

## Validação  
A validação inicial será feita com casos de teste simples:  
- Procurar um CEP válido e confirmar que os pontos próximos aparecem no mapa.  
- Verificar se os pontos de coleta cadastrados exibem as informações corretas.  
- Testar o CRUD de pontos (inserção, edição e exclusão).

## Estratégia  
A estratégia de desenvolvimento seguirá entregas incrementais:  
1. Montagem do ambiente e repositório.  
2. Protótipo das telas principais.  
3. Implementação de backend e banco de dados.  
4. Integração do mapa.  
5. Testes e ajustes finais.

## Conclusões  
O projeto busca unir tecnologia e sustentabilidade, oferecendo uma ferramenta prática para resolver um problema real: o descarte inadequado de resíduos. Além de ajudar os usuários, a solução pode ser ampliada e utilizada por organizações e prefeituras, tornando-se um recurso de impacto social e ambiental positivo.

## Referências  
- Documentação da API do Google Maps  
- Leaflet.js — Biblioteca Open Source para mapas interativos  
- Ministério do Meio Ambiente — Materiais sobre coleta seletiva e descarte correto  
