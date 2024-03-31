class Activity {
    constructor(name, caloriesPerMinute) {
        this.name = name;
        this.caloriesPerMinute = caloriesPerMinute;
    }
}

//  includes the name of the activity and the number of calories burned per minute. 

class User {
    constructor(name, age, weight, height) {
        this.name = name;
        this.age = age;
        this.weight = weight;
        this.height = height;
        this.activities = [];
    }

    addActivity(activity, duration) {
        this.activities.push({activity, duration});
    }

    calculateCalories() {
        let totalCalories = 0;
        for(let activity of this.activities) {
            totalCalories += activity.duration * activity.activity.caloriesPerMinute;
        }
        return totalCalories;
    }
}

// Define some activities
let running = new Activity('running', 10);
let swimming = new Activity('swimming', 8);

// Usage
let user = new User('John Doe', 30, 75, 180);
user.addActivity(running, 30);
user.addActivity(swimming, 60);
console.log(user.calculateCalories());
