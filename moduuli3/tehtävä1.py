""""""

kuha = int(input('kuinka senttimetri on kuha? '))
if kuha < 37:
    print('laskea kuhan takaisin järveen!')
    print(f'{37-kuha} senttiä alimmasta sallitusta pyyntimitasta puuttuu.Kuha on alamittainen, jos sen pituus on alle 37 cm.')
