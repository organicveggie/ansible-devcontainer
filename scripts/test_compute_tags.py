import unittest

import combos
import compute_tags


class TestTags(unittest.TestCase):
    def test_without_alias(self):
        self.assertEqual(
            compute_tags.release_tags(
                "5.0.1", combos.Combo("3.14", combos.OSRelease.BOOKWORM)
            ),
            [
                "5.0.1-py3.14-bookworm",
                "5.0-py3.14-bookworm",
                "5-py3.14-bookworm",
                "py3.14-bookworm-latest",
            ],
        )

    def test_with_alias(self):
        self.assertEqual(
            compute_tags.release_tags(
                "5.0.1", combos.Combo("3.14", combos.OSRelease.NOBLE)
            ),
            [
                "5.0.1-py3.14-24.04",
                "5.0-py3.14-24.04",
                "5-py3.14-24.04",
                "py3.14-24.04-latest",
                "5.0.1-py3.14-noble",
                "5.0-py3.14-noble",
                "5-py3.14-noble",
                "py3.14-noble-latest",
            ],
        )

    def test_canonical(self):
        self.assertEqual(
            compute_tags.release_tags(
                "5.0.1",
                combos.Combo(combos.CANONICAL_PYTHON, combos.CANONICAL_OS_RELEASE),
            ),
            [
                "5.0.1-py3.14-trixie",
                "5.0-py3.14-trixie",
                "5-py3.14-trixie",
                "py3.14-trixie-latest",
                "5.0.1",
                "5.0",
                "5",
                "latest",
            ],
        )


if __name__ == "__main__":
    unittest.main()
