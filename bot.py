"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/web/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

from webdriver_manager.chrome import ChromeDriverManager

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

class Produto:
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade
        
    def atualizar_preco(self, novo_preco):
        self._preco = novo_preco
        print("Preço atualizado.\n")
        
    def atualizar_quantidade(self, nova_quantidade):
        self._quantidade = nova_quantidade
        print("Quantidade atualizada.")
        
    def mostrar_info(self):
        print(f"Produto: {self._nome}")
        print(f"Preço unitário: {self._preco}")
        print(f"Quantidade em estoque: {self._quantidade}")
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco
    
    @property
    def quantidade(self):
        return self._quantidade
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self._preco = novo_preco
        else:
            print("Preço inválido.")
            
    @quantidade.setter
    def quantidade(self, quantidade):
        if quantidade > 0:
            self._quantidade = quantidade
        else:
            print("Quantidade inválida.")
            
def criar_produto(nome, preco, quantidade):
    produto = Produto(nome, preco, quantidade)
    return produto
    
def cadastrar_produto(bot:WebBot, produto:Produto):
    bot.browse("http://127.0.0.1:5501/bot_produto_POO/templates/index.html")
    bot.maximize_window()
    
    while len(bot.find_elements('//*[@id="productName"]', By.XPATH)) < 1:
        bot.wait(1000)
        print("Carregando...")
    bot.find_element('//*[@id="productName"]', By.XPATH).click()
    bot.kb_type(produto.nome)
    
    while len(bot.find_elements('//*[@id="productPrice"]', By.XPATH)) < 1:
        bot.wait(1000)
        print("Carregandoo...")
    bot.find_element('//*[@id="productPrice"]', By.XPATH).click()
    bot.kb_type(produto.preco)
    
    while len(bot.find_elements('//*[@id="productQuantity"]', By.XPATH)) < 1:
        bot.wait(1000)
        print("Carregando...")
    bot.find_element('//*[@id="productQuantity"]', By.XPATH).click()
    bot.kb_type(produto.quantidade)
    
    while len(bot.find_elements('//*[@id="productForm"]/button', By.XPATH)) < 1:
        bot.wait(1000)
        print("Carregando")
    bot.find_element('//*[@id="productForm"]/button', By.XPATH).click()
    bot.save_screenshot('confirmacao.png')
    


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.CHROME

    # Uncomment to set the WebDriver path
    bot.driver_path = ChromeDriverManager().install()

    # Opens the BotCity website.
   

    # Implement here your logic...
    try:
        produto = criar_produto("batata", "2.50", "100")
        cadastrar_produto(bot, produto)
    except Exception as ex:
        print(f"Erro: {ex}")
        

    # Wait 3 seconds before closing
    bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()





    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
