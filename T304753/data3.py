import cyaron as c
import random as r
for i in range(1,11):
    test_data = c.IO(file_prefix="f", data_id=i)
    n=r.randint(3000,5000)
    test_data.input_writeln(n)
    for i in range(n-1):
        test_data.input_write(r.randint(1,5000))
    test_data.input_writeln(r.randint(0,5000))
    test_data.output_gen("i.exe")
    test_data.close()
