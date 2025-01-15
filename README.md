# 
 
<h1 align="center">LinkedinAutoBot 🤖</h1>

<div align="center">
  <img src="https://github.com/SidneyTeodoroJr/LinkedinAutoBot/blob/main/bot_designer/LinkedIn-Auto%20Bot-%20home%20-light.png" alt="Banner LinkedinAutoBot">
</div>
</br>
</br>

<h2 align="center">Overview</h2>
<p>
 O LinkedIn Auto Bot é uma aplicação que automatiza interações no LinkedIn, facilitando o gerenciamento de conexões e interações na plataforma. A aplicação possui uma interface gráfica intuitiva e permite a personalização de várias configurações.
</p>

<h2>Download the Application</h2>

<a href="https://raw.githubusercontent.com/SidneyTeodoroJr/MoviePY/main/build_platforms/MoviePY.apk" download>Windows</a></br>

<h2>Tecnologias Utilizadas</h2>

- [Python](https://docs.python.org/3/)
- [Flet](https://flet.dev/docs/) (para construção da interface gráfica)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) (para automação de interações)
- [OpenCV](https://docs.opencv.org/4.x/index.html) (para processamento de imagens)

<div align="center">
  <img height=200 width=300 src="https://logosmarcas.net/wp-content/uploads/2021/10/Python-Logo.png" alt="Python"/>
  <img height=200 width=300 src="https://raw.githubusercontent.com/flet-dev/flet/main/media/logo/flet-logo.svg" alt="Flet"/>
</div>

<h2>Instalação</h2>

<p>Para executar o projeto, você precisará ter o Python instalado em sua máquina. Siga os passos abaixo:</p>

1. Clone este repositório:
   ```
   git clone https://github.com/SidneyTeodoroJr/LinkedinAutoBot.git
2. Navegue até o diretório do projeto:
   ```
   cd LinkedinAutoBot
4. Navegue até 'SRC'
   ```
   cd scrc
5. Instale as dependências necessárias:
   ```
   pip install -r requirements.txt
5. Para iniciar a aplicação, execute o seguinte comando:
    ``` 
    flet -r main.py
    
 <h2>Estrutura do Código</h2>
 
<p>O projeto é organizado da seguinte forma:</p>

- [main.py](https://github.com/SidneyTeodoroJr/LinkedinAutoBot/blob/main/LinkedInAutoBot/src/main.py): Ponto de entrada da aplicação, onde a interface é configurada.
  
- [modules/GUI_elements.py](https://github.com/SidneyTeodoroJr/LinkedinAutoBot/blob/main/LinkedInAutoBot/src/modules/GUI_elements.py): Define elementos gráficos personalizados, como textos, botões e sliders.
  
- [pages/](https://github.com/SidneyTeodoroJr/LinkedinAutoBot/tree/main/LinkedInAutoBot/src/pages): Contém as páginas da aplicação, como a página inicial e a página de configuração.
  
- [modules/image_search.py](https://github.com/SidneyTeodoroJr/LinkedinAutoBot/blob/main/LinkedInAutoBot/src/modules/image_search.py): Contém a lógica para localizar elementos na tela através da classe ImageLocator.

<div align="center">
  <img src="https://github.com/SidneyTeodoroJr/LinkedinAutoBot/blob/main/bot_designer/LinkedIn-Auto-Bot%20-setup-light.png" alt="Print LinkedinAutoBot light">
</div>

<h2>Classe ImageLocator</h2>

<p>A classe ImageLocator é responsável por localizar elementos de imagem na tela e interagir com eles. Os principais parâmetros e métodos incluem:</p>

- <h3>Parâmetros:</h3>

1. `img_path:` Caminho da imagem a ser localizada.
2. `max_attempts:` Número máximo de tentativas para localizar a imagem.
3. `search_interval:` Intervalo de tempo entre tentativas de busca.
4. `duration:` Duração do movimento do mouse até a posição localizada.
5. `confidence:` Nível de confiança ao localizar a imagem (de 0 a 1).

- <h3>Método start_search:</h3>

1. Localiza a imagem na tela e executa um clique se encontrada.
2. Se a imagem não for encontrada após o número máximo de tentativas, imprime uma mensagem de erro.

<h2>Componentes Personalizados</h2>

<p>Abaixo estão os principais componentes personalizados utilizados na aplicação:</p>

1. `CustonAppBar:` Uma barra de aplicativo que inclui ícones para informações e alternância entre temas.
2. `CustonCard:` Um cartão que pode conter informações e é estilizado com uma cor de fundo personalizada.
3. `CustonSwitch:` Um switch que pode ser utilizado para alternar configurações, com cor ativa e tooltip personalizáveis.
4. `CustonText:` Um componente de texto que permite personalizar cor, peso, alinhamento e tamanho.
5. `bot_name:` Um campo de entrada para o nome do bot, com ícone de raio.
6. `InputSearch:` Um campo de entrada para pesquisar termos, com ícone de lupa.
7. `time_slider:` Um slider para ajustar o tempo entre cliques, com intervalo de 3 a 10 segundos.
8. `connects_slider:` Um slider para definir o número de conexões por página, com intervalo de 1 a 7.
9. `pages_slider:` Um slider para definir o número de páginas que o bot irá percorrer, com intervalo de 1 a 10.

<h2>Página Inicial</h2>

<p>A página inicial (home_page) é composta pelos seguintes elementos:</p>

1. `CustonAppBar:` Uma barra de aplicativo que inclui opções para abrir o repositório do GitHub e alternar entre temas.
2. `Texto de Boas-vindas:` Uma mensagem central que diz "Best engagement bot for LinkedIn".
3. `Imagem:` Um ícone representativo da aplicação, exibido em tamanho 350x350.
4. `Instruções:` Mensagens que incentivam o usuário a fazer login no LinkedIn antes de prosseguir.
5. `Botão "Start Setup":` Um botão destacado que inicia o processo de configuração, com um estilo personalizado.
   
<h2>Página de Configuração</h2>

<p>A página de configuração (setup_page) permite que os usuários personalizem as configurações do bot. Os principais componentes incluem:</p>

1. `Banner:` Uma imagem de capa com uma descrição da funcionalidade do bot.
2. `Cartões de Informação:` Exibem informações sobre a quantidade de conexões, páginas e tempo configurado pelo usuário, utilizando sliders.
3. `Configuração de Automação:` Inclui campos de entrada para nome do bot e pesquisa, além de sliders para configurar o número de conexões, páginas e tempo.
4. `Botão "GO":` Um botão que inicia a automação, ao clicar, aciona a função AutoBot.

<h2>Função AutoBot</h2>

<p>A função AutoBot é responsável por executar o processo de automação no LinkedIn. Os principais passos incluem:</p>

1. Minimizar todas as janelas e abrir o LinkedIn.
2. Localizar e interagir com o campo de busca.
3. Navegar pelas páginas de resultados e enviar solicitações de conexão com base nas configurações do usuário.
4. Gerenciar a navegação entre páginas e a quantidade de conexões.
5. Finalizar a sessão do bot e fechar o navegador.
   
<h2>Principais Funções</h2>

1. `open_website:` Abre a URL do repositório do GitHub.
2. `toggle_theme:` Alterna entre os temas claro e escuro.
3. `start_setup:` Navega para a página de configuração.
4. `start_home:` Retorna para a página inicial.
5. `route_change:` Gerencia a mudança de rotas na aplicação.
6. `AutoBot:` Função que inicia a automação com as configurações definidas pelo usuário.

<h2>Licença</h2>

<p>Este projeto está licenciado sob a MIT License. Clique no link a baixo para mais detalhes.</p>

[LICENSE](https://opensource.org/license/mit)

## Contributions
</br>

<p>
  Contributions are welcome! If you want to improve the project, add new features or fix bugs, feel free to do so.
</p>
<hr>
</br>

<div align="center">
<a href="https://sidney-personal-portifolio.netlify.app/"><img src="https://img.shields.io/badge/-Portifolio-%230077B5?style=for-the-badge&logo=portifolio&logoColor=white" style="border-radius: 30px" target="_blank" /></a>
<a href="https://www.instagram.com/sidneyteodoroaraujo" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" /></a>
<a href="https://www.linkedin.com/in/sidey-teodoro-a-jr/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" style="border-radius: 30px" target="_blank" /></a>
</div>
