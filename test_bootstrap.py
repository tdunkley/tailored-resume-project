import unittest
import os
from unittest.mock import patch, MagicMock

class TestBootstrap(unittest.TestCase):
    @patch("bootstrap.logging")
    @patch("bootstrap.load_resume_data")
    @patch("bootstrap.section_processor")
    def test_happy_path(self, mock_section_processor, mock_load_resume_data, mock_logging):
        mock_load_resume_data.return_value = {
            "sections": {"personal_information": {}, "summary": {}, "skills": {}}
        }
        mock_section_processor.return_value = None

        # Run bootstrap
        from bootstrap import main
        main()

        # Assert the process runs without issues
        self.assertTrue(mock_section_processor.called)

    @patch("bootstrap.logging")
    def test_missing_config(self, mock_logging):
        # Simulate missing config.json
        with patch("os.path.exists", return_value=False):
            from bootstrap import main
            with self.assertRaises(FileNotFoundError):
                main()

    @patch("bootstrap.logging")
    def test_missing_resume_json(self, mock_logging):
        # Simulate missing resume.json
        with patch("os.path.exists", side_effect=lambda x: False if "resume.json" in x else True):
            from bootstrap import main
            with self.assertRaises(FileNotFoundError):
                main()

if __name__ == "__main__":
    unittest.main()
