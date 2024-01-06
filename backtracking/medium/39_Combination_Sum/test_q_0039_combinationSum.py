import pytest
from q_0039_combinationSum import Solution


@pytest.mark.parametrize(
    "candidates, target, output",
    [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
    ],
)
class TestSolution:
    def test_combinationSum(
        self, candidates, target, output
    ):
        sc = Solution()
        assert (
            sc.combinationSum(
                candidates,
                target,
            )
            == output
        )
