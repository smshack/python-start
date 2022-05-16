import calcu
import my_module
add_result = calcu.add(10,2)
sub_result = calcu.sub(10,2)
mul_result = calcu.mul(10,2)
div_result = calcu.div(10,2)
mod_result = calcu.mod(10,2)

print(add_result)  #=> 12
print(sub_result)  #=> 8
print(mul_result)  #=> 20
print(div_result)  #=> 5
print(mod_result)  #=> 0



print(my_module.three_times(10)) #=> 30
print(my_module.ten_times(10)) #=> 100