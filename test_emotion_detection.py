"""Unit tests for the EmotionDetection package."""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test dominant-emotion classification."""

    def test_joy(self):
        """A happy statement should have joy as its dominant emotion."""
        result = emotion_detector("I am glad this happened.")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """An angry statement should have anger as its dominant emotion."""
        result = emotion_detector("I am really mad about this.")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """A disgusted statement should have disgust as its dominant emotion."""
        result = emotion_detector(
            "I feel disgusted just hearing about this."
        )
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        """A sad statement should have sadness as its dominant emotion."""
        result = emotion_detector("I am so sad about this.")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        """A fearful statement should have fear as its dominant emotion."""
        result = emotion_detector(
            "I am really afraid that this will happen."
        )
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()