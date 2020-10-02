import pytest
import wave.data.likeness as likeness

class TestLikenessFDS:
    def testRoundedLikenessFDS(self):
        likeness_instance = likeness.WaveLikeness(
            base=[i for i in range(64)],
            comparison=[0 for i in range(64)],
            ceiling=64
        )

        assert 31.46 == likeness_instance.getLikeness()

    def testExactRoundedLikenessFDS(self):
        likeness_instance = likeness.WaveLikeness(
            base=[i for i in range(64)],
            comparison=[i for i in range(64)],
            ceiling=64
        )

        assert 100.00 == likeness_instance.getLikeness()

    def testSinglePercentageNamco(self):
        likeness_instance = likeness.WaveLikeness(
            base=[i for i in range(64)],
            comparison=[0 for i in range(64)],
            ceiling=64
        )

        assert 100.00 == likeness_instance.getPercentage(0, 0)
        assert 0.00 == likeness_instance.getPercentage(63, 63)

class TestLikenessNamco:
    def testExactRoundedLikenessNamco(self):
        likeness_instance = likeness.WaveLikeness(
            base=[i for i in range(16)],
            comparison=[i for i in range(16)],
            ceiling=16
        )

        assert 100.00 == likeness_instance.getLikeness()

    def testRoundedLikenessNamco(self):
        likeness_instance = likeness.WaveLikeness(
            base=[i for i in range(16)],
            comparison=[0 for i in range(16)],
            ceiling=16
        )

        assert 33.71 == likeness_instance.getLikeness()

    def testSinglePercentageNamco(self):
        likeness_instance = likeness.WaveLikeness(
            base=[i for i in range(16)],
            comparison=[0 for i in range(16)],
            ceiling=16
        )

        assert 100.00 == likeness_instance.getPercentage(0, 0)
        assert 0.00 == likeness_instance.getPercentage(15, 15)
