# Criar uma conta no Google Cloud (cloud.google.com).
# Clicar em Compute Engine > Instâncias de VM.
# Após isto, clicar em Criar.
# Depois, nomear a VM, escolho Região como us-central1 (iowa), Configuração de Máquina em E2, Tipo de Máquina e2-medium- (2 vCPU, 1 núcleos, 4 gb Memória), Disco de Inicialização clicar em Mudar (escolher Sistema: Ubuntu, Versão 20.04 LTS x86/64, amd64 focal image, Tipo de Disco permanente equilibrado, Tamanho 10gb, depois clicar em SELECIONAR.).
# Em Firewall, clicar em: "Permitir tráfego HTTP" e "Permitir tráfego HTTPS".
# Feito isso tudo, clique em CRIAR.
# Clique em cima do nome da VM (no meu caso, djangodeploy) e em Interfaces de Rede analise o ip interno primário e o Endereço IP Externo. Neste mesmo campo role para o lado e em Detalhes de Rede clique em Mais detalhes.
# Agora você estará em Rede VPC, clique em Endereços Ip.
# Na aula, no final do canto onde há o endereço ip externo há o botão Reservar (mas não achei). Então, leia abaixo.
# Havia três pontinhos e a opção de "Promover a endereço ip estático". Isso mesmo, agora precisamos informar NOME (que será djangodeploy). Deu tudo certo. ;-)
# 
