# Criação de GIF a partir de Imagens PNG

Este projeto permite a criação de arquivos GIF animados a partir de múltiplas imagens PNG.

## Requisitos

- Python 3.x
- Biblioteca `imageio` 

## Instalação

Instale a biblioteca necessária usando pip:

```bash
pip install imageio
```

## Como Usar

### Passo 1: Prepare suas imagens

Coloque todas as imagens PNG que você deseja incluir no GIF na mesma pasta do script. Certifique-se de que estão nomeadas adequadamente.

### Passo 2: Ajuste o código

Modifique a lista `filenames` com os nomes dos seus arquivos:

```python
import imageio.v3 as iio

# Lista com os nomes dos arquivos das imagens
filenames = ['fh540-1620x1620-1.png', 'fh540-1620x1620-2.png', 'fh540-1620x1620-3.png']
images = [ ]

# Carrega cada imagem
for filename in filenames:
  images.append(iio.imread(filename))

# Cria o GIF
# duration: tempo em milissegundos que cada frame aparece
# loop: 0 significa que o GIF repetirá infinitamente
iio.imwrite('fh540.gif', images, duration=500, loop=0)
```

### Passo 3: Execute o script

```bash
python nome_do_script.py
```

### Passo 4: Verifique o resultado

Após a execução bem-sucedida, um arquivo chamado `fh540.gif` será criado na mesma pasta. Você pode renomear este arquivo no código alterando o primeiro parâmetro da função `iio.imwrite()`.

## Personalizações

- **Duração dos frames**: Altere o valor do parâmetro `duration` (em milissegundos) para controlar a velocidade da animação.
- **Repetição**: O parâmetro `loop=0` faz o GIF repetir infinitamente. Para limitar o número de repetições, defina um valor numérico (exemplo: `loop=3`).
- **Nome do arquivo de saída**: Modifique o primeiro parâmetro de `iio.imwrite()` para alterar o nome do GIF gerado.

## Exemplo

Para criar um GIF mais lento com 5 imagens:

```python
filenames = ['imagem1.png', 'imagem2.png', 'imagem3.png', 'imagem4.png', 'imagem5.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('animacao_lenta.gif', images, duration=1000, loop=0)
```

Este exemplo criará um GIF onde cada imagem é exibida por 1 segundo (1000ms).