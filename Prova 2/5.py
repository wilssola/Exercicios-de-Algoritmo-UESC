def aceleracao(v_inicial, v_final, tempo):
    v_inicial /= 3.6
    v_final /= 3.6
    
    aceleracao = (v_final - v_inicial) / tempo

    return round(aceleracao, 2)

def main():
    v_inicial = 30
    v_final = 60
    tempo = 2
    
    print('Velocidade Inicial:', v_inicial, 'km/h')
    print('Velocidade Final:', v_final, 'km/h')
    print('Tempo:', tempo, 's')
    print('Aceleração:', aceleracao(v_inicial, v_final, tempo), 'm/s')
    
main()
