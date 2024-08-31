# Baixamos o gunicorn.txt para utilizar em nosso servidor (e passo a passo).
# Devemos substituir os arquivos marcados no início do arquivo, como __FUNICORN_FILE_NAME_-, etc.
# No VS Code, marcamos o nome que queremos substituir e com "ctrl + f" vai aparecer uma caixinha de pesquisa no topo, clicamos na setinha para baixo e em "replace" escolhemos o nome que queremos (veja o arquivo abaixo para ver o resultado final) e por fim clicamos no último ícone da direita (replace all).
# Em __YOUR_USERNAME__, vá no servidor/terminal e digite "whoami" para saber seu user. Neste caso, gnulinuxdebian.
# Em __APP_ROOT_NAME__, temos que colocar o diretório de nossa agenda, neste caso scheduleapp.
# Em __WSGI_FOLDER_NAME__, é a pasta "Projeto" dentro do nosso projeto, no meu caso, "schedule" (my_project/schedule/). Se você der um "ls schedule" dentro do diretório do servidor (scheduleapp), vai ver o arquivo "wsgi.py".
# Perceba que agora dentro do arquivo gnucorn.txt os diretórios foram formados, como home/gnulinuxdebian/scheduleapp/... Lindo! ;-)
# Agora que o arquivo está criado, vamos criar o arquivo agenda.socket.
# No servidor/terminal, digite: sudo nano /etc/systemd/system/schedule.socket.
# Vai abrir uma tela no Nano e agora vamos copiar o conteúdo do arquivo (guicorn.txt), começando em [Unit] e terminando em [Install] (target).
# /etc/systemd/system/schedule.socket (conteúdo parcial do gunicorn.txt) Depois dê "ctrl+o" e "ctrl + x":
[Unit]
Description=gunicorn schedule socket
[Socket]
ListenStream=/run/schedule.socket
[Install]
WantedBy=sockets.target
# Agora vamos criar o service: sudo nano /etc/systemd/system/schedule.service.
# Dentro do schedule.service, vamos incluir este conteúdo abaixo e somente depois vamos de "ctrl+o" e "ctrl + x"::
[Unit]
Description=Gunicorn daemon (You can change if you want)
Requires=schedule.socket
After=network.target
[Service]
User=gnulinuxdebian
Group=www-data
Restart=on-failure
# EnvironmentFile=/home/gnulinuxdebian/scheduleapp/.env
WorkingDirectory=/home/gnulinuxdebian/scheduleapp
# --error-logfile --enable-stdio-inheritance --log-level and --capture-output
# are all for debugging purposes.
ExecStart=/home/gnulinuxdebian/scheduleapp/venv/bin/gunicorn \
          --error-logfile /home/gnulinuxdebian/scheduleapp/gunicorn-error-log \
          --enable-stdio-inheritance \
          --log-level "debug" \
          --capture-output \
          --access-logfile - \
          --workers 6 \
          --bind unix:/run/schedule.socket \
          schedule.wsgi:application
[Install]
WantedBy=multi-user.target
# sudo systemctl start schedule.socket #1:
# sudo systemctl enable schedule.socket #2:
# sudo systemctl status schedule.socket #3: #  #error #4:
# sudo systemctl status schedule #5:
# sudo systemctl restart schedule.service #6:
# sudo systemctl restart schedule.socket #7:
# sudo systemctl restart schedule #8:
# sudo systemctl daemon-reload #9:
# sudo journalctl -u schedule.service #10:
# sudo journalctl -u schedule.socket #11:
