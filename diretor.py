import SysPonto
import validacoes
from datetime import datetime

def loginDiretor(cpf, nasc):
	if cpf in SysPonto.diretores and SysPonto[cpf][4] == nasc:
		print ("Diretor já cadastrado! ")
		return True
	else:
		return False
		
def menuDiretor():

	while validacoes.validaCPF(cpf) == False or validacoes.cpfExistenteDiretor(cpf) == False:
		print("CPF inválido.")
		cpf = input("Digite seu CPF: ")
	nasc = input("Digite o seu nascimento XX/XX/XXXX: ")
	validacoes.validaData(nasc)
	
	if loginDiretor(cpf, nasc) == True:
		escolha = input ("Digite 1 para registrar entrada. Digite 2 para registrar saída.\n")
		if escolha == '1':
			print("Entrada registrada.")
			cpfreg = cpf
			hora = data()
			choose = 'Entrada'
		elif escolha == '2'
			print("Saída registrada.")
			cpfreg = cpf
			hora = data()
			choose = 'Saída'
		else:
			print("Opção inválida.")
	SysPonto.Historico[cpf] = [cpfreg, hora, choose]
	
def data()
	now = datetime.now()
	return now
	
	
