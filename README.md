HISTÓRICO DESSE PROJETO:


PREPARAÇÕES
Acompanhando esse video do árabe gente fina https://www.youtube.com/watch?v=neBZ6huolkg e esse do Piotr https://www.youtube.com/watch?v=aBVGKoNZQUw. 
Os requisitos para rodar o yolo são Python e PyTorch
Instalei o python: Não lembro se fiz pelo conda... ou por onde... Na real acho que instalei o python do site deles. Acho que desinstalei o conda. O conda é como um conteiner pra usar python. Um sub-ambiente. 
PyTorch: pip3 install torch==2.3.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 (a versão mais recente estava com problemas, e nessa versão do torch, a mais nova do cudo (124) não estava disponível)
Instalamos o ulytralytics de onde pegamos o yolo: pip install ultralytics
Baixamos um video de teste, da bundesliga, sugerido no video 1.


PRIMEIRO USO
Fizemos o primeiro uso do yolo, em inference_yolo.py, pra detectar usando os videos de teste (pasta input_videos).  Veja lá as bases do uso do Yolo. Podemos verificar o modelo base do yolo no github deles: https://github.com/ultralytics/ultralytics. Rodar o código que fizemos já baixa o modelo (arquivo.pt). Quando baixado o modelo, rodar o código o executa e insere resultados salvos em runs>detect


TREINANDO UM NOVO MODELO
Então seguimos para treinar o modelo com um dataset de futebol. Criamos um arquivo notebook, em training>training_yolo_v8.ipynb. Lá está todo o processo de treino.


TRANSFORMAÇÕES NOS VIDEOS.
Agora que temos modelos treinados, vamos começar a aplicar alterações nos videos. Veja o novo notebook: usando_yolo.ipynb
    Seguindo pelo Árabe: Bom, sabendo treinar o modelo e como ele funciona, o próximo passo é criar um sistema de salvamento dos videos após as transformações da predição crua.
    pip install opencv-python (ja tava instalado aqui não sei pq)
    Criamos um main.py e um utils>video_utils.py. Neste, teremos a lógica para ler e salvar o video. Criamos tbm, um init.py para expor as funções de dentro do utils para fora dele. Basicamente pra poder importar, creio.
    Tracking: reconhecer (sustentando uma id) uma entidade ao longo dos frames, ao longo das bounding boxes encontradas. 
    Isso pode se dar pela direção do movimento, ou pela cor. Usaremos o tracker chamado ByteTracker, do Supervision
    Criamos a pasta trackers, com init.py e tracker.py
Consegui lidar com as dificuldades no tutorial do Piotr, então voltamos a utilizá-lo. O do árabe ica de lado por enquanto
Conseguimos realizar o tracking e dividir os times. A seguir, vamos para a detecção de pontos chave no campo, 
com isso, poderemos criar a visão homográfica do jogo, e seremos capazes de coletar informações de movimentação dos jogadores, como velocidade e distância percorrida.


TREINO DO PITCH KEY POINT DETECTOR
veja training_pitch_keypoint_detector.ipynb

