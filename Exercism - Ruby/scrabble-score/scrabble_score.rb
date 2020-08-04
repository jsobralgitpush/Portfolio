class Scrabble
  def initialize(word)
    @word = word
  end

  def score

    if @word != nil
      array_word = @word.split('')
    else
      return 0
    end

    dict_count = {
      ["a", "e", "i","o","u","l","n","r","s","t"] =>1,
      ["d","g"] => 2,
      ["b","c","m","p"] => 3,
      ["f","h","v","w","y"] => 4,
      ["k"] => 5,
      ["j","x"] => 8,
      ["q", "z"] => 10
    }

    answer = 0

    for i in array_word
      for j in dict_count
        for k in j[0]
          if i.downcase == k
            answer += j[1]
          end
        end
      end
    end

    return answer
  end

  def self.score(word)
    array_word = word.split('')

    dict_count = {
      ["a", "e", "i","o","u","l","n","r","s","t"] =>1,
      ["d","g"] => 2,
      ["b","c","m","p"] => 3,
      ["f","h","v","w","y"] => 4,
      ["k"] => 5,
      ["j","x"] => 8,
      ["q", "z"] => 10
    }

    answer = 0

    for i in array_word
      for j in dict_count
        for k in j[0]
          if i.downcase == k
            answer += j[1]
          end
        end
      end
    end

    return answer
  end

end
