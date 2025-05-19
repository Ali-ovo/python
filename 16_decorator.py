def comment():
    print("comment")


def func_out(fun):
    def func_in():
        print("please login")
        fun()

    return func_in


decorator = func_out(comment)
# decorator()


def check(fn):
    def inner():
        print("check")
        fn()

    return inner


@check  # fbc01 = check(func01)
def func01():
    print("func01")


# func01()




def print_info(get_sum):
    def fun_in(a,b):
      print("start")
      get_sum(a,b)
    return fun_in
  
def check_login(fn):
  def fun_in(a,b):
    print("check_login")
    fn(a,b)
  return fun_in
  
@print_info
@check_login
def get_sum(a,b):
  c = a + b
  print(c)

# get_sum(1,2)


def check_use(fn):
  def func_in():
    print("check_use")
    fn()
  return func_in

def check_code(fn):
  def func_in():
    print("check_code")
    fn()
  return func_in

@check_code
@check_use
def comment():
  print("comment")
  
comment()