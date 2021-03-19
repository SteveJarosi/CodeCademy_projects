// Returns a random DNA base
const returnRandBase = () => {
    const dnaBases = ['A', 'T', 'C', 'G']
    return dnaBases[Math.floor(Math.random() * 4)] 
  }
  
  // Returns a random single stand of DNA containing 15 bases
  const mockUpStrand = () => {
    const newStrand = []
    for (let i = 0; i < 15; i++) {
      newStrand.push(returnRandBase())
    }
    return newStrand
  }
  
  function pAequorFactory(number, array) {
    return {
      specimen: number,
      dna: array,
      mutate() {
        let baseMutationIndex = Math.floor(Math.random() * 16)
        let baseMutation = returnRandBase()
        while (this.dna[baseMutationIndex] === baseMutation) {
          baseMutation = returnRandBase()
        }
        console.log("Mutation:", baseMutationIndex, this.dna[baseMutationIndex], baseMutation)
        this.dna[baseMutationIndex] = baseMutation
        return this.dna
      },
      compareDNA(spec) {
        let commonBaseNr = 0
        for (i=0; i< this.dna.length; i++) {
          if (this.dna[i] === spec.dna[i]) {
            commonBaseNr++
          }
        }
        let perc = Math.round(10000 * commonBaseNr / this.dna.length)/100
        console.log(`specimen #${spec.specimen} and specimen #${this.specimen} have ${perc}% DNA in common`)
      },
      willLikelySurvive() {
        let goodBaseNr = 0
        for (i=0; i< this.dna.length; i++) {
          if (this.dna[i] === 'C' || this.dna[i] === 'G') {
            goodBaseNr++
          }
        }
        let perc = Math.round(10000 * goodBaseNr / this.dna.length)/100
        return perc >= 60
      }
    }
  }
  let syringe = []
  let viableBugs = []
  let newBug = {}
  let num = 1
  while (viableBugs.length < 30) {
    newBug = pAequorFactory(num, mockUpStrand())
    syringe.push(newBug)
    console.log(newBug)
    console.log("Will survive?",newBug.willLikelySurvive())
    if (newBug.willLikelySurvive() === true) {
      viableBugs.push(newBug)
    }
    num++
  }
  
  let joe = pAequorFactory(42, mockUpStrand())
  console.log(joe)
  joe.mutate()
  console.log(joe)
  joe.compareDNA(syringe[23])
  
  
  
  
  
  
  