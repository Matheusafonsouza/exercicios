### Q1
Foi utilizada a regra (\d{2})/(\d{2})/(\d{4}) para fazer a captura das datas no formado americano e utilizada e a regra $2/$1/$3 para convertê-las para o formato brasileiro.

### Q2
Utilizando o módudo "re", foram criadas 3 variáveis:

* uma com o texto gerado a partir do arquivo
* uma com a regex que seria executada
* uma com as respostas

A regex utilizada foi a <img src=\"(/\w+)+.gif\"> para capturar todos os arquivos do formato ".gif", logo em seguida foi igualada a variável das respostas com re.findall(r"<img src=\"(/\w+)+.gif\">", <variável do texto>) para assim, encontrar todos os arquivos ".gif". A resposta foi calculada utilizando a função len() do python, assim, recuperando o tamanho da variável.