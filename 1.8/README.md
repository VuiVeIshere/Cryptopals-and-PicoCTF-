Đề yêu cầu xác định dãy nào là dãy được mã hóa AES-MODE_ECB. 
ECB là kiểu mã hóa bằng cách chia dãy hex thành các block 32 hoặc block 16 với dãy bytes.
Các khối được mã hóa bằng cùng 1 key, nếu 1 khối plaintext giống nhau thì ciphertext sẽ giống nhau. Vì thế cần chia các dãy đầu vào thành block 32 hex và tìm các block giống nhau.
Dãy có nhiều block giống nhau nhất có thể được mã hóa AES_ECB nhất

ANS: 
d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a
Số lần lặp:
3