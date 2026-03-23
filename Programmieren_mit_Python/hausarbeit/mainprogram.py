import classes as c
import placeholders as p

game_objects = []
collision_model = c.CollisionModel(game_objects)

# Instanzierung der Spielobjekte
ship_1234 = c.Ship(
    ID=1234,
    x=100,
    y=15,
    width=15,
    height=30,
    max_health=150,
    cannon_capacity=30,
    collision_model=collision_model,
    game_objects=game_objects,
)
ship_4312 = c.Ship(
    ID=4312,
    x=10,
    y=40,
    width=15,
    height=30,
    max_health=150,
    cannon_capacity=40,
    collision_model=collision_model,
    game_objects=game_objects,
)

rock_6543 = c.Rock(6543, 60, 90, 5, 5)
rock_8756 = c.Rock(8756, 45, 89, 7, 7)

sandbank_5436 = c.SandBank(5436, 70, 140, 30, 10)

fortress_4567 = c.Fortress(
    ID=4567,
    x=200,
    y=200,
    width=20,
    height=20,
    max_health=300,
    collision_model=collision_model,
    game_objects=game_objects
)
fortress_9867 = c.Fortress(
    ID=9867, x=0, y=0, width=20, height=20, max_health=300,
    collision_model=collision_model,
    game_objects=game_objects
)

game_objects = [
    ship_1234,
    ship_4312,
    rock_6543,
    rock_8756,
    sandbank_5436,
    fortress_4567,
    fortress_9867,
]


while True:
    p.get_user_input()
    for objects in game_objects:
        if objects._existing:
            objects.update()
        else:
            game_objects.remove(objects)
            del objects

    collision_model.update()

    print(type(ship_1234))

    break
