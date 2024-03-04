class Job:
    def __init__(self, name, skills, starting_weapon, starting_armor, saving_throws) -> None:
        self.name : str = name
        self.skills : list[str] = skills
        self.weapon = starting_weapon
        self.armor = starting_armor
        self.saving_throws = saving_throws
