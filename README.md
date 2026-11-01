# projeto-DarMais

## Descrição do sistema:
O projeto DarMais é um sistema de doação que permite ao usuário divulgar seus pedidos de urgência na plataforma. O sistema conta também com a divulgação de instituições e seus projetos sociais, alem de também disponibilizar a opção de doar para ONGS que realizam trabalhos humanitários para a nossa sociedade.

## Entidades do sistema:
Usuarios
<br>
Doacao
<br>
Instituicao
<br>
Ong
<br>
Beneficiario
<br>
PedidoDeAjuda
<br>
ProjetoSocial

## Explicação do relacionamento 1:N ;
### Usuários e Doações -
&nbsp; O relacionamento entre essas tabelas se caracteriza como Um para Muitos, pois um usuário pode realizar várias doações, entretanto cada doação só pode ser vinculada a um único usuário. Essa relação permite registrar a quantidade de doações que cada usuário realizou, auxiliando no processo de organização de informações sobre as doações.

### Instituição e Pedidos de Ajuda -
&nbsp; O relacionamento entre essas tabeelas se caracteriza como Um para Muitos, pois uma instituição pode ser ligada a vários pedidos de ajuda, enquanto cada pedido está vinculado a somente uma instituição. Essa relação permite registrar a quantidade de pedidos de ajuda associados às instituições, contribuindo para que o sistema possa organizar e exibir de maneira correta as informações sobre os pedidos.

### ONGs e Projetos Sociais - 
&nbsp; O relacionamento entre essas tabelas se caracteriza como Um para Muitos, pois uma ONG pode desenvolver vários projetos sociais e cadastrar no banco de dados, enquanto cada projeto só pode estar associado a uma única ONG. Essa relação permite registrar a quantidade de projetos sociais que cada ONG realizou e cadastrou em nosso sistema, possibilitando uma maior clareza para os usuários que pretendem procurar informações e uma visibilidade para os trabalhos sociais das ONGs

### ONGs e Doações -
&nbsp; O relacionamento entre essas tabelas se caracteriza como Um para Muitos, pois uma ONG pode receber várias doações, enquanto cada registro de doação pode estar associado a somente uma ONG. Essa relação permite registrar e acompanhar as doações que são destinada às organizações, auxiliando no processo de organização de informações sobre os recursos recebidos.

### Pedidos de Ajuda e Beneficiários - 
&nbsp; O relacionamento entre essas tabelas se caracteriza como Um para Muitos, pois um pedido de ajuda pode estar associado à vários beneficiários, enquanto cada beneficiário só pode estar associado a um pedido de ajuda. Essa relação permite organizar, no sistema desenvolvido, as informações sobre as pessoas beneficiadas pelas solicitações, contribuindo para o acompanhamento de suas necessidades.

### Pedidos de Ajuda e Doações - 
&nbsp; O relacionamento entre essas tabelas se caracteriza como Um para Muitos, pois um pedido de ajuda pode receber várias doações, enquanto cada registro de doação só pode estar relacionada a um pedido de ajuda. Esse relacionamento permite organizar a quantidade de doações que cada pedido de ajuda irá receber, possibilitando dessa maneira uma maior clareza para os usuários e uma maior organização no sistema.
 
## Explicação do relacionamento N:N ;
### Usuários e ONGs por meio das Doações-
&nbsp; A relação entre essas duas tabelas se caracteriza como Muito para Muitos, pois um usuário pode realizar doações para diferentes ONGs, enquanto uma ONG pode receber doações de múltiplos usuários. Essa associação ocorre indiretamente por meio da tabela Doações, que funciona como intermediária e registra informações sobre cada contribuição. Dessa maneira, a plaforma consegue relacionar os doadores às ONGs beneficiadas e manter o histórico de doações.

## Instruções para instalar dependências;
pip install flask
<br>
pip install sqlalchemy

## Instruções para criar ou popular o banco;
usar a função popular_banco() no app.py logo abaixo de Base.metadata.create_all(engine)

## Instruções para executar o sistema;
execute no app.py

## Principais dificuldades encontradas;
Lidar com os relacionamentos na hora de puxar os dados no banco de dados, manter o padrão de segurança por se tratar de um código extenso, o seed.py foi funcionar no penúltimo dia de desenvolvimento e criar todos os blueprints para cada seção.

## Declaração de autoria:
Declaro que desenvolvi este projeto compreendendo o código entregue e que sou
capaz de explicar e modificar suas partes principais.
<br>
Uso de IA:
<br>
[ ] Não utilizei IA generativa.
[X] Utilizei IA generativa e descrevo abaixo onde e como foi utilizada.
<br>
No nosso projeto a inteligência artificial foi utilizada para gerar o html e o css, entretanto algumas partes do jinja em alguns templates foram feitos de maneira autoral, como todos os links no index.html, a checagem se o usuario está logado para exibir Ver seu perfil e Sair no base.html, além de muitos ajustes porque a IA foi incapaz de entregar os htmls com 100% de precisão.
