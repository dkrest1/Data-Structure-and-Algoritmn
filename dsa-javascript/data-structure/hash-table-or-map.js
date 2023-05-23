//console.log("a".charCodeAt(0));
//console.log("hi".charCodeAt(1));
//subtracting 96 for the code will give the alphabetic postion of the string or letter

//BIG O
// access = O(1)
// removal = O(1)
// insertion = O(1)

//simple hash function
// function hash(key, arrayLen) {
//     let total = 0;
//     let WEIRD_PRIME = 31
//     for (let i = 0; i < Math.min(key.length, 100); i++) {
//         let char = key[i]
//         let value = char.charCodeAt(0) - 96;
//         total = ((total * WEIRD_PRIME) + value) % arrayLen;
//     }
//     return total;
// }

class HashTable {

    constructor(size = 53) {
        this.keyMap = new Array(size);
    }

    _hash(key) {
        let total = 0;
        let WEIRD_PRIME = 31
        for (let i = 0; i < Math.min(key.length, 100); i++) {
            let char = key[i];
            let value = char.charCodeAt(0) - 96;
            total = (total * WEIRD_PRIME + value) % this.keyMap.length;
        }
        return total;
    }

    set(key, value) {
        let index = this._hash(key);
        if (!this.keyMap[index]) {
            this.keyMap[index] = [];
        }
        this.keyMap[index].push([key, value])
    }

    get(key) {
        let index = this._hash(key);
        if (this.keyMap[index]) {
            for (let i = 0; i < this.keyMap[index].length; i++) {
                if (this.keyMap[index][i][0] === key) {
                    return this.keyMap[index][i]
                }
            }
        }
        return undefined;
    }

    values() {
        let valueArr = [];
        for (let i = 0; i < this.keyMap.length; i++) {
            if (this.keyMap[i]) {
                for (let j = 0; j < this.keyMap[i].length; j++) {
                    if (!valueArr.includes(this.keyMap[i][j][1])) {
                        valueArr.push(this.keyMap[i][j][1])
                    }
                }
            }
        }

        return valueArr
    }

    keys() {
        let keyArr = [];
        for (let i = 0; i < this.keyMap.length; i++) {
            if (this.keyMap[i]) {
                for (let j = 0; j < this.keyMap[i].length; j++) {
                    if (!keyArr.includes(this.keyMap[i][j][0])) {
                        keyArr.push(this.keyMap[i][j][0])
                    }
                }
            }
        }
        return keyArr
    }
}


let ht = new HashTable(3);
ht.set("name", "oluwatosin");
ht.set("name", "oluwamayowa");
ht.set("female", "busayo");
ht.set("gender", "busayo");
// console.log(ht.keyMap);
// console.log(ht.get("gender"));
// console.log(ht.values());
console.log(ht.keys());