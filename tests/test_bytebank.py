from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_receber_13_03_2000_deve_retornar_25_em_2025(self):
        entrada = '13/03/2000' #Given -Contexto
        esperado = 25

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() #When -ação

        assert resultado == esperado #Then-desfecho