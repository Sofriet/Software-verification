import random


class Mutator:
    def mutate(self, s: str):
        """
        randomly stack mutators 1-5 times.

        :param s: the input string
        :return s: the mutated string
        """
        # for question 1 variant comment out lines 13-20 and change for each execution the mutator, for example s = self.swap_characters(s)
        num_mutators = random.randint(1, 5)
        for _ in range(num_mutators):
            mutator = random.choice([
                self.insert_random_character,
                self.remove_random_character,
                self.swap_characters,
                self.scramble_characters,
                self.invert_characters
            ])
            s = mutator(s)
        return s

    @staticmethod
    def insert_random_character(s: str) -> str:
        """
        insert a character from ASCII printable characters and the extended ASCII codes at a random position

        :param s: the input string
        :return s: the mutated string
        """
        random_char = chr(random.randint(32, 126))  # ASCII printable characters
        position = random.randint(0, len(s))
        return s[:position] + random_char + s[position:]

    @staticmethod
    def remove_random_character(s: str) -> str:
        """
        remove a random character from the string

        :param s: the input string
        :return s: the mutated string
        """
        if s:
            position = random.randint(0, len(s) - 1)
            s = s[:position] + s[position + 1:]
        return s

    @staticmethod
    def swap_characters(s: str) -> str:
        """
        randomly swap two characters of the string

        :param s: the input string
        :return s: the mutated string
        """
        if len(s) >= 2:
            positions = random.sample(range(len(s)), 2)
            first_char, second_char = s[positions[0]], s[positions[1]]
            s = s[:positions[0]] + second_char + s[positions[0] + 1:]
            s = s[:positions[1]] + first_char + s[positions[1] + 1:]
        return s

    @staticmethod
    def scramble_characters(s: str) -> str:
        """
        select a random number of characters from the string (which may not be contiguous)
        and randomly shuffle their values

        :param s: the input string
        :return s: the mutated string
        """
        if len(s) <= 1:
            return s
        else:
            num_chars = random.randint(1, len(s))
            positions = random.sample(range(len(s)), num_chars)
            chars_to_scramble = [s[i] for i in positions]
            random.shuffle(chars_to_scramble)
            return ''.join([c if i not in positions else chars_to_scramble.pop() for i, c in enumerate(s)])

    @staticmethod
    def invert_characters(s: str) -> str:
        """
        select a random number of contiguous characters from the string and reverse their order

        :param s: the input string
        :return s: the mutated string
        """
        if len(s) >= 2:
            start = random.randint(0, len(s) - 2)
            end = random.randint(start + 1, len(s))
            substring_list = list(s[start:end])
            substring_list.reverse()
            s = s[:start] + ''.join(substring_list) + s[end:]
        return s