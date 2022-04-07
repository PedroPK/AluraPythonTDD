#Principal.py
#from google.colab import drive # Import a library named google.colab
#drive.mount('/content/drive/', force_remount=True) # mount the content to the directory `/content/drive`
#print ('\n')

# Uncomment these lines below in the First execution
'''
# Change the Folder
%cd /content/drive/MyDrive/Alura/Python/TDD/testes-python-projeto-inicial/src/leilao

# Print the actual folder
!pwd

# Copy a File to Colab/Research
!cp /content/drive/MyDrive/Alura/Python/TDD/testes-python-projeto-inicial/src/leilao/dominio.py
'''

from Auction          import Leilao
from Bid              import Lance
from User             import Usuario
from AuctionEvaluator import AuctionEvaluator

guilherme = Usuario("Guilherme")
yuri      = Usuario("Yuri")

lance_guilherme   = Lance(guilherme,  150.0)
lance_yuri        = Lance(yuri,       100.0)

leilao = Leilao("celular")

leilao.propose(lance_yuri)
leilao.propose(lance_guilherme)


for lance in leilao.lances:
  print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')

evaluator = AuctionEvaluator()
evaluator.evaluate(leilao)

print(f'O menor lance foi de {evaluator.smaller_bid} e o maior foi de {evaluator.bigger_bid}')