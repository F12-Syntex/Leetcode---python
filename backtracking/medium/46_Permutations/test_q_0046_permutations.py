import pytest
from q_0046_permutations import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
    ],
)
class TestSolution:
    def test_permute(self, nums, output):
        sc = Solution()
        assert (
            sc.permute(
                nums,
            )
            == output
        )
