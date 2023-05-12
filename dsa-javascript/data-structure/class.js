class Student {
    constructor(firstName, lastName, grade, tardies) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.grade = grade;
        this.tardies = tardies;
        this.scores = [];
    }

    getFullname() {
        return `My fullname is ${this.firstName} ${this.lastName}`
    }

    markLate() {
        this.tardies += 1
        if (this.tardies >= 3) {
            return `You are EXPELLED!`
        }
        return `${this.firstName} ${this.lastName} has been late ${this.tardies} times.`
    }

    addScore(score) {
        this.scores.push(score)
        return this.scores
    }

    calculateAverage() {
        let sum = this.scores.reduce((a, b) => a + b)
        return sum / this.scores.length;
    }

    static enrolStudent() {
        return `We are enrolling students...`
    }
}

// instantiatin an object from a class
let firstStudent = new Student("oluwatosin", "akande", "first class", 5);
let secondStudent = new Student('oluwamayowa', "akande");

console.log(firstStudent.getFullname())
console.log(firstStudent.markLate())
console.log(firstStudent.addScore(90))
console.log(firstStudent.addScore(89))
console.log(firstStudent.addScore(96))
console.log(firstStudent.calculateAverage())
console.log(Student.enrolStudent())

//instance method
