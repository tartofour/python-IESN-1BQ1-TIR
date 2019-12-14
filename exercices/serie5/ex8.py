#!/usr/bin/python

#################################
########### FONCTIONS ###########
#################################

def modify_production(tile: dict, resource: str, amount: int) -> None:
        if tile[resource] + amount > 0:
            tile[resource] += amount
            print(tile)
        else:
            print("Erreur !")

def new_tile(terrain: str) -> dict:
    if terrain == "water":
        tile = {"terrain" : "water", "production" : {"food" : 1}}    
    elif terrain == "plain":
        tile = {"terrain" : "plain", "production" : {"food" : 2}}    
    elif terrain == "forest":
        tile = {"terrain" : "forest", "production" : {"food" : 1, "materials" : 1}}    
    elif terrain == "mountain":
        tile = {"terrain" : "mountain", "production" : {"materials" : 2}}    
    return tile

#def has_owner(tile: dict, name: str = None) -> bool:
#    return tile["owner"] == name or "owner" in tile

def has_city(tile: dict) -> bool:
    return "city" in tile

def has_tradepost(tile: dict) -> bool:
    return "tradepost" in tile

def can_build_city(tile: dict) -> bool:
    return tile["terrain"] == "plain"\
            and "owner" in tile\
            and tile["owner"] != None\
            and "city" not in tile\

def can_build_tradepost(tile: dict) -> bool:
    return tile["terrain"] != "water"\
            and "owner" in tile\
            and tile["owner"] != None\
            and "tradepost" not in tile

def build_tradepost(tile: dict) -> None:
    if can_build_tradepost(tile):
        tile["tradepost"] = True

def build_city(tile: dict, name: str) -> None:
    if can_build_city(tile):
        tile["city"] = name
        if "tradepost" in tile:
            del tile["tradepost"]

def cut_forest(tile: dict) -> None:
    if tile["terrain"] == "forest":
        tile["terrain"] = "plain"

def changer_owner(tile: dict, name: str = None) -> str:
    if not name and tile["owner"]:
        del tile["owner"]
    else: 
        old_name = tile["owner"]
        tile["owner"] = name
        return old_name

#def raze_building(tile: dict) -> bool:
#   débalage ?
#   buildings = ("city", "tradepost")
#    razed_buildings = 0
#    for building in buildings:
#        if tile[building]:
#            del tile[build]
#            razed_buildings += 1


def count_cities(tiles: list, name: str) -> int:
    owned_cities = 0
    for tile in tiles:
        if tile["owner"] == name and "city" in tile:
            owned_cities += 1
    return owned_cities

def count_total_production(tiles: list, name: str) -> dict:
    # DEGUEU
    total_food = 0
    total_materials = 0
    total_gold = 0
    for tile in tiles:
        if tile["owner"] == name:
            food = tile["production"]["food"]
            materials = tile["production"]["materials"]
            gold = tile["production"]["gold"]
            total_food += food
            total_materials += materials
            total_gold += gold
    return {"food" : total_food, "materials" : total_materials, "gold" : total_gold}


#################################
############## MAIN #############
#################################

#tile1 = {"terrain" : "forest", "production" : {"food" : 1, "materials" : 1, "gold" : 1}, "city" : "Ma ville", "owner" : "moi",}
#tile2 = {"terrain" : "forest", "production" : {"food" : 1, "materials" : 1, "gold" : 1},  "city" : "Ma ville","owner" : "moi"}
#tile3 = {"terrain" : "forest", "production" : {"food" : 1, "materials" : 1, "gold" : 1}, "owner" : "moi"}
#tiles = [tile1, tile2, tile3]
#print(tile1)
#print(count_total_production(tiles, "moi"))


