from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_receber_13_03_2000_deve_retornar_25_em_2025(self):
        entrada = '13/03/2000' #Given -Contexto
        esperado = 25

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() #When -ação

        assert resultado == esperado #Then-desfecho

    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_apenas_carvalho(self):
        entrada = ' Lucas Carvalho'
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome()

        assert resultado ==esperado

    def test_decrescimo_salario_recebe_10000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome ='Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome,'11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado


