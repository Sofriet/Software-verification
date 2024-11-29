from typing import List, Callable
from coverage import Coverage
from mutator import Mutator
import random

class SVFuzzer:
    def __init__(self, coverage_type: int, input_num: int, seeds: List[str], target_file: str, function: Callable):
        """
        Constructor of SVFuzzer

        :param coverage_type: type of coverage used for the fuzzing.
            0 stands for line coverage, 1 stands for branch coverage
        :param input_num: the number of generated inputs
        :param seeds: initial inputs given by the user
        :param target_file: the file you will consider for coverage calculation. In this case, "html/parser.py"
        :param function: the function/method you want to fuzz
        """
        self.coverage_type = coverage_type
        self.input_num = input_num
        self.seeds = seeds
        self.target_file = target_file
        self.function = function

    def runs(self):
        """
        Run the fuzzer for input_num times.
        For every 100 runs, print the number of runs and the coverage value
        """
        assert self.seeds #should not be empty

        run_count = 0
        input_corpus = self.seeds
        input_failures = []
        covered = set() #for checking the total coverage of multiple coverage runs on inputs
        cur_input = None
        
        for i in range(self.input_num):
            cur_input = self.seeds[i] if i < len(self.seeds) else Mutator().mutate(random.choice(input_corpus))

            cov = Coverage(self.target_file, self.function, cur_input)
            if not cov.coverage_runner():
                input_failures.append(cur_input)

            # for question 2 variant comment out line 46 and tab back lines 47 and 48 once
            if not cov.same_set(covered, self.coverage_type):
                input_corpus.append(cur_input)
                covered.update(cov.get_cov_set_for_type(self.coverage_type))

            run_count += 1
            if run_count % 100 == 0:
                cov = Coverage(self.target_file, self.function, self.seeds)
                print("Number of runs is: ", run_count)
                print("Lines/Branches covered: ", len(covered))
                print("Number of failed inputs: ", len(input_failures))
                

