module Isogram
  def self.isogram?(input)
    test_isogram = input.split('')
    word_count = {}

    for i in test_isogram
      if word_count[i.downcase] == nil
        word_count[i.downcase] = 1
      else
        word_count[i.downcase] += 1
      end
    end

    for i in word_count
      if i[0] != '-' && i[0] != ' '
        if i[1] > 1
          return false
        end
      end
    end
    
    return "Expected true, '#{input}' is an isogram" 

  end
end