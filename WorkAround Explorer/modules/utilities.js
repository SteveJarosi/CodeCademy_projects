function formatNumber(number) {
    let formattedNum = []
    let numToFormat = String(number).split('.')
    if (numToFormat[1] == undefined) {
        numToFormat[1] = '00';
    }
    for (let i = numToFormat[0].length - 1; i >= 0; i--) {
        formattedNum.push(numToFormat[0][i])
        if ((i % 3 == 0) && (i > 0)) {
            formattedNum.push(',')
        }
    }
    return formattedNum.reverse().join('') + '.' + numToFormat[1]
}

export { formatNumber }