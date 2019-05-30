# Trabalho 3 - Injeção de código

## Introdução
Um ataque de injeção de código é uma ameaça de segurança que se aproveita de falhas em sistemas através de comandos de linguagens de programação, onde o atacante consegue inserir uma instrução personalizada e indevida dentro de uma das entradas de dados de uma aplicação, como formulários ou URL.

Através de um ataque desse, o atacante pode conseguir muitas coisas, dentre elas acesso a áreas não permitidas, execução de atividades ilícitas e às vezes até o acesso completo à maquina que hospeda a aplicação.

Nesse trabalho será demonstrado um simples servidor *web* com uma brecha de segurança extremamente preocupante. O passo-a-passo de como colocar o servidor funcionando e replicar os resultados obtidos nesse relatórios estão na seção [Funcionamento](#Funcionamento)

## O servidor *web*
Nesse trabalho, foi construído um servidor *web* simples através do *framework* [Flask](http://flask.pocoo.org/) cuja única funcionalidade é o *echo* através da URL.

Esse exemplo foi escolhido para demonstrar duas coisas, principalmente:
* O risco que se corre ao utilizar a biblioteca *"os"* do *Python*;
* A facilidade com que ocorre a injeção de código por URL num método *GET* não tratado.

### Explicando o *source code*
```
import os
from flask import Flask, request, render_template_string
```
Primeiramente, de modo a demonstrar o risco de uso da *"os"*, é feito o *import* dela e dos módulos do Flask:
```
app = Flask(__name__)
app.jinja_env.globals['os'] = os
```
Essas duas linhas se referem à instanciação do *Flask* para o objeto *app* e a inclusão da *"os"* no ambiente do *jinja*, para uso em código embutido nos templates.
```
@app.route('/')
@app.route('/echo')
def  index():
	echo_input = {'echo':"Please make a GET request with '?echo=your_input'"}
	if request.args.get('echo'):
		echo_input['echo'] = request.args.get('echo')
	template =  '''<h3>Echo: %s</h3>'''  % echo_input['echo']
	return render_template_string(template, echo_input=echo_input)
```
A seguir, é feito o uso de decoradores para incluir a rota dos diretórios raiz e */echo* para o mesmo método que, quando não há o argumento *"echo"* na URL, demonstra *"Please make a GET request with '?echo=your_input'"* e, caso contrário, demonstra o próprio argumento.

## A injeção de código

Primeiramente, testa-se o funcionamento comum da aplicação, conforme os *screenshots* a seguir:
![empty_args](screenshots/empty_args.png)
![echoTeste](screenshots/echoTeste.png)

Após, verifica-se a possibilidade de injeção de código realizando a chamada de um *alert()*:
![alertTest](screenshots/alertTest.png)

Em seguida, testa-se a oportunidade de uso da biblioteca *"os"*:
![osNameTest](screenshots/osNameTest.png)

Uma vez que essa biblioteca está disponível para uso num ataque de injeção de código, é possível obter com facilidade uma *shell* completa do servidor, da seguinte maneira:
```
os.popen("<comando>").read()
```
Com essa simples linha de comando, é possível executar qualquer instrução diretamente na *shell* do servidor e receber o *output* dela!

Sabendo disso, foi elaborado um *script Python* simples que funciona como a própria *shell* do servidor, uma vez que, quando é dada uma instrução, ela é passada por XSS para o servidor, executada e a resposta é *parseada* para demonstrar estritamente o necessário.

Fazendo uso desse *script*:
![xssShell](screenshots/xssShell.png)

## Conclusão
A partir desse trabalho, foi possível concluir que todos os *inputs* dos servidores devem ser devidamente tratados, de modo a evitar qualquer invasão. Também foi possível notar a responsabilidade de usar a biblioteca *"os"* do *Python*, uma vez que essa possui grandes privilégios na máquina, portanto, pode se tornar uma brecha de segurança extremamente séria.

## Funcionamento
Primeiramente, clone esse repositório
```
git clone https://github.com/gabriel-milan/SecurityClass.git
```
Acesse a pasta referente a esse trabalhor
```
cd SecurityClass/Trabalho\ 3\ -\ Injeção\ de\ código/
```
Instale as dependências
```
pip3 install -r requirements.txt
```
Defina o *app* que deve rodar
```
export FLASK_APP=server.py
```
Coloque o servidor rodar
```
python3 -m flask run
```
Pronto! Após isso, só seguir os passos conforme o [vídeo](https://youtu.be/cwMauENMH40) de demonstração.