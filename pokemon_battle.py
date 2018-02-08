import random
from objects.pokemons import m1
from objects.pokemons import m2
from objects.pokemons import m3


battle_poke = random.randint (1,2)
#  Random Pokemon
if (battle_poke == 1):
    b_poke = m2.name
    print (b_poke)
else:
    b_poke = m3.name
    print(b_poke)

print("A " + b_poke+ " savage has appears, it's time to fight")
#fight
while (m1.hp > 0) and (m2.hp > 0):

    atc_p_1 = random.randint (1,2)
    atc_p_2 = random.randint (1,2)

    #  Random attack
    if (atc_p_1 == 1):
        atc_n_1 = m1.atc_name_1
    else:
        atc_n_1 = m1.atc_name_2

    if (battle_poke == 1):

        if (atc_p_2 == 1):
            atc_n_2 = m2.atc_name_1
        else:
            atc_n_2 = m2.atc_name_2

    else:
        if (atc_p_2 == 1):
            atc_n_2 = m3.atc_name_1
        else:
            atc_n_2 = m3.atc_name_2
    if (m2.hp < 30):
        print(m1.name + " is near to the victory")
    print (b_poke+' attacks  '+m1.name + ' with ' + atc_n_2)
    m1.hp -= m2.atc_1
    print(m1.name+ ' have '+str(m1.hp)+' of HP')
    if (m1.hp > 0):
        m2.hp -= m1.atc_1
        print (m1.name+' attacks  '+b_poke + ' with ' + atc_n_1)
    if (m1.hp <= 0):
        print(str(m1.name)+" dies")
    elif (m2.hp <= 0):
        print(str(b_poke) + " dies")