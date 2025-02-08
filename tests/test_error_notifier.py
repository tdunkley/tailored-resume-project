import unittest
from unittest.mock import patch
from error_notifier import send_error_notification

class TestErrorNotifier(unittest.TestCase):

    @patch("smtplib.SMTP")
    def test_send_error_notification(self, mock_smtp):
        send_error_notification("Test Subject", "Test Message", ["recipient@example.com"])
        mock_smtp.assert_called_with("smtp.example.com", 587)
        instance = mock_smtp.return_value
        instance.starttls.assert_called_once()
        instance.login.assert_called_with("your_email@example.com", "your_password")
        instance.sendmail.assert_called_once()

if __name__ == "__main__":
    unittest.main()
