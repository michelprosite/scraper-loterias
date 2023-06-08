# Prajeo Scraper Loterias

Este projeto, chamado "Prajeo Scraper Loterias", foi desenvolvido com o objetivo de facilitar a seleção de números para apostas na Mega Sena, com base em dados de sorteios anteriores.

## Autor
Michel Souza Santana

## Data
08/06/2023

## Descrição
O "Prajeo Scraper Loterias" utiliza técnicas de web scraping para coletar informações sobre os resultados dos sorteios da Mega Sena a partir do site "asloterias.com.br". Com a biblioteca BeautifulSoup em Python, são extraídos os números sorteados em diferentes anos.

Após a coleta dos dados, o projeto oferece duas opções para a seleção dos números da aposta:

1. Composição aleatória com todos os números mais sorteados:
   Nessa opção, o usuário define a quantidade total de números que deseja apostar, utilizando a variável "total_numeros". O projeto seleciona aleatoriamente os números da lista de todos os números mais sorteados, garantindo que não haja repetições.

2. Limitação do total de números mais sorteados:
   Nessa opção, o usuário define a quantidade total de números desejada e o número de números mais sorteados que deseja levar em consideração. O projeto limita a seleção aos números mais sorteados, aumentando a probabilidade de acerto.

Após a seleção dos números, o projeto exibe a lista final para o usuário.

## Como usar
1. Certifique-se de ter as seguintes bibliotecas instaladas:
   - pandas
   - bs4
   - urllib

2. Clone este repositório:
git clone https://github.com/seu-usuario/prajeo-scraper-loterias.git

3. Execute o script Python `prajeo_scraper_loterias.py` em um ambiente Python:
python prajeo_scraper_loterias.py

4. Siga as instruções fornecidas no programa para selecionar os números da aposta.

## Contribuição
Contribuições são bem-vindas! Se você quiser melhorar este projeto, fique à vontade para abrir um pull request.

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.

Lembre-se de adaptar as seções de acordo com suas necessidades e especificações do projeto. Certifique-se também de fornecer informações relevantes sobre a instalação e uso do projeto.
