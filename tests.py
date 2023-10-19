import unittest as UT
import pytest
import otp2 as OTP
class TestOtp(UT.TestCase):
    def test_validatemail(self):
        result = OTP.validateEmailID("aradwadrushabhgmail.com")
        expected = True
        self.assertEqual(result, expected)

    def test_validatemail(self):
        result = OTP.validateEmailID("aradwadrushabh@gmaicom")
        expected = True
        self.assertEqual(result, expected)

    def test_generateotp(self):
        otp_len = len(OTP.generateOtp())
        expected_len = 6
        self.assertEqual(otp_len, expected_len)
        resut_type = OTP.generateOtp()
        otp_type = resut_type.isdigit()
        expected_type = True
        self.assertEqual(otp_type, expected_type)
if __name__ == '__main__':
    pytest.main()
