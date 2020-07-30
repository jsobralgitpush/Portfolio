module Raindrops
  def self.convert(number)
    factors = []
    string_answer = ''

    if number >= 3
      if number % 7 == 0
        factors.append(7)
      end
      
      if number % 5 == 0
        factors.append(5)
      end

      if number % 3 == 0
        factors.append(3)
      end

    else
      return number.to_s
    end

    if factors.length() == 0
      return number.to_s
    end

    for i in factors.sort()

      if i == 3
        string_answer += 'Pling'
      elsif i == 5
        string_answer += 'Plang'
      elsif i == 7
        string_answer += 'Plong'
      else
        return number.to_s
      end

    end

    return string_answer



  end
end