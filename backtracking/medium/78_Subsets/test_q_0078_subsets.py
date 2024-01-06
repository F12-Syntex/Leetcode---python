import pytest
from q_0078_subsets import Solution


@pytest.mark.parametrize(
    "nums, output",
    [
        ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        ([0], [[], [0]]),
    ],
)
class TestSolution:
    def test_subsets(self, nums, output):
        sc = Solution()
        assert (
            sc.subsets(
                nums,
            )
            == output
        )
