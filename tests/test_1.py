from main import tratar_nome

def test_tratamento_nome():
    retorno_esperado = "Guilherme Cavalcante"

    assert tratar_nome("guilherme cavalcante") == retorno_esperado