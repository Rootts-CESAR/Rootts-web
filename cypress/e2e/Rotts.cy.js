/// <reference types="cypress" />

describe(`Validate Rootts APP`, () => {
  before(() => {
    cy.viewport(1920, 1080);
    cy.visit('http://localhost:8000');
    
    Cypress.on("uncaught:exception", () => false);
    
    Cypress.Cookies.preserveOnce("JSESSIONID", "XSRF-TOKEN");
  });

  beforeEach(() => {
    cy.viewport(1920, 1080);
  })
  
  after(() => {
    cy.clearLocalStorage();
    cy.clearCookies();
  });
  
  describe("Validar História sem Login", () => {
    afterEach(function () {
      if (this.currentTest.state === "failed") {
        Cypress.runner.stop();
      }
    });

    after(() => {
      cy.clearLocalStorage();
      cy.clearCookies();
    });

    it("Validar Contatar Emergencia", () => {
      cy.xpath(`//a[contains(@class, 'btn btn-outline-danger')]`).scrollIntoView().should('be.visible');
    });
    
    it("Valida Reportar um problema", () => {
      var url = cy.url();
      cy.get(".row > :nth-child(2) > .btn").click();
      cy.url().should("not.eq", url);

      cy.get("h1").should("have.text", "Reportar Problema");

      cy.get("#id_nome").should("exist").and("be.visible");
      cy.get("#id_nome").type("Problema Teste Automatico");

      cy.get("#id_endereco").should("exist").and("be.visible");
      cy.get("#id_endereco").type("Rua Endereço Teste Automatico");

      cy.get("#id_data").should("exist").and("be.visible");
      cy.get("#id_data").type("2022-11-11");

      cy.get("#id_titulo").should("exist").and("be.visible");
      cy.get("#id_titulo").type("Titulo Teste Automatico");

      cy.get("#id_descricao").should("exist").and("be.visible");
      cy.get("#id_descricao").type("Descrição de Teste Automatico");

      cy.get('[type="submit"]').should("exist").and("be.visible");
      cy.get('[type="submit"]').click();

      cy.get("strong").should(
        "have.text",
        "Seu relatório foi feito com sucesso"
      );
      cy.get("#image").click();
    });

    it("Validar Visualizar encosta", () => {
      var url = cy.url();
      cy.get(".row > :nth-child(3) > .btn")
        .should("exist")
        .and("be.visible")
        .click();
      cy.url().should("not.eq", url);

      cy.get("thead > tr > :nth-child(1)").should("have.text", "Nome");
      cy.get("thead > tr > :nth-child(2)").should("have.text", "Localização");
      cy.get("thead > tr > :nth-child(3)").should(
        "have.text",
        "Risco de Deslizamento"
      );
    });

    it("Validar pesquisar uma Encosta", () => {
      cy.get("#form12").should("be.visible").type("Encosta");
      cy.get("#form12").type("{enter}");

      cy.get("tbody > tr > :nth-child(1)").should('be.visible')
      cy.get("#image").click();
    });
  });

  describe("Validar História com Login Usuario", () => {
    before(() => {
      cy.get('[href="/login/"] > .btn').click();

      cy.get("#username")
        .should("exist")
        .and("be.visible")
        .click()
        .type("TesteAutomatico");
      cy.get("#password")
        .should("exist")
        .and("be.visible")
        .click()
        .type("Teste123Ab@");
      cy.get(".btn").should("exist").and("be.visible").click();

    });

    after(() => {
      cy.clearLocalStorage();
      cy.clearCookies();
    })



    it("Valida Reportar um problema", () => {
      var url = cy.url();
      cy.get(".row > :nth-child(2) > .btn").click();
      cy.url().should("not.eq", url);

      cy.get("h1").should("have.text", "Reportar Problema");

      cy.get("#id_nome").should("exist").and("be.visible");
      cy.get("#id_nome").type("Teste Automatico Autenticado");

      cy.get("#id_endereco").should("exist").and("be.visible");
      cy.get("#id_endereco").type("Rua Endereço Teste Automatico");

      cy.get("#id_data").should("exist").and("be.visible");
      cy.get("#id_data").type("2022-11-11");

      cy.get("#id_titulo").should("exist").and("be.visible");
      cy.get("#id_titulo").type("Titulo Teste Automatico");

      cy.get("#id_descricao").should("exist").and("be.visible");
      cy.get("#id_descricao").type("Descrição de Teste Automatico");

      cy.get('[type="submit"]').should("exist").and("be.visible");
      cy.get('[type="submit"]').click();

      cy.get("strong").should(
        "have.text",
        "Seu relatório foi feito com sucesso"
      );
      cy.get("#image").click();
    });

    it("Validar Visualizar encosta", () => {
      var url = cy.url();
      cy.get(".row > :nth-child(3) > .btn")
        .should("exist")
        .and("be.visible")
        .click();
      cy.url().should("not.eq", url);

      cy.get("thead > tr > :nth-child(1)").should("have.text", "Nome");
      cy.get("thead > tr > :nth-child(2)").should("have.text", "Localização");
      cy.get("thead > tr > :nth-child(3)").should(
        "have.text",
        "Risco de Deslizamento"
      );
    });

    it("Validar pesquisar uma Encosta", () => {
      cy.get("#form12").should("be.visible").type("Encosta");
      cy.get("#form12").type("{enter}");

      cy.get("tbody > tr > :nth-child(1)").should('be.visible');
      cy.get("#image").click();
    });
  });


  describe("Validar História do Engenheiro", () => {
    before(() => {
      cy.get('[href="/login/"] > .btn').click();

      cy.get("#username")
        .should("exist")
        .and("be.visible")
        .click()
        .type("Engautomatico");
      cy.get("#password")
        .should("exist")
        .and("be.visible")
        .click()
        .type("Teste123Ab@");
      cy.get(".btn").should("exist").and("be.visible").click();


      Cypress.Cookies.preserveOnce("csrftoken", "sessionid");
    });

    beforeEach(() => {
      Cypress.Cookies.preserveOnce("csrftoken", "sessionid");
    })

    after(() => {
      cy.clearLocalStorage();
      cy.clearCookies();
    })


    it("Validar Gerenciar encostas", () => {
      cy.get('.row > :nth-child(1) > .btn').should("exist").and("be.visible").click();
      
      cy.get('[style="margin-left: 15px;"]').should("be.visible")
      cy.get(':nth-child(1) > :nth-child(4) > .btn-sm').should("exist").and("be.visible")
      cy.get(':nth-child(1) > .buttons > .btn-warning').should("exist").and("be.visible")
      cy.get(':nth-child(1) > .buttons > .btn-danger').should("exist").and("be.visible")
      cy.get('.btn').should("exist").and("be.visible")
    })

    it("Validar Visualizar Encosta", () => {
      cy.get(':nth-child(1) > :nth-child(4) > .btn-sm').click()

      cy.get('h3').should("be.visible")

      cy.get('thead > tr > :nth-child(1)').should("have.text", "Latitude")
      cy.get('thead > tr > :nth-child(2)').should("have.text", "Longitude")
      cy.get('thead > tr > :nth-child(3)').should("have.text", "Declividade")
      cy.get('thead > tr > :nth-child(4)').should("have.text", "Construções por m²")
      cy.get('thead > tr > :nth-child(5)').should("have.text", "Coef. Umidade")
      cy.get('thead > tr > :nth-child(6)').should("have.text", "Redes Viarias por m²")
      cy.get('thead > tr > :nth-child(7)').should("have.text", "Corpos Liquidos por m²")
      cy.get('thead > tr > :nth-child(8)').should("have.text", "Nível de Risco de Deslizamento")

      cy.get('.btn').should("be.visible").and("have.text", "Voltar").click()
    })

    it("Validar Editar Encosta", () => {
      cy.get(':nth-child(1) > .buttons > .btn-warning').click()

      cy.get('[for="id_declividade"]').should("be.visible")
      cy.get('[for="id_numeroConstrucoes"]').should("be.visible")
      cy.get('[for="id_coeficienteUmidade"]').should("be.visible")
      cy.get('[for="id_proximidadeRedeViarias"]').should("be.visible")
      cy.get('[for="id_proximidadeCorposLiquidos"]').should("be.visible")
      cy.get('[for="id_prioridadeEncosta"]').should("be.visible")

      cy.get('.btn-primary').should("be.visible").and("have.text", "Salvar").click()
    })

    it("Validar Adicionar Encosta", () => {
      cy.get('.btn').should("be.visible").and("have.text", "Adicionar encosta").click()

      cy.get('#id_nome').type("Encosta Automatica")
      cy.get('#id_local').type("Local Recife Automatico")
      cy.get('#id_latitude').type("1.3451")
      cy.get('#id_longitude').type("1.3451")
      cy.get('#id_declividade').type("1.3451")
      cy.get('#id_numeroConstrucoes').type("1.3451")
      cy.get('#id_coeficienteUmidade').type("1.3451")
      cy.get('#id_proximidadeRedeViarias').type("1.3451")
      cy.get('#id_proximidadeCorposLiquidos').type("1.3451")
      cy.get('#id_prioridadeEncosta').select("Baixo")
      cy.get('.btn-primary').should("be.visible").and("have.text", "Salvar").click()
    })

    it("Validar Excluir Encosta", () => {
      cy.get(':nth-child(1) > .buttons > .btn-danger').click()
      cy.get('[method="post"] > .text-light').should("be.visible")

      cy.get('[href="/crud/"]').should("be.visible")
      cy.get('.btn-danger').should("be.visible").and("have.text", "Confirmar").click()
    })

    it("Validar Pesquisar Encosta", () => {
      cy.get('#form12').type("Encosta")
      cy.get('#form12').type("{enter}")

      cy.get('tbody > tr > :nth-child(2)').should('be.visible')
      cy.get('#image').click()
    })

    it("Validar Gerenciar Reports", () => {
      cy.get(':nth-child(2) > .btn').should("exist").and("be.visible").click();
      cy.get('[style="font-size: 30px"]').should("be.visible")
      
      cy.get('[type="submit"]').should("exist").and("be.visible")
    })

    it("Validar Visualizar Report", () => {
      cy.xpath(`(//div[contains(@class, 'main-content')]//h2[contains(. , 'Teste Automatico')]//..//..//a[contains(@class, 'btn-sm btn-warning margin')])[1]`).click()

      cy.get('h3').should("be.visible")
      cy.get('[scope="col"]').should("be.visible")

      cy.get('.btn').should("be.visible").and("have.text", "Voltar").click()
    })

    it("Validar Descartar Report", () => {
      cy.xpath(`(//div[contains(@class, 'main-content')]//h2[contains(. , 'Teste Automatico')]//..//..//a[contains(@class, 'btn-sm btn-danger')])[1]`).click()

      cy.get('[method="post"] > .text-light').should("be.visible")

      cy.get('[href="/Engenheiro_formulario/"]').should("be.visible")
      cy.get('.btn-danger').should("be.visible").and("have.text", "Confirmar").click()

    })

    it("Validar Aprovar Report", () => {
      cy.xpath(`(//div[contains(@class, 'main-content')]//h2[contains(. , 'Teste Automatico')]//..//..//label[contains(@id, 'label')]//span[contains(. , 'Aprovar')])[1]`).should("not.be.checked").click()
      cy.xpath(`(//div[contains(@class, 'main-content')]//h2[contains(. , 'Teste Automatico')]//..//..//label[contains(@id, 'label')]//span[contains(. , 'Aprovado')])[1]`).should("be.visible")

      cy.get('[type="submit"]').click()
      cy.get('[style="font-size: 30px"]').should("be.visible").and('have.text', 'Reportes Aprovados');
      cy.get('.btn').should("be.visible").and("have.text", "Pendentes")

      cy.get(':nth-child(1) > :nth-child(1) > h2').should("be.visible")
      cy.get(':nth-child(1) > :nth-child(2) > h2').should("be.visible")

      cy.get(':nth-child(1) > .buttons > .box > .btn-warning').should("be.visible").and("have.text", "Visualizar")
      cy.get(':nth-child(1) > .buttons > .box > .btn-danger').should("be.visible").and("have.text", "Descartar")

      cy.get(':nth-child(1) > .buttons > h4').should("be.visible")

      cy.get('#image').click()
    })

  });

});
