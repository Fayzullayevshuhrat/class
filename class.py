# class Math:
#
#
#     @staticmethod
#     def add(a , b):
#         return a + b
#     @staticmethod
#     def minus(a , b):
#         return a - b
#
# print(Math.add(2,6))
# print(Math.minus(6,3))


class Static:
    @staticmethod
    def static_islower_text(text):
        if text.islower():
            return text.upper()
        return text



    @staticmethod
    def static_remove_numbers_sorted_text(text):
        letters = [char for char in text if char.isalpha()]
        return ''.join(sorted(letters))



    @staticmethod
    def static_remove_numbers_text(text):
        return ''.join(char for char in text if not char.isdigit())

    @staticmethod
    def static_isupper_text(text):
        if text.isupper():
            return text.lower()
        return text
