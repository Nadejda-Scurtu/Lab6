import unittest
from Import_Function import encrypt_text_AES, decrypt_text_AES

class TestYourModule(unittest.TestCase):

    # Тест 1.1: Проверка, что зашифрованный текст не совпадает с исходным
    def test_encrypt_text_AES_not_equal(self):
        plaintext = "Hello, World!"
        ciphertext = encrypt_text_AES(plaintext)
        self.assertNotEqual(plaintext, ciphertext)

    # Тест 1.2: Проверка, что зашифрованный текст не пуст
    def test_encrypt_text_AES_not_empty(self):
        plaintext_1 = "Hello, World!"
        ciphertext_1 = encrypt_text_AES(plaintext_1)
        self.assertTrue(ciphertext_1)

    # Тест 1.3: Проверка, что зашифрованный текст для одинаковых входных данных всегда одинаковый
    # Зашифрованный текст для одних и тех же данных всегда одинаковый (что является характеристикой алгоритма AES в режиме ECB)
    def test_encrypt_text_AES_same_input(self):
        plaintext_3 = "Hello"
        ciphertext_3_1 = encrypt_text_AES(plaintext_3)
        ciphertext_3_2 = encrypt_text_AES(plaintext_3)
        self.assertEqual(ciphertext_3_1, ciphertext_3_2)
    
    # Тест 2.1: Проверка, что расшифрованный текст совпадает с исходным текстом до зашифровки
    def test_decrypt_text_AES_original_text(self):
      plaintext = "Hello, World!"
      ciphertext = encrypt_text_AES(plaintext)
      decrypted_text = decrypt_text_AES(ciphertext)
      self.assertEqual(plaintext, decrypted_text)

    # Тест 2.2: Проверка, что расшифрованный текст для одинаковых входных данных всегда одинаковый
    def test_decrypt_text_AES_same_input(self):
        plaintext = "Hello"
        ciphertext = encrypt_text_AES(plaintext)
        decrypted_text_1 = decrypt_text_AES(ciphertext)
        decrypted_text_2 = decrypt_text_AES(ciphertext)
        self.assertEqual(decrypted_text_1, decrypted_text_2)

    # Тест 2.3: Проверка, что зашифрованный и расшифрованный текст не совпадают
    def test_decrypt_text_AES_not_equal(self):
      plaintext = "Test message"
      ciphertext = encrypt_text_AES(plaintext)
      decrypted_text = decrypt_text_AES(ciphertext)
      self.assertNotEqual(plaintext.encode('utf-8'), decrypted_text)

    
if __name__ == '__main__':
    unittest.main()
