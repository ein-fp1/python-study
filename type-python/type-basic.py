from typing import List, Tuple, Dict, Callable, Union, Optional, Final, TypeVar, Generic
from typing_extensions import TypedDict

int_var: int = 11
str_var: str = "Hello world"
float_var: float = 11.1
bool_var: bool = True
list_var: List[str] = ["1", "2", "3"]
tuple_var: Tuple[int, int, int] = (1, 2, 3)
dic_var: Dict[str, int] = {"hello": 12}
int_str_var: Union[int, str] = 3
option_var: Optional[str] = "aa"  # Union[str, None]
FINAL_INT: Final = 1
CustomType = Union[int, str]
int_str_custom_var: CustomType = 133
T = TypeVar("T")


def type_check(obj, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"Type Error : {typer}")


def cal_add(x: int, y: int) -> int:
    # type_check(x, int)
    # type_check(y, int)
    return x + y


def append_str(a: str, b: str) -> str:
    return b + b


def foo(func: Callable[[int, int], int]) -> int:
    return func(100, 200)


def void_func():
    print("void")


class Robot:

    def __init__(self, name: str, code: int):
        self.name = name
        self.code = code

    def greeting(self):
        print(f"greetings, my master call me {self.name}({self.code}).")

    def get_name(self) -> str:
        return self.name


class Point(TypedDict):
    x: int
    y: int
    z: int


class Sample(Generic[T]):

    def __init__(self, code: T):
        self.code: T = code

    def get_code(self):
        return self.code

    def set_code(self, code: T):
        self.code: T = code


int_var = cal_add(1, 2) + cal_add(1, 2)
print(cal_add(1, 2))
print(append_str("aaa", "bbb"))
print(foo(cal_add))

siri: Robot = Robot("aa", 112)
siri.greeting()

siri2: Robot = Robot("siri2", 113)

print(siri2.greeting())

int_str_var = "Union Str"
print(int_str_var)

# FINAL_INT = 3
print(FINAL_INT)

print(int_str_custom_var)
int_str_custom_var = "abcd"
print(int_str_custom_var)

point: Point = {"x": 1, "y": 2, "z": 3}
print(f"x={point['x']}, y={point['y']}, z={point['z']}")


sample1 = Sample[int](112)
sample1.set_code(222)

sample2 = Sample[str]("str")
sample2.set_code("abcabc")

print(sample1.get_code())
print(sample2.get_code())
