// All valid credit card numbers
const valid1 = [4, 5, 3, 9, 6, 7, 7, 9, 0, 8, 0, 1, 6, 8, 0, 8];
const valid2 = [5, 5, 3, 5, 7, 6, 6, 7, 6, 8, 7, 5, 1, 4, 3, 9];
const valid3 = [3, 7, 1, 6, 1, 2, 0, 1, 9, 9, 8, 5, 2, 3, 6];
const valid4 = [6, 0, 1, 1, 1, 4, 4, 3, 4, 0, 6, 8, 2, 9, 0, 5];
const valid5 = [4, 5, 3, 9, 4, 0, 4, 9, 6, 7, 8, 6, 9, 6, 6, 6];

// All invalid credit card numbers
const invalid1 = [4, 5, 3, 2, 7, 7, 8, 7, 7, 1, 0, 9, 1, 7, 9, 5];
const invalid2 = [5, 7, 9, 5, 5, 9, 3, 3, 9, 2, 1, 3, 4, 6, 4, 3];
const invalid3 = [3, 7, 5, 7, 9, 6, 0, 8, 4, 4, 5, 9, 9, 1, 4];
const invalid4 = [6, 0, 1, 1, 1, 2, 7, 9, 6, 1, 7, 7, 7, 9, 3, 5];
const invalid5 = [5, 3, 8, 2, 0, 1, 9, 7, 7, 2, 8, 8, 3, 8, 5, 4];

// Can be either valid or invalid
const mystery1 = [3, 4, 4, 8, 0, 1, 9, 6, 8, 3, 0, 5, 4, 1, 4];
const mystery2 = [5, 4, 6, 6, 1, 0, 0, 8, 6, 1, 6, 2, 0, 2, 3, 9];
const mystery3 = [6, 0, 1, 1, 3, 7, 7, 0, 2, 0, 9, 6, 2, 6, 5, 6, 2, 0, 3];
const mystery4 = [4, 9, 2, 9, 8, 7, 7, 1, 6, 9, 2, 1, 7, 0, 9, 3];
const mystery5 = [4, 9, 1, 3, 5, 4, 0, 4, 6, 3, 0, 7, 2, 5, 2, 3];

// An array of all the arrays above
const batch = [valid1, valid2, valid3, valid4, valid5, invalid1, invalid2, invalid3, invalid4, invalid5, mystery1, mystery2, mystery3, mystery4, mystery5];


// Add your functions below:

function validateCred(array) {
    let newArr = []
    newArr.unshift(array[array.length - 1])
    for (i = array.length - 2; i >= 0; i--) {
        // console.log(array[i], i)
        if ((array.length % 2 + i) % 2 == 0) {
            let k = array[i] * 2;
            if (k > 9) {
                k = k - 9
            }
            newArr.unshift(k)
        } else {
            newArr.unshift(array[i])
        }

    }
    let s = newArr.reduce((a, b) => a + b)
    // console.log(s)
    return s % 10 ? false : true
}
//console.log(valid1)
//console.log(validateCred(valid1))

function fixInvalidCards(cardArray) {
    let invalidArray = []
    for (card of cardArray) {
        if (!validateCred(card)) {
            invalidArray.push(card)
        }
        console.log(card, validateCred(card), idInvalidCardCompanies([card]))
    }
    return invalidArray
}

//console.log(fixInvalidCards(batch))

function idInvalidCardCompanies(invArray) {
    let compArray = []
    for (card of invArray) {
        //console.log(card)
        switch (card[0]) {
            case 3:
                if (!compArray.includes('Amex')) {
                    compArray.push('Amex')
                }
                break
            case 4:
                if (!compArray.includes('Visa')) {
                    compArray.push('Visa')
                }
                break
            case 5:
                if (!compArray.includes('Mastercard')) {
                    compArray.push('Mastercard')
                }
                break
            case 6:
                if (!compArray.includes('Discover')) {
                    compArray.push('Discover')
                }
                break
            default:
                console.log('Company not found!', card[0])
                break
        }
    }
    return compArray
}

console.log(idInvalidCardCompanies(fixInvalidCards(batch)))
let testCardNumbers = `
VISA:
4485040934039837
4532697451742482
4929536551512847170
MasterCard:
5103788656221145
5144996540451684
2720994326285623
American Express (AMEX):
378948809312642
348091560348856
376226942812303
Discover:
6011480956869562
6011998493192008
6011212581902353584
JCB:
3540906896579157
3543396907688279
3529822051683346112
Diners Club - North America:
5418495990119114
5500310764404908
5548191875256187
Diners Club - Carte Blanche:
30266671618578
30165187826677
30384252107760
Diners Club - International:
36759905137310
36310519098660
36823808888518
Maestro:
0604955276172850
0604249491323690
6304093512928578
Visa Electron:
4844595422384330
4508425017628635
4917409299381589
InstaPayment:
6373047161795205
6388737261937656
6389659192170612`

console.log(testCardNumbers)
let testArray = testCardNumbers.split("\n")
console.log(testArray)
let newTests = []
for (line of testArray) {
    console.log(typeof Number(line), Number(line))
    if (Number(line) > 0) {
        let newLine = line.split('')
        let numArray = []
        for (i of newLine) {
            numArray.push(parseInt(i))
        }

        newTests.push(numArray)
    }
}
console.log(newTests)
console.log(batch)
console.log(idInvalidCardCompanies(fixInvalidCards(newTests)))