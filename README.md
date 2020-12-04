# Helmet Detector
Atividade avaliativa final da disciplina de Computação Gráfica - Ciência da Computação IMED

Desenvolvido por Alysson Drews e Frederico Detofano

### Objetivo

O principal objetivo da aplicação, é que seja usada em cameras de segurança para a detecção do uso de capacete, seja na estrada, ou para segurança caso haja uma tentativa de roubo em lojas.

### Funcionamento

O código, escrito em *Python*, utiliza como sua principal biblioteca o *OpenCV* para o reconhecimento e treinamento de imagens ou videos, fazendo o uso de Haar Cascade para o treino.

É esperado um vídeo como input para que a aplicação funcione, esse, pode ser uma camera ou um arquivo. Após definir a fonte que sera usada, o código começa a capturar os frames e analisar se existe algo relacionado ao seu treinamento feito anteriormente, nesse caso, uma pessoa usando ou carregando um capacete de moto. Caso o objeto seja detectado, o código começa a lançar *logs* e tirar fotos do vídeo. O possível suspeito sera marcado com um retangulo, mostrando o objeto em destaque.

