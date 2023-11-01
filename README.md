# 11. Tipos de Apreendizagem de Máquina

## Apredizagem supervisionada

Tem como caracteristica o supervisionamento e classificação por grupos(Classes:A,B ...) pelo usuario.
### Fase 1

- Extração de caracteristicas
- Algoritimo de aprendizagem
- Modelo aprendido

### Fase 2

-Extracao de caracteristicas
- Modelo aprendido
- reconhecimento

## Apredizagem não- supervisionada

-Analiza automaticamente os dados (associação e agrupamento)
-Necessita analise para detrminar o significado dos padrões encontrado

## Apredizagem por reforço

- Apreende com as interações com o ambiente (causa e efeito);
- Apreende com sua propria esperiência;
- Ex.: Robô coletando lixo apreendendo a andar em um ambiente;
- Ex. 2: Controle automatizado de elevadores

## 12. Ajuste de pesos 1
- Usa o operador E
- x1,x2,... são atributos previsores e classe são atributos meta pois queremos fazer a previsão
- Algoritimo mais simples
- Formula do Erro:
    - Erro= Resposta Correta - Resposta Errada
- Formula para atualiza peso:
    - Os pesos são atualizados até os erros serem pequenos
        - peso(n-1)= peso(n) + (taxaAprendizagem * Entrada * erro)
            - Observação a taxa de aprendizagem pe um valor fixo informado pelo supevisor
            - Ex.da formula: P(n+1)=0+(0.1 * 1 * 1 )= 0.1
# 13. Ajuste de pesos 2

O algoritmo vai processando tentando acertar e vai ajustando os pesos ate chegar em pesos que ele consiga classificar obtendo uma porcentagem de acerto de 100% ou o mais proximo possivel. 


