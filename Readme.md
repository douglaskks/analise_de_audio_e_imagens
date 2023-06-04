# Análise de Áudio e imagens utilizando o Librosa

### Resultado do áudio
---


![Imagem com informações visuais de um audio](/images/Resultado%20do%20audio.png)

---


#### Este repositório tem como objetivo ser uma atividade para a disciplina de Projeto e Execução de Software do curso de bacharelado em Ciência da Computação, onde o software tem como obejtivo Fazer análise de áudio e imagens onde eu escolhi a Librosa como ferramenta através da linguagem de programação Python, mostrando assim parâmetros como Spectograma, Cores, Gráficos e demais características do audio selecionado.

<br>
<br>

# Descrição do código
<br>

### Abaixo temos a importação das bibliotecas utilizadas para fazer a análise do áudio e da imagem, assim podemos fazer o uso livre das ferramentas, lembrando que algumas linhas não são necessárias como o <italic>IPython.display</italic> que permite exibir áudio diretamente no Jupyter Notebook ou em outros ambientes interativos compatíveis.

    from numpy import ndarray
    import numpy as np
    import matplotlib.pyplot as plt
    from IPython.display import Audio
    import librosa
    import librosa.display

### O próximo código define a variável data e fs. data será usado para armazenar os dados do áudio e fs será usado para armazenar a taxa de amostragem, carrega o arquivo de áudio 'teste.mp3' usando a função librosa.load. O parâmetro sr=44100 especifica que a taxa de amostragem desejada é 44100 Hz. A função librosa.load retorna os dados do áudio e a taxa de amostragem e cria um objeto Audio com os dados do áudio e a taxa de amostragem. Isso permite reproduzir o áudio diretamente no ambiente interativo, como um Jupyter Notebook.

    data: ndarray
    data, fs = librosa.load('teste.mp3', sr=44100)
    Audio(data=data, rate=fs)

### O próximo código calcula o espectrograma do áudio utilizando a função librosa.stft, que realiza uma transformada de Fourier de curto tempo (STFT) nos dados do áudio. Em seguida, a função np.abs é aplicada para calcular o valor absoluto dos coeficientes da STFT. Por fim, a função librosa.amplitude_to_db é usada para converter a escala do espectrograma em decibéis, exibe o espectrograma usando a função librosa.display.specshow. Os parâmetros x_axis='time' e y_axis='linear' especificam que o eixo x representa o tempo e o eixo y representa a frequência, respectivamente. O parâmetro sr=fs define a taxa de amostragem para a exibição correta do espectrograma. O parâmetro cmap='jet' define o mapa de cores a ser usado para a representação visual.

    D = librosa.amplitude_to_db(np.abs(librosa.stft(data)))
    librosa.display.specshow(D, x_axis='time', y_axis='linear', sr=fs, cmap='jet')
    plt.xlabel('Time [s]')
    plt.ylabel('Frequency [Hz]')
    plt.colorbar(format='%+2.0f dB')

### A linha que contém <italic>plt.interactive(False)</italic> desativa o modo interativo do matplotlib, o que pode ajudar a garantir que a janela de plotagem seja exibida corretamente dentro do ambiente do PyCharm.

<br>
<br>

### A linha que contém <italic>plt.show()</italic> força a exibição da janela de plotagem e aguarda até que você a feche manualmente.