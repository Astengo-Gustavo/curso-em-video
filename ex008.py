'''
escreva um programa que leia um valor em metros e o
exiba convertido em centimetros e milimetros
'''

medida = float(input('digite uma distancia em metros: '))
km = medida / 1000
hm = medida / 100
dm = medida / 10
dc = medida * 10
cm = medida * 100
mm = medida * 1000

print('a medida de {} m corresponde a: \n{} km \n{} hm \n{} dm \n{} dc \n{} cm \n{} mm'.format(medida,km,hm,dm,dc,cm,mm))