<h1>(PTBR) <a href = "https://rootts.herokuapp.com" target = "Rootts: notificador de risco de deslizamento"</a></h1>

<h2>Equipe:</h2>

<ul>
<li><a href = "https://www.linkedin.com/in/arthur-hendrich-b30885153/" target = "_blank">Arthur Hendrich Alencar de Menezes</a></li> (Líder Frontend);
<li><a href = "https://www.linkedin.com/in/matheus-lazzarotto/" target = "_blank">Matheus Vilaverde Lazzarotto</a></li> (Líder Backend);
<li><a href = "https://www.linkedin.com/in/luis-adolfo-araujo-703a721aa/" target = "_blank">Luis Adolfo Alves De Araújo Neto</a></li> (Líder Mobile);
<li><a href = "https://www.linkedin.com/in/rafael-falk/" target = "_blank">Rafael Martins Falk</a></li> (Frontend);
<li><a href ="https://www.linkedin.com/in/isaacmagl/" target = "_blank">Samuel Isaac de Melo Magalhães</li></a></li> (Frontend);
<li><a href ="https://www.linkedin.com/in/rafael-falk/" target = "_blank">Rafael Martins Falk</li></a></li> (Frontend);
<li><a href = "https://www.linkedin.com/in/davi-aleixo-548b55b8/" target = "_blank">Davi Aleixo Carvalho</a></li> (Backend);
<li><a href = "https://www.linkedin.com/in/lucas-rocha-603683246/" target = "_blank">Lucas Duarte Freitas Rocha</a></li> (Mobile);
</ul>
<h2> O que é o projeto? </h2>
  
<p>Um site que opera como notificador de risco de deslizamento, baseado num banco de dados que deve ser capaz de ser alimentado tanto por um artefato pluviométrico como informações relevantes ao cálculo de risco de deslizamento de encostas. <b>Nesta primeira iteração e para os propósitos da disciplina de Fundamentos de Desenvolvimento de Software, iremos nos restringir a usar um banco de dados que funciona apenas com entrada manual de dados, sem o uso do pluviometro.</b></p>

<h2> Como o projeto funciona? </h2>
<p>Iremos utilizar um banco de dados local via SQLite. Os dados dentro deste banco devem ser lidos e interpretados pela aplicação avaliando o risco de deslizamento em um dado local, enviando notificações caso necessário. O artefato pluviométrico deve conferir entrada automática de valores referentes ao volume de chuva (lembrando que o pluviometro ainda não será incorporado nesta iteração do projeto). Já as informações relevantes ao cálculo de risco devem ser inseridas no sistema manualmente ao catalogar uma determinada encosta.</p>

<p>Sem fazer login, o usuário pode acessar perguntas frequentes (F.A.Q.), além dos contatos habituais da Defesa Civil e serviços adjacentes. Existem duas opções de login: login como civil e login como engenheiro.</p>

<p>Como civil, o usuário pode enviar um relatório contendo informações de localização, a natureza da ocorrência e possivelmente fazer <i>upload</i> de imagens ou vídeos do incidente. Como engenheiro, o usuário pode conferir os relatórios enviados por civis em uma página que diferencia entre relatórios pendentes, aprovados e descartados. Além disso, o engenheiro pode gerenciar (criar, ler, atualizar e excluir) encostas e suas variáveis no banco de dados.</p>

<h2> Por que o projeto é útil? </h2>
<p>De um lado, a digitalização da captação e organização de dados referente a encostas em risco de deslizamento apresenta uma melhoria em relação ao método atual de armazeno e manejo de dados, ainda feito no papel pela Defesa Civil (CODECIR (2012), pp. 45). Do outro, o artefato pluviométrico apresenta uma alternativa precisa para a avaliação de risco de uma encosta em tempo real.</p>

<h2>Ferramentas utilizadas:</h2>

Backend:
<ul> 
  <a href= https://www.sqlite.org/docs.html><img src="https://img.shields.io/badge/SQLite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white"/></a><br>
  <a href= https://www.djangoproject.com/><img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/></a>
