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
