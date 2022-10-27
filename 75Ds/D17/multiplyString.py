class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        converted_num1 = 0
        converted_num2 = 0
        for i, n in enumerate(num1):
            converted_num1 += pow(10, (len(num1) - i - 1)) * int(n)
        for i, n in enumerate(num2):
            converted_num2 += pow(10, (len(num2) - i - 1)) * int(n)
            print(converted_num2)

        print(converted_num1, converted_num2)
        
        product = converted_num1 * converted_num2
        converted_product = []
        
        if product == 0:
            return '0'

        print(product)
        
        while product:
            product, n = divmod(product, 10)
            converted_product.append(str(n))
        
        return ''.join(converted_product[::-1])

print(Solution().multiply('9', '99'))