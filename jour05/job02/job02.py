width=int(input("rentrer la largeur du rectangle : "))
height=int(input("rentrer la hauteur du rectangle : "))
for i in range(height):
    if i==0 or i==height-1:
        print('|' + '-' * (width - 2) + '|')
    else:
        print('|' + ' ' * (width - 2) + '|')