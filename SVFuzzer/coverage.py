from sys import settrace
from typing import Callable
from html.parser import HTMLParser
from mutator import Mutator
import random


class Coverage:
    def __init__(self, target_file: str, to_exec: Callable, inp: str):
        """
        Constructor for Coverage

        :param target_file: the file used to calculate the coverage
        :param to_exec: the function/method to execute
        :param inp: the input for to_exec
        """
        self.target_file = target_file
        self.to_exec = to_exec
        self.inp = inp
        self.cov_lines_list = []    # list of covered lines (used to fill the cov_pairs_set)
        self.cov_lines_set = set()  # set of covered lines
        self.cov_pairs_set = set()  # set of covered pairs of lines

    def same_set(self, covered: set, coverage_type: int):
        """
        returns true if the set in self (cov_lines_set if the coverage_type is 0 else cov_pairs_set) is equal to covered, else false
        """
        if(coverage_type == 0):
            return self.cov_lines_set == covered
        else:
            return self.cov_pairs_set == covered
        
    def get_cov_set_for_type(self, coverage_type: int):
        """
        returns cov.cov_lines_set if the coverage_type is 0, else it returns cov_pairs_set
        """
        if(coverage_type == 0):
            return self.cov_lines_set
        else:
            return self.cov_pairs_set


    def trace_lines_and_fill_set(self, frame, event, arg = None):
        """
        the tracer, returns itself and fills the cov_lines_set and cov_pairs_set using cov_lines_list
        """
        initial_size = len(self.cov_lines_list)
        # check line events and the target file
        if (event == "line" and frame.f_code.co_filename.endswith(self.target_file)):
            self.cov_lines_set.add(frame.f_lineno)
            self.cov_lines_list.append(frame.f_lineno)

            #than the pairs
            if (len(self.cov_lines_list) > initial_size and len(self.cov_lines_list) > 1):
                self.cov_pairs_set.add((self.cov_lines_list[-2], self.cov_lines_list[-1]))

        return self.trace_lines_and_fill_set

    
    def coverage_runner(self):
        """
        Calculate the covered lines and pairs of lines
        return True if no exception was thrown (test passed)
        return False if there is exception (test failed)
        """
        try:
            settrace(self.trace_lines_and_fill_set)
            self.to_exec(self.inp)

        except Exception as e:
            # print(f"Exception during tracing: {e}")
            return False

        finally:
            settrace(None)

        return True

                

            
