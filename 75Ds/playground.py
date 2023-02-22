def incExc1():
    probabilities = [1/66, 1/66, 1/66, 1/66, 1/66, 1/66]
    result = 1
    
    for i in range(len(probabilities)):
        result -= probabilities[i]
        print(result)
        for j in range(i + 1, len(probabilities)):
            result += probabilities[i] * probabilities[j]
            for k in range(j + 1, len(probabilities)):
                result -= probabilities[i] * probabilities[j] * probabilities[k]
                for l in range(k + 1, len(probabilities)):
                    result += probabilities[i] * probabilities[j] * probabilities[k] * probabilities[l]
                    for m in range(l + 1, len(probabilities)):
                        result -= probabilities[i] * probabilities[j] * probabilities[k] * probabilities[l] * probabilities[m]
                        for n in range(m + 1, len(probabilities)):
                            result += probabilities[i] * probabilities[j] * probabilities[k] * probabilities[l] * probabilities[m] * probabilities[n]
    
    return result

def incExc2():
    result = 1
    
    for i in range(6):
        result -= 1/66
        print(result)
        for j in range(i + 1, 6):
            result += 1/66 * 1/45
            for k in range(j + 1, 6):
                result -= 1/66 * 1/45 * 1/28
                for l in range(k + 1, 6):
                    result += 1/66 * 1/45 * 1/28 * 1/15
                    for m in range(l + 1, 6):
                        result -= 1/66 * 1/45 * 1/28 * 1/15 * 1/6
                        for n in range(m + 1, 6):
                            result += 1/66 * 1/45 * 1/28 * 1/15 * 1/6 * 1
    
    return result

print(f'version 1: {incExc1()}\n')
print(f'version 2: {incExc2()}')