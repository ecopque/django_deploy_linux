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
# No exemplo da aula, já constava as portas tcp: 80  e 443 liberadas, no meu não. No futuro provavelmente vou ter que CRIAR REGRAS DE FIREWALL.
# Agora vamos em COMPUTE ENGINE > INSTÂNCIAS DE VM e em CONFIGURAÇÕES > METADADOS vamos em CHAVES SSH e clicar em EDITAR. (voltaremos em breve).
# Vamos no terminal/bash e digitamos: ssh-keygen -C 'gnulinuxdebian'. Agora vai ser gerada uma chave (não mostre à ninguém). Vai aparecer uma confirmação de onde será salvo sua chave. Só dar ENTER. O endereço foi "/home/my_user/.ssh/id_rsa". Agora será solicitado uma senha. Decidi não usar senha alguma, apertei apenas ENTER. Pronto, suas chaves foram criadas.
# Agora vamos abrir com editor de texto o arquivo id_rsa.pub, pois o usaremos no Google.
# Ao abrir, selecione todo conteúdo e copie. 
# Agora lá em CHAVES SSH (METADADOS), vamos em ADICIONAR ITEM e colamos a chave SSH e depois clicamos em SALVAR.
# Agora vamos testar. No terminal digitaremos: ssh meu_usuario@ip_meu_servidor_externo (ssh gnulinuxdebian@34.28.163.xxx).
# Seu terminal vai questionar se quer continuar a conexão. Digite yes.
# Após isto, vai perceber que você está dentro do servidor. Em seu terminal vocÊ aparecerá assim: gnulinuxdebian@djangodeploy:~$.
