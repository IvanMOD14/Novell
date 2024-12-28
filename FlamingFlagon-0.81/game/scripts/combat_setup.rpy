init python:

    class Fighter:
        def __init__(self, name, con, str, int, dex, cha, resistances, status_resistances, skills, frame_background):
            self.name = name
            self.max_hp = con * 10  # Example calculation, adjust as needed
            self.hp = self.max_hp
            self.max_ep = int  # Starting EP, adjust as needed
            self.ep = self.max_ep
            self.str = str
            self.int = int
            self.dex = dex
            self.cha = cha
            self.resistances = resistances  # Dictionary of damage type to resistance percentage
            self.status_resistances = status_resistances  # Dictionary of status effect to resistance percentage
            self.skills = skills  # List of Skill objects
            self.status_effects = []  # List of active status effects
            self.frame_background = frame_background  # unique UI frame

    class Enemy(Fighter):
        def __init__(self, name, con, str, int, dex, cha, resistances, status_resistances, skills, action_probabilities, frame_background, picture):
            super(Enemy, self).__init__(name, con, str, int, dex, cha, resistances, status_resistances, skills, frame_background)
            self.action_probabilities = action_probabilities
            self.picture = picture  # Path to the enemy's picture

        @property
        def is_alive(self):
            return self.hp > 0

    class Skill:
        def __init__(self, name, cost, damage, damage_type, targets_all=False):
            self.name = name
            self.cost = cost
            self.damage = damage
            self.damage_type = damage_type
            self.targets_all = targets_all  # True if the skill targets all enemies, False if it targets a single enemy

    # Defining Skills
    fire_ball = Skill("Fire Ball", 3, 15, "Fire", targets_all=False)
    water_gun = Skill("Water Gun", 2, 10, "Water", targets_all=False)
    electro_shock = Skill("Electro Shock", 4, 20, "Thunder", targets_all=False)
    poison_dust = Skill("Poison Dust", 5, 5, "Poison", targets_all=True)  # This skill targets all enemies

    # Player Fighters
    hero = Fighter("Hero", 12, 7, 4, 5, 3, {"Physical": 10, "Mind": 0, "Fire": 5, "Water": 5, "Thunder": 0, "Earth": -5}, {"Poison": 25, "Constrain": 50, "Sleep": 25}, [fire_ball], "frame_hero_bg.png")
    mage = Fighter("Mage", 8, 3, 10, 4, 6, {"Physical": -10, "Mind": 20, "Fire": 10, "Water": 10, "Thunder": 15, "Earth": 0}, {"Poison": 30, "Constrain": 20, "Sleep": 40}, [water_gun], "frame_mage_bg.png")
    berserker = Fighter("Berserker", 15, 10, 2, 6, 1, {"Physical": 15, "Mind": -5, "Fire": 0, "Water": -5, "Thunder": -10, "Earth": 20}, {"Poison": 10, "Constrain": 60, "Sleep": 15}, [electro_shock], "frame_berserker_bg.png")
    ranger = Fighter("Ranger", 10, 6, 5, 8, 4, {"Physical": 5, "Mind": 5, "Fire": -5, "Water": 15, "Thunder": 10, "Earth": 0}, {"Poison": 35, "Constrain": 30, "Sleep": 20}, [poison_dust], "frame_ranger_bg.png")

    # Enemies
    goblinA = Enemy("Goblin", 3, 5, 2, 7, 2, {"Physical": 0, "Mind": -10, "Fire": 5, "Water": 0, "Thunder": -5, "Earth": 10}, {"Poison": 20, "Constrain": 25, "Sleep": 30}, [], {"attack": 70, "guard": 30}, "frame_bg.png", "goblin normal")
    goblinB = Enemy("Goblin", 3, 5, 2, 7, 2, {"Physical": 0, "Mind": -10, "Fire": 5, "Water": 0, "Thunder": -5, "Earth": 10}, {"Poison": 20, "Constrain": 25, "Sleep": 30}, [], {"attack": 70, "guard": 30}, "frame_bg.png", "goblin normal")
    goblinC = Enemy("Goblin", 3, 5, 2, 7, 2, {"Physical": 0, "Mind": -10, "Fire": 5, "Water": 0, "Thunder": -5, "Earth": 10}, {"Poison": 20, "Constrain": 25, "Sleep": 30}, [], {"attack": 70, "guard": 30}, "frame_bg.png", "goblin normal")
    slimeA = Enemy("Slime", 10, 3, 1, 3, 1, {"Physical": 20, "Mind": 0, "Fire": -20, "Water": 50, "Thunder": -10, "Earth": 5}, {"Poison": 50, "Constrain": 0, "Sleep": 0}, [], {"attack": 60, "guard": 40}, "frame_bg.png", "slime normal")
    slimeB = Enemy("Slime", 10, 3, 1, 3, 1, {"Physical": 20, "Mind": 0, "Fire": -20, "Water": 50, "Thunder": -10, "Earth": 5}, {"Poison": 50, "Constrain": 0, "Sleep": 0}, [], {"attack": 60, "guard": 40}, "frame_bg.png", "slime normal")
    tentacle = Enemy("Tentacle", 12, 6, 5, 9, 3, {"Physical": 10, "Mind": 15, "Fire": -5, "Water": 20, "Thunder": 0, "Earth": -10}, {"Poison": 25, "Constrain": 50, "Sleep": 20}, [], {"attack": 50, "guard": 50}, "frame_bg.png", "tentacle normal")

    # Assigning skills to Fighters
    hero.skills.append(fire_ball)
    mage.skills.append(water_gun)
    berserker.skills.append(electro_shock)
    ranger.skills.append(poison_dust)

    # Convert the hero's resistances dictionary to a string and store it in a variable
    hero_resistances_str = str(hero.resistances).replace("{", "").replace("}", "").replace("'", "")
    "Hero's HP: [hero.hp], EP: [hero.ep], Resistances: [hero_resistances_str]"