</ul>

Frontend:
<ul> 
  <a href= https://getbootstrap.com/><img src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"/></a>
</ul>

<br>
<h1>(ENG) Rootts: landslide risk notifier</h1>
<h2>Team:</h2>

<ul>
<li><a href = "https://www.linkedin.com/in/arthur-hendrich-b30885153/" target = "_blank">Arthur Hendrich Alencar de Menezes</a></li> (Lead Frontend);
<li><a href = "https://www.linkedin.com/in/matheus-lazzarotto/" target = "_blank">Matheus Vilaverde Lazzarotto</a></li> (Lead Backend);
<li><a href = "https://www.linkedin.com/in/luis-adolfo-araujo-703a721aa/" target = "_blank">Luis Adolfo Alves De Araújo Neto</a></li> (Lead Mobile);
<li><a href = "https://www.linkedin.com/in/rafael-falk/" target = "_blank">Rafael Martins Falk</a></li> (Frontend);
<li><a href ="https://www.linkedin.com/in/isaacmagl/" target = "_blank">Samuel Isaac de Melo Magalhães</li></a></li> (Frontend);
<li><a href ="https://www.linkedin.com/in/rafael-falk/" target = "_blank">Rafael Martins Falk</li></a></li> (Frontend);
<li><a href = "https://www.linkedin.com/in/davi-aleixo-548b55b8/" target = "_blank">Davi Aleixo Carvalho</a></li> (Backend);
<li><a href = "https://www.linkedin.com/in/lucas-rocha-603683246/" target = "_blank">Lucas Duarte Freitas Rocha</a></li> (Mobile);
</ul>
<h2> What is the project? </h2>
  
<p>A website that operates as a landslide risk notifier, relying on a database that must be able to be feed by a pluviometric artefact and by information pertaining to the calculation of landslide risk. <b>In this first iteration and for the purposes of the Foundations of Software Engineering class, we will be utilizing a local database that works only with manual input of data, without the use of the pluviometric artefact.</b></p>

<h2> How does the project work? </h2>
<p>We will use a local database via SQLite. The data within this database must be read and interpreted by the application, assessing the risk of landslides in a given location, sending notifications if necessary. The pluviometric artifact must provide automatic entry of values referring to the volume of rain (as it was said, the pluviometric artefact will not be integrated into this iterarion of the project). The information relevant to the risk calculation must be manually entered into the system when cataloging a particular slope.</p>

<p>Without logging in, the user can acess frequently asked questions (F.A.Q.), in addition to the usual contacts for Civil Defense and adjacent services. There are two login options: login as civilian and login as engineer.</p>

<p>As a civilian, the user can submit a report containing location information, the nature of the occurrence and possibly uploading images or videos of the incident. As an engineer, the user can check the reports sent by civilians on a page that differentiates between pending, approved, and discarded reports. Furthermore, the engineer can manage (create, read, update and delete) slopes in the database.</p>


<h2> How is the project useful? </h2>
<p>On the one hand, the digitization of the capture and organization of data referring to slopes at risk of landslides presents an improvement in relation to the current method of storing and managing data, still done on paper by the Civil Defense (CODECIR, 2012, pp 45). On the other hand, the pluviometric artifact presents an accurate alternative for the risk assessment of a slope in real time.</p>

<h2>Tools utilized:</h2>

Backend:
<ul> 
  <a href= https://www.sqlite.org/docs.html><img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white"/></a><br>
  <a href=[ https://flask.palletsprojects.com/en/2.2.x/](https://www.djangoproject.com/)><img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/></a>
</ul>

Frontend:
<ul> 
  <a href= https://getbootstrap.com/><img src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"/></a>
</ul>

<h2>Referências/References</h2>

<p>CODECIR, "Avaliação das Ações de Prevenção de Deslizamento de Encostas (AADPE)", 2012. 
  Disponível em: https://www.tce.pe.gov.br/internet/docs/anop/2543/microsoft-word-relat-auditoria-codecir-pcr-proc-1002037-8-consolidado.pdf</p>
