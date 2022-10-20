import pytest
import sys
from pathlib import Path
from deepdiff import DeepDiff

SRC_PATH = str(Path(__file__).parent / '..' / 'src')
sys.path.insert(0, SRC_PATH)

from randomGenerator import randomGenerator

def test_randomGenerator():
    solution_maxtrix = [[1, 1, 0, 1], [0, 1, 0, 1], [0, 1, 1, 1], [1, 1, 0, 1]]
    rg = randomGenerator(seed=123, threshold=0.35, fieldX=4, fieldY=4);
    matrix = rg.generateMatrix();
    assert DeepDiff(solution_maxtrix, matrix) == {}