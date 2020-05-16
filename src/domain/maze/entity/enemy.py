from src.domain.maze.entity.character import Character


class Enemy(Character):
    def start(self):
        self.case = self.maze.end
