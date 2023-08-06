from BancoCorrente import ContaCorrente, CartaoCredito
from Agencia import Agencia, AgenciaVirtual, AgenciaComum, AgenciaPremium

# programa
conta_Lira = ContaCorrente("Lira", "111.222.333-45", 1234, 34062)

cartao_Lira = CartaoCredito('Lira', conta_Lira)

conta_Lira.nome = "João Lira"
print(conta_Lira.nome)

cartao_Lira.senha = '2345'
print(cartao_Lira.senha)


agencia1 = Agencia(22223333, 2000000000, 4568)

agencia1.caixa = 1000000

agencia1.verificar_caixa()

agencia1.emprestar_dinheiro(1500, 123456489454, 0.02)
print(agencia1.emprestimos)

agencia1.adicionar_cliente('Lira',12345678912, 10000)
print(agencia1.clientes)

agencia_virtual = AgenciaVirtual('www.agencia.com.br', 22224444, 152000000)
agencia_virtual.verificar_caixa()
print(agencia_virtual.site)

agencia_comum = AgenciaComum(22225555, 25500000000)
agencia_comum.verificar_caixa()

agencia_premium = AgenciaPremium(222266666, 2354222222222)
agencia_premium.verificar_caixa()

agencia_virtual.depositar_paypal(20000)
print(agencia_virtual.caixa)
print(agencia_virtual.caixa_paypal)