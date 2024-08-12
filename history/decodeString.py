        """
        Premise
        . given encoding rule of k[encoded_string], decode decodeString

        Constraint
        . 1 <= s.length <= 30
        . s are rule compliant and always valid.
        . 1 <= s <= 300
        """
        decodedString = [] # array to bypass complexity of string concat
        kStack = [] # stack to track (index of k, k)
        currK = [] # stores current k
        
        for i, c in enumerate(s):
            if c.isdigit():
                currK.append(c)
            if c == "[":
                kStack.append((len(decodedString), int("".join(currK))))
                currK = []
            elif c.isalpha():
                decodedString.append(c)
            elif c == "]":
                start, k = kStack.pop()
                toDecode = decodedString[start:]
                decodedString.extend(toDecode * (int(k) - 1))

        return "".join(decodedString)
