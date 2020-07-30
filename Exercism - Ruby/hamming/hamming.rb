module Hamming
  def self.compute(dna,mutation)
    dna = dna.split('')
    mutation = mutation.split('')

    counter = 0

    if dna.length() != mutation.length()
      raise ArgumentError
    end

    i = 0 
    while i != dna.length()
      if dna[i] != mutation[i]
        counter +=1
      end
      i +=1
    end

    return counter
  end

end