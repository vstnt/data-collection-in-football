PREPARAÇÕES
Acompanhando esse video do árabe gente fina https://www.youtube.com/watch?v=neBZ6huolkg e esse do Piotr https://www.youtube.com/watch?v=aBVGKoNZQUw
Os requisitos para rodar o yolo são Python e PyTorch
instalei o python
    não lembro se fiz pelo conda... ou por onde... Na real acho que instalei o python do site deles. Acho que desinstalei o conda.
    O conda é como um conteiner pra usar python. Um sub-ambiente. 
PyTorch
    pip3 install torch==2.3.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
    (a versão mais recente estava com problemas, e nessa versão do torch, a mais nova do cudo (124) não estava disponível)
Instalamos o ulytralytics de onde pegamos o yolo.
    pip install ultralytics
Baixamos um video de teste, da bundesliga, sugerido no video 1.


PRIMEIRO USO
Fizemos o primeiro uso do yolo, em inference_yolo.py, pra detectar usando os videos de teste (pasta input_videos). 
Veja lá as bases do uso do Yolo.
Podemos verificar o modelo base do yolo no github deles: https://github.com/ultralytics/ultralytics. 
    Rodar o código que fizemos já baixa o modelo (arquivo.pt)
Quando baixado o modelo, rodar o código o executa e insere resultados salvos em runs>detect

TREINANDO UM NOVO MODELO
Então seguimos para treinar o modelo com um dataset de futebol
Criamos um arquivo notebook, em training>training_yolo_v8.ipynb. Lá está todo o processo de treino.

TRANSFORMAÇÕES NOS VIDEOS.
Agora que temos modelos treinados, vamos começar a aplicar alterações nos videos.
Veja o novo notebook: usando_yolo.ipynb

Durante o seguimento do tutorial do Piotr, em usando_yolo.ipynb, descobri que, pelo jeito, o uso das ferramentas do Supervision e Inference,
que são base pra as transformações realizadas no tutorial, envolvem todas o deploy de nosso modelo na database Roboflow, e com isso a cobrança
por usos mais elevados. Procurei um bom tanto sobre como escapar disso e poder usar as ferramentas livremente, mas não parece ser possível.
Assim, vou seguir com o outro tutorial, do árabe, e depois volto ao do Piotr pra ver se há algo a se coletar ali. 

Seguindo pelo Árabe. Bom, sabendo treinar o modelo e como ele funciona, o próximo passo é criar um sistema de salvamento dos videos após as
transformações da predição crua.

pip install opencv-python (ja tava instalado aqui não sei pq)

Criamos um main.py e um utils>video_utils.py. Neste, teremos a lógica para ler e salvar o video. Criamos tbm, um init.py para expor
as funções de dentro do utils para fora dele. Basicamente pra poder importar, creio.

Tracking: reconhecer (sustentando uma id) uma entidade ao longo dos frames, ao longo das bounding boxes encontradas. 
Isso pode se dar pela direção do movimento, ou pela cor. Usaremos o tracker chamado ByteTracker, do Supervision
Criamos a pasta trackers, com init.py e tracker.py

  
Piotr safado! O método .infer não existe por padrão nos modelos do yolov8. Esse método é adicionado apenas quando fazemos o deploy do
modelo na roboflow e o recuperamos via get_model(). Com isso eles podem controlar o uso que fazemos de um modelo e, principalmente, o
uso que fazemos do método de inferencia, e cobrar por isso. Absurdo... Bem que ele fala que no mundo SÓ O TUTORIAL dele é gratuito.
Creio que o uso do supervision em si não cai nessa necessidade da API deles, mas os objetos e métodos que ela aceita sim! Por exemplo,
o detections = sv.Detections.from_inference(result) no código acima, não aceita o retorno padrão do modelo.predict(). Tem que ser o retorno
do  método .infer(), que por sua vez não existe como método do modelo puro, e sim somente doo modelo retornado pelo get_model, via a API. Pilantras!
Vou largar o tutorial dele e seguir pelo do árabe, e talvez volte no dele pra ver se há algo a ser aprendido depois.
Mentira!!!!!! Consegui resolver usando o .predict e ao invés do .from_inference, usando o .from_ultralytics

