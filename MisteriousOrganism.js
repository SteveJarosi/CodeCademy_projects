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
  
        console.log(`specimen #${spec.specimen} and specimen #${this.specimen} have ${perc}% DNA in common`)
      },
      willLikelySurvive() {
        if (true) {
          return true
        } else return false
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
    if (newBug.willLikelySurvive() === true) {
      viableBugs.push(newBug)
    }
    num++
  }
  console.log(viableBugs)
  let joe = pAequorFactory(42, mockUpStrand())
  console.log(joe)
  joe.mutate()
  console.log(joe)
  
  
  
  
  
  
  