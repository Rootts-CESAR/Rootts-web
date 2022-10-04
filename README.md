# (PT-BR) [Rootts: notificador de risco de deslizamento](https://rootts.herokuapp.com)

## Equipe:

* [Arthur Hendrich Alencar de Menezes](https://www.linkedin.com/in/arthur-hendrich-b30885153/) (Líder Frontend);
* [Matheus Vilaverde Lazzarotto](https://www.linkedin.com/in/matheus-lazzarotto/) (Lider Backend);
* [Luis Adolfo Alves De Araújo Neto](https://www.linkedin.com/in/luis-adolfo-araujo-703a721aa/) (Backend);
* [Rafael Martins Falk](https://www.linkedin.com/in/rafael-falk/) (Frontend);
* [Samuel Isaac de Melo Magalhães](https://www.linkedin.com/in/isaacmagl/) (Frontend);
* [Davi Aleixo Carvalho](https://www.linkedin.com/in/davi-aleixo-548b55b8/) (Backend);
* [Lucas Duarte Freitas Rocha](https://www.linkedin.com/in/lucas-rocha-603683246/) (Backend);

## O que é o projeto?
  
Um site que opera como notificador de risco de deslizamento, baseado num banco de dados que deve ser capaz de ser alimentado tanto por um artefato pluviométrico como informações relevantes ao cálculo de risco de deslizamento de encostas. **Nesta primeira iteração e para os propósitos da disciplina de Fundamentos de Desenvolvimento de Software, iremos nos restringir a usar um banco de dados que funciona apenas com entrada manual de dados, sem o uso do pluviometro.**

## Como o projeto funciona?
Iremos utilizar um banco de dados local via SQLite. O banco deve guardar variáveis relevantes no cálculo de risco de deslizamento de encostas, enviando notificações caso a variável de risco que varia entre 1 (menor risco) e 4 (maior risco) aumente. O artefato pluviométrico deve conferir entrada automática de valores referentes ao volume de chuva **(lembrando que o pluviometro ainda não será incorporado nesta iteração do projeto)**. Já as informações relevantes ao cálculo de risco devem ser inseridas no sistema manualmente ao catalogar uma determinada encosta.

## Funcionalidades atuais:
Sem fazer login, o usuário pode acessar perguntas frequentes (F.A.Q.), além dos contatos habituais da Defesa Civil e serviços adjacentes. Existem duas opções de login: login como civil e login como engenheiro.

Como civil, o usuário pode enviar um relatório contendo informações de localização, a natureza da ocorrência e possivelmente fazer *upload* de imagens ou vídeos do incidente. Como engenheiro, o usuário pode gerenciar (criar, ler, atualizar e excluir) encostas e suas variáveis no banco de dados.

## Por que o projeto é útil?
De um lado, a digitalização da captação e organização de dados referente a encostas em risco de deslizamento apresenta uma melhoria em relação ao método atual de armazeno e manejo de dados, ainda feito no papel pela Defesa Civil (CODECIR (2012), pp. 45). Do outro, o artefato pluviométrico apresenta uma alternativa precisa para a avaliação de risco de uma encosta em tempo real.

## Requerimentos
1. Instale o Python.

    ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  
2. Instale o Git.

    ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

3. Abra o terminal e clone o nosso [repositório](https://github.com/Rootts-CESAR/Rootts-web):
```
git clone https://github.com/Rootts-CESAR/Rootts-web
```
4. Em seguida, instale os requerimentos:
```
python -m pip install -r requirements.txt
```

5. Com os requerimentos instalados, inicie o servidor:
```bash 
python manage.py runserver
```

6. `Ctrl + left mouse click` no endereço do servidor local para acessá-lo.

## Ferramentas utilizadas

Backend:
<ul> 
  <a href= ><img src="https://img.shields.io/badge/SQLite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white"/></a><br>
  <a href= https://www.djangoproject.com/><img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/></a>
</ul>

Frontend:
<ul> 
  <a href= https://getbootstrap.com/><img src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"/></a>
</ul>


# (ENG) [Rootts: landslide risk notifier](https://rootts.herokuapp.com)

## Team:

* [Arthur Hendrich Alencar de Menezes](https://www.linkedin.com/in/arthur-hendrich-b30885153/) (Lead Frontend);
* [Matheus Vilaverde Lazzarotto](https://www.linkedin.com/in/matheus-lazzarotto/) (Lead Backend);
* [Luis Adolfo Alves De Araújo Neto](https://www.linkedin.com/in/luis-adolfo-araujo-703a721aa/) (Backend);
* [Rafael Martins Falk](https://www.linkedin.com/in/rafael-falk/) (Frontend);
* [Samuel Isaac de Melo Magalhães](https://www.linkedin.com/in/isaacmagl/) (Frontend);
* [Davi Aleixo Carvalho](https://www.linkedin.com/in/davi-aleixo-548b55b8/) (Backend);
* [Lucas Duarte Freitas Rocha](https://www.linkedin.com/in/lucas-rocha-603683246/) (Backend);
## What is the project?
  
A website that operates as a landslide risk notifier, relying on a database that must be able to be feed by a pluviometric artefact and by information pertaining to the calculation of landslide risk. **In this first iteration and for the purposes of the Foundations of Software Engineering class, we will be utilizing a local database that works only with manual input of data, without the use of the pluviometric artefact.**

## How does the project work?
We will use a local database via SQLite. The database must keep relevant variables in the calculation of risk of landslides on slopes, sending notifications if the risk variable that varies between 1 (lowest risk) and 4 (highest risk) increases. The pluviometric artifact must provide automatic entry of values referring to the volume of rain (as it was said, the pluviometric artefact will not be integrated into this iterarion of the project). The information relevant to the risk calculation must be manually entered into the system when cataloging a particular slope.

## Present functionalities
Without logging in, the user can access frequently asked questions (F.A.Q.), in addition to the usual contacts for Civil Defense and adjacent services. There are two login options: login as civilian and login as engineer.

As a civilian, the user can submit a report containing location information, the nature of the occurrence and possibly uploading images or videos of the incident. As an engineer, the user can manage (create, read, update and delete) slopes in the database.


## How is the project useful?
On the one hand, the digitization of the capture and organization of data referring to slopes at risk of landslides presents an improvement in relation to the current method of storing and managing data, still done on paper by the Civil Defense (CODECIR, 2012, pp 45). On the other hand, the pluviometric artifact presents an accurate alternative for the risk assessment of a slope in real time.

## Requeriments
1. Install Python.

    ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

2. Install Git.

    ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

3. Clone our [repository](https://github.com/Rootts-CESAR/Rootts-web):
```
git clone https://github.com/Rootts-CESAR/Rootts-web
```
4. Install requeriments.txt via terminal:
```
python -m pip install -r requirements.txt
```

5. Launch the server:
```bash 
python manage.py runserver
```

6. `Ctrl + left mouse click` in the local server adress to access it.

## Tools utilized

Backend:
<ul> 
  <a href= https://www.sqlite.org/docs.html><img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white"/></a><br>
  <a href=[ https://flask.palletsprojects.com/en/2.2.x/](https://www.djangoproject.com/)><img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/></a>
</ul>

Frontend:
<ul> 
  <a href= https://getbootstrap.com/><img src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"/></a>
</ul>

## Referências/References

<p>CODECIR, "Avaliação das Ações de Prevenção de Deslizamento de Encostas (AADPE)", 2012. 
  Disponível em: https://www.tce.pe.gov.br/internet/docs/anop/2543/microsoft-word-relat-auditoria-codecir-pcr-proc-1002037-8-consolidado.pdf</p>
