from JogoDaForca import JogoDeForca
from agente import Agent

jogo = JogoDeForca()
print(jogo.novo_jogo())
print(jogo.palavra)
tam = len(jogo.palavra)
print(tam)
print(jogo.vidas)
agent = Agent([], [], tam)
while jogo.vidas > 0:
    letra = agent.escolher_letra()
    print(f'Agente chutou: {letra}')
    feedback = jogo.tentar_letra(letra)
    print(f'Feedback: {feedback}')
    agent.receber_feedback(letra, feedback)
    print(f'Letras que nao sao parte da resposta: {agent.letras_nao}')
    print(f'Letras que sao parte da resposta: {agent.letras_sim}')
    print(f'Palavra: {agent.palavra}')
    if agent.palavra_completa() == jogo.palavra:
        break
    print(jogo.vidas)
    print()

print(f'Palavra: {agent.palavra}')
print(f'Palavra do jogo: {jogo.palavra}')
print(f'Vidas: {jogo.vidas}')
print(jogo.tentar_palavra(agent.palavra))
