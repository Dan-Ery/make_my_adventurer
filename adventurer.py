import random
from job import Job

class Adventurer:

    def __init__(self, name: str, species: str, seed = None) -> None:
        if seed:
            random.seed(seed)
 
        self.prof_bonus = 2
        self.name = name
        self.species = species

        self.pick_stats()
        self.pick_job()

    def pick_stats(self):
        standard_stat_array = [15, 14, 13, 12, 10, 8]
        random.shuffle(standard_stat_array)
        stats = {}
        stats['strength']=standard_stat_array[0]
        stats['dexterity']=standard_stat_array[1]
        stats['consitution']=standard_stat_array[2]
        stats['intelligence']=standard_stat_array[3]
        stats['wisdom']=standard_stat_array[4]
        stats['charisma']=standard_stat_array[5]
        self.stats : dict[str,int] = stats

    def pick_job(self):
        base_jobs = [
            Job(
                'fighter',
                ['athletics', 'intimidation'],
                'longsword',
                ('chainmail', lambda adv : 16),
                ['strength', 'constitution']
            ),
            Job(
                'thief',
                ['acrobatics', 'deception', 'sleight of hand', 'stealth'],
                'dagger',
                ('padded armor', lambda adv: 11 + adv.get_dex_mod()),
                ['dexterity', 'intelligence']
            ),
            Job(
                'magic user',
                ['arcana', 'history'],
                'staff',
                ('robe and a wizard hat', lambda adv : adv.get_dex_mod()),
                ["intelligence", "wisdom"]
            )
        ]
        self.job = (random.sample(base_jobs,1))[0]

    def create_description(self) -> str:
        job = self.job

        name_line = f"{self.name} is a {self.species} {job.name}."
        stat_line = (f"Strength: {self.get_strength()} (STR: {self.get_str_mod()}) | " +
            f"Dexterity: {self.get_dexterity()} (DEX: {self.get_dex_mod()}) | " +
            f"Constitution: {self.get_constitution()} (CON: {self.get_con_mod()}) |"
            f"Intelligence: {self.get_intelligence()} (INT: {self.get_int_mod()}) |"
            f"Wisom: {self.get_wisdom()} (WIS: {self.get_wis_mod()}) |"
            f"Charisma: {self.get_charisma()} (CHA: {self.get_cha_mod()})"
        )
        armor_class_func = job.armor[1]
        ac_line = f"Armor Class: {armor_class_func(self)}"
        equip_line = f"They wield a {job.weapon}, and wear a set of {job.armor[0]}."
        skill_line = self._create_skill_line(job.skills)

        return f"{name_line}\n{stat_line}\n{ac_line}\n{equip_line}\n{skill_line}"

    def _create_skill_line(self, trained_skills : list[str]):
        skill_line = "They are trained in"
        if not trained_skills:
            return f"{skill_line} no skills."
        elif len(trained_skills) == 1:
            return f"{skill_line} {trained_skills[0]}."

        elif len(trained_skills) == 2:
            return f"{skill_line} {trained_skills[0]} and {trained_skills[1]}."
        else:
            for i in range(0, len(trained_skills)-1):
                skill_line = f"{skill_line} {trained_skills[i]},"
            return f"{skill_line} and {trained_skills[len(trained_skills)-1]}"

    def get_strength(self):
        return self.stats['strength']
    def get_str_mod(self):
        return (self.get_strength() - 10) // 2

    def get_dexterity(self):
        return self.stats['dexterity']
    def get_dex_mod(self):
        return (self.get_dexterity() - 10) // 2

    def get_constitution(self):
        return self.stats['consitution']
    def get_con_mod(self):
        return (self.get_constitution() - 10) // 2

    def get_intelligence(self):
        return self.stats['intelligence']
    def get_int_mod(self):
        return (self.get_intelligence() - 10) // 2

    def get_wisdom(self):
        return self.stats['wisdom']
    def get_wis_mod(self):
        return (self.get_wisdom() - 10) // 2

    def get_charisma(self):
        return self.stats['charisma']
    def get_cha_mod(self):
        return (self.get_charisma() - 10) // 2
