class Player:
    name: str
    hp: int
    mp: int
    skills: dict

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        skills = [x for x in self.skills.keys()]

        if skill_name not in skills:
            self.skills[skill_name] = mana_cost
            return f'Skill {skill_name} added to the collection of the player {self.name}'
        return f'Skill already added'

    def player_info(self):
        data = f'Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n'
        for (k, v) in self.skills.items():
            data += f'==={k} - {v}\n'
        return data
