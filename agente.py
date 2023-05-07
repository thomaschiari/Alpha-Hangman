class Agent:

    def __init__(self, letras_nao, letras_sim, tamanho_palavra):
        self.letras_nao = letras_nao # letras q nao sao parte da resposta do hangman
        self.letras_sim = letras_sim # letras q sao parte da resposta do hangman
        self.tamanho_palavra = tamanho_palavra # tamanho da palavra a ser adivinhada
        self.palavra = ['_' for i in range(tamanho_palavra)]




    def escolher_letra(self):
        with open('wordlist.txt', 'r') as f:
            wordlist = f.read().splitlines()
        wordlist = [word for word in wordlist if len(word) == self.tamanho_palavra]
        # precisamos descartar as palavras que contem as letras que ja sabemos q nao sao parte da resposta
        for letter in self.letras_nao:
            wordlist = [word for word in wordlist if letter not in word]
        # precisamos descartar as palavras que nao contem as letras que ja sabemos q sao parte da resposta no lugar certo
        for idx in range(self.tamanho_palavra):
            if self.palavra[idx] != '_':
                wordlist = [word for word in wordlist if word[idx] == self.palavra[idx]]



        # faremos uma decisao de qual letra escolher baseado na frequencia de cada letra
        # na wordlist
        # para isso, criaremos um dicionario com a frequencia de cada letra
        frequencia_letras = {}
        for word in wordlist:
            for letter in word:
                if letter in frequencia_letras:
                    frequencia_letras[letter] += 1
                else:
                    frequencia_letras[letter] = 1
        # agora, vamos ordenar as letras por frequencia
        frequencia_letras = sorted(frequencia_letras.items(), key=lambda x: x[1], reverse=True)
        # e retornar a letra mais frequente que nao esteja na lista de letras que ja sabemos
        for letter in frequencia_letras:
            if letter[0] not in self.letras_sim and letter[0] not in self.letras_nao:
                return letter[0]
        # se nao houver nenhuma letra que nao sabemos, retornamos a letra mais frequente
        return frequencia_letras[0][0]
    
    def receber_feedback(self, letra, feedback):
        try:
            if feedback != []:
                self.letras_sim.append(letra)
                for idx in feedback:
                    self.palavra[idx] = letra
            else:
                self.letras_nao.append(letra)
        except:
            # jogo acabou
            pass


    def palavra_completa(self):
        if '_' not in self.palavra:
            # list to string
            return ''.join(self.palavra)
        else:
            return False

