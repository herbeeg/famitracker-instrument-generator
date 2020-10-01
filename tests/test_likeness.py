import pytest
import wave.data.likeness as likeness

class TestLikenessFDS:
    def testRoundedLikenessFDS(self):
        assert True == True

class TestLikenessNamco:
    def testRoundedLikenessNamco(self):
        likeness_instance = likeness.WaveLikeness(
            base=[i for i in range(16)],
            comparison=[0 for i in range(16)],
            ceiling=16
        )

        assert True == True
    
    def testExactRoundedLikenessNamco(self):
        likeness_instance = likeness.WaveLikeness(
            base=[i for i in range(16)],
            comparison=[i for i in range(16)],
            ceiling=16
        )

        assert 100.00 == likeness_instance.getLikeness()
