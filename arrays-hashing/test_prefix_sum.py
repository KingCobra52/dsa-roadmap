import pytest

from prefix_sum import build_prefix, build_prefix_v2  # adjust import


def naive_prefix_sum(input_list):
    """Reference/oracle implementation."""
    result = []
    running = 0
    for x in input_list:
        running += x
        result.append(running)
    return result


TEST_CASES = [
    [],
    [5],
    [1, 2, 3, 4],
    [-1, -2, 3, 4],
    [0, 0, 0],
    list(range(-10, 10)),
]


class TestBuildPrefixAgainstOracle:
    @pytest.mark.parametrize("input_list", TEST_CASES)
    def test_build_prefix_matches_oracle(self, input_list):
        expected = [0] + naive_prefix_sum(input_list)
        assert build_prefix(input_list) == expected

    @pytest.mark.parametrize("input_list", TEST_CASES)
    def test_build_prefix_v2_matches_oracle(self, input_list):
        expected = naive_prefix_sum(input_list)
        assert build_prefix_v2(input_list) == expected


class TestBuildPrefixEquivalence:
    """Compares the two functions directly, accounting for the length/offset difference."""

    @pytest.mark.parametrize("input_list", TEST_CASES)
    def test_v1_and_v2_agree_after_offset(self, input_list):
        v1_result = build_prefix(input_list)
        v2_result = build_prefix_v2(input_list)

        assert len(v1_result) == len(input_list) + 1
        assert len(v2_result) == len(input_list)
        assert v1_result[1:] == v2_result  # will FAIL given v2's current bug


def test_v2_is_actually_buggy():
    """Pins down the known bug: v2 never accumulates because it reads
    prefix_list[i] (still 0) instead of prefix_list[i-1]."""
    input_list = [1, 2, 3, 4]
    result = build_prefix_v2(input_list)
    assert result == input_list  # bug: v2 just returns a copy of the input
    assert result != naive_prefix_sum(input_list)  # confirms it's not a real prefix sum
