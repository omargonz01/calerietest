class User:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.streak = 0

    def log_daily_streak(self):
        # Add points for maintaining a daily log streak
        if self.streak >= 5:
            self.points += 20 * self.streak
            print(f"{self.name} logged a meal for {self.streak} consecutive days and earned {20 * self.streak} points!")
        else:
            self.points += 10
            print(f"{self.name} logged a meal and earned 10 points!")
        self.streak += 1

    def log_healthy_meal(self, meal):
        # Add points for choosing a healthy meal option
        self.points += 25
        print(f"{self.name} logged a healthy meal '{meal}' and earned 25 points!")

    def reach_nutrition_goal(self):
        # Add points for reaching a nutrition goal
        self.points += 50
        print(f"{self.name} reached a nutrition goal and earned 50 points!")
    
    def share_achievement(self, platform):
        # Add points for sharing a meal log or achievement on social media
        self.points += 30
        print(f"{self.name} shared a meal log or achievement on {platform} and earned 30 points!")

    def log_exercise(self, exercise):
        # Add points for logging an exercise activity
        self.points += 15
        print(f"{self.name} logged an exercise activity '{exercise}' and earned 15 points!")

    def join_group_challenge(self, challenge_name, group_members):
        # Add points for participating in a group challenge
        self.points += 50
        print(f"{self.name} joined the group challenge '{challenge_name}' with {len(group_members)} other members and earned 50 points!")



    
user = User("Alice")
user.log_healthy_meal("Salad")
user.reach_nutrition_goal()
print(f"{user.name} has {user.points} points.